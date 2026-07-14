# Basic Bayesian observer for motion-direction estimation

> Markdown twin of `projects/behavior_and_theory/earth_laquitaine.ipynb`.
> Reworked from the Laquitaine & Gardner prior-learning demo into a minimal **Bayesian inference** model, built step by step following **W3D2 Bayesian Decisions, Tutorial 2** (continuous state: Gaussian prior × Gaussian likelihood = Gaussian posterior).

Inspired by [Laquitaine & Gardner, Neuron, 2017](https://www.cell.com/neuron/fulltext/S0896-6273(17)31134-0).

**The plan.** Each cell adds one piece. Run them top to bottom:

1. Set up the state space (all possible motion directions).
2. Build the **prior** — directions the experiment shows more often.
3. Build the **likelihood** — this trial's noisy sensory measurement.
4. Apply **Bayes rule** — multiply and normalize to get the **posterior**.
5. Read out the estimate (MAP) and see the **bias toward the prior**.
6. Sweep many trials to see the classic effect: weaker signal → stronger prior pull.

---

## Dependencies

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['figure.figsize'] = [8, 4]
rcParams['font.size'] = 11
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False
rcParams['figure.autolayout'] = True
```

## Step 0 — one helper: a Gaussian on a grid

Both the prior and the likelihood are Gaussians evaluated on the same grid of directions. This is the `my_gaussian` from W3D2 Tutorial 2, normalized so it sums to 1 on the discrete grid.

```python
def my_gaussian(x, mu, sigma):
    """Gaussian probability density over the state space x (normalized on the grid)."""
    px = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / np.sqrt(2 * np.pi * sigma ** 2)
    return px / px.sum()
```

## Step 1 — the state space

All motion directions the observer could report, in degrees.

```python
x = np.arange(1, 360, 1)   # motion directions (deg)
print('state space:', x[0], '...', x[-1], 'deg  (', len(x), 'points )')
```

## Step 2 — the prior

The experiment shows some directions more often. The observer's prior is a Gaussian centred on that most-frequent direction. `PRIOR_SIGMA` sets how strong (narrow) the prior belief is.

```python
PRIOR_MEAN = 225    # most frequent direction (deg)
PRIOR_SIGMA = 40    # prior width: smaller = stronger prior

prior = my_gaussian(x, PRIOR_MEAN, PRIOR_SIGMA)

plt.plot(x, prior, color=[0.75, 0.75, 0])
plt.title(f'Prior over directions (mean {PRIOR_MEAN}°, sigma {PRIOR_SIGMA}°)')
plt.xlabel('Motion direction (deg)'); plt.ylabel('Probability')
plt.show()
```

## Step 3 — the likelihood

On a trial the observer gets a noisy sensory measurement of the true direction. The likelihood is a Gaussian centred on that measurement; its width `SENSORY_SIGMA` encodes signal quality — small = strong signal (high coherence), large = weak signal.

```python
MEASUREMENT = 190     # measured direction this trial (deg)
SENSORY_SIGMA = 25    # likelihood width: small = strong signal

likelihood = my_gaussian(x, MEASUREMENT, SENSORY_SIGMA)

plt.plot(x, prior, color=[0.75, 0.75, 0], label='prior')
plt.plot(x, likelihood, color=[0, 0.5, 1], label='likelihood')
plt.title(f'Likelihood of measurement = {MEASUREMENT}°')
plt.xlabel('Motion direction (deg)'); plt.ylabel('Probability')
plt.legend(); plt.show()
```

## Step 4 — Bayes rule: posterior = prior × likelihood

Multiply the two distributions pointwise, then normalize so the result is a true PDF. This is the whole of Bayesian inference on a grid.

```python
def compute_posterior(prior, likelihood):
    """Bayes rule on a grid: posterior proportional to prior * likelihood."""
    posterior = np.multiply(prior, likelihood)
    return posterior / posterior.sum()

posterior = compute_posterior(prior, likelihood)
```

## Step 5 — read out the estimate and see the prior bias

The observer reports the peak of the posterior (the MAP estimate). It lands **between** the measurement and the prior mean — the estimate is pulled toward the prior.

```python
estimate = x[np.argmax(posterior)]   # MAP readout

plt.plot(x, prior, label='prior', color=[0.75, 0.75, 0])
plt.plot(x, likelihood, label='likelihood (measurement)', color=[0, 0.5, 1])
plt.plot(x, posterior, label='posterior', color=[1, 0, 0], lw=2)
plt.axvline(MEASUREMENT, color=[0, 0.5, 1], ls='--', lw=1)
plt.axvline(estimate, color=[1, 0, 0], ls='--', lw=1)
plt.title(f'measurement={MEASUREMENT}°  ->  MAP estimate={estimate}° (pulled toward prior {PRIOR_MEAN}°)')
plt.xlabel('Motion direction (deg)'); plt.ylabel('Probability')
plt.legend(); plt.show()

print(f'measurement      : {MEASUREMENT} deg')
print(f'MAP estimate     : {estimate} deg')
print(f'bias toward prior: {estimate - MEASUREMENT:+d} deg')
```

> Try re-running Step 3 with a larger `SENSORY_SIGMA` (weaker signal) and watch the estimate move closer to the prior mean of 225°.

## Step 6 — many trials: prior bias grows as the signal weakens

Wrap Steps 2–5 in one function, then sweep true directions at three signal levels. The gap between each curve and the dashed unbiased line is the Bayesian bias — the model's central prediction.

```python
def bayesian_estimate(measurement, prior_mean, prior_sigma, sensory_sigma):
    """MAP estimate for one noisy measurement (Steps 2-5 combined)."""
    prior = my_gaussian(x, prior_mean, prior_sigma)
    likelihood = my_gaussian(x, measurement, sensory_sigma)
    posterior = compute_posterior(prior, likelihood)
    return x[np.argmax(posterior)]


true_dirs = np.arange(100, 350, 5)
coherences = {'strong signal (sigma=10)': 10,
              'medium signal (sigma=30)': 30,
              'weak signal (sigma=60)': 60}

plt.plot(true_dirs, true_dirs, 'k--', label='unbiased (estimate = true)')
for label, sensory_sigma in coherences.items():
    estimates = [bayesian_estimate(d, PRIOR_MEAN, PRIOR_SIGMA, sensory_sigma) for d in true_dirs]
    plt.plot(true_dirs, estimates, label=label)

plt.axhline(PRIOR_MEAN, color='gray', ls=':', lw=1)
plt.axvline(PRIOR_MEAN, color='gray', ls=':', lw=1)
plt.title('Estimates pulled toward the prior (225°); weaker signal = stronger pull')
plt.xlabel('True motion direction (deg)'); plt.ylabel('Reported (MAP) estimate (deg)')
plt.legend(); plt.show()
```

## What this is and where to take it

A minimal Bayesian observer: a prior, a likelihood, one multiply, a MAP readout — the machinery from **W3D2 Tutorial 2**. It reproduces the paper's central qualitative effect: **estimates are attracted to the prior, and the attraction grows as sensory reliability drops.**

Next steps:

- **Circular version.** Directions live on a circle (359° and 1° are neighbours). Swap `my_gaussian` for a Von Mises (`scipy.stats.vonmises`), concentration κ ≈ 1/σ². See W3D2 for the circular treatment.
- **Fit to data.** Compute the negative log likelihood of a subject's reports under this model and fit `prior_sigma` / `sensory_sigma` — the parameter-recovery workflow in **W3D2 Tutorial 3** (+ W1D2 Model Fitting). Real data lives in `laquitaine_human_errors.ipynb`.
- **Loss functions.** MAP is one readout; the posterior mean minimizes squared error. W3D2 Tutorial 2 covers expected-utility readouts.
