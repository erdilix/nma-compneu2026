# W1D3 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 1.1 — `make_design_matrix`

Blanked skeleton (fill the `____`):

```text
def make_design_matrix(stim, d=25):
  """Create time-lag design matrix from stimulus intensity vector.

  Args:
    stim (1D array): Stimulus intensity at each time point.
    d (number): Number of time lags to use.

  Returns
    X (2D array): GLM design matrix with shape T, d

  """
  # Create version of stimulus vector with zeros before onset
  padded_stim = np.concatenate([np.zeros(d - 1), stim])

  # Construct a matrix where each row has the d frames of
  # the stimulus preceding and including timepoint t
  T = len(stim)  # Total number of timepoints (hint: number of stimulus frames)
  X = np.zeros((T, d))
  for t in range(T):
      X[t] = ____

  return X


# Make design matrix
X = make_design_matrix(stim)

# Visualize
with plt.xkcd():
  plot_glm_matrices(X, spikes, nt=50)
```

**Blanks:** `X[t]` (fill in)

→ twin `pseudocode/W1D3_Tutorial1_Pseudocode_03ed3adf.md` · answer `solutions/W1D3_Tutorial1_Solution_03ed3adf.py`

---

## Exercise 1.2 — `predict_spike_counts_lg`

Blanked skeleton (fill the `____`):

```text
def predict_spike_counts_lg(stim, spikes, d=25):
  """Compute a vector of predicted spike counts given the stimulus.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    d (number): Number of time lags to use.

  Returns:
    yhat (1D array): Predicted spikes at each timepoint.

  """

  # Create the design matrix
  y = spikes
  constant = ____
  X = ____

  # Get the MLE weights for the LG model
  theta = ____

  # Compute predicted spike counts
  yhat = X @ theta

  return yhat


# Predict spike counts
predicted_counts = predict_spike_counts_lg(stim, spikes)

# Visualize
with plt.xkcd():
  plot_spikes_with_prediction(spikes, predicted_counts, dt_stim)
```

**Blanks:** `constant` (fill in); `X` (fill in); `theta` (Get the MLE weights for the LG model)

→ twin `pseudocode/W1D3_Tutorial1_Pseudocode_823fa455.md` · answer `solutions/W1D3_Tutorial1_Solution_823fa455.py`

---

## Exercise 1.3 — `neg_log_lik_lnp`

Blanked skeleton (fill the `____`):

```text
def neg_log_lik_lnp(theta, X, y):
  """Return -loglike for the Poisson GLM model.

  Args:
    theta (1D array): Parameter vector.
    X (2D array): Full design matrix.
    y (1D array): Data values.

  Returns:
    number: Negative log likelihood.

  """
  # Compute the Poisson log likelihood
  rate = np.exp(X @ theta)
  log_lik = y @ np.log(rate) - rate.sum()
  return -log_lik


def fit_lnp(stim, spikes, d=25):
  """Obtain MLE parameters for the Poisson GLM.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    d (number): Number of time lags to use.

  Returns:
    1D array: MLE parameters

  """

  # Build the design matrix
  y = spikes
  constant = np.ones_like(y)
  X = np.column_stack([constant, make_design_matrix(stim)])

  # Use a random vector of weights to start (mean 0, sd .2)
  x0 = np.random.normal(0, .2, d + 1)

  # Find parameters that minimize the negative log likelihood function
  res = minimize(neg_log_lik_lnp, x0, args=(X, y))

  return res["x"]


# Fit LNP model
theta_lnp = fit_lnp(stim, spikes)

# Visualize
with plt.xkcd():
  plot_spike_filter(theta_lg[1:], dt_stim, show=False, color=".5", label="LG")
  plot_spike_filter(theta_lnp[1:], dt_stim, show=False, label="LNP")
  plt.legend(loc="upper left")
  plt.show()
```

→ twin `pseudocode/W1D3_Tutorial1_Pseudocode_a988a95b.md` · answer `solutions/W1D3_Tutorial1_Solution_a988a95b.py`

---

## Exercise 1.4 — `predict_spike_counts_lnp`

Blanked skeleton (fill the `____`):

```text
def predict_spike_counts_lnp(stim, spikes, theta=None, d=25):
  """Compute a vector of predicted spike counts given the stimulus.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    theta (1D array): Filter weights; estimated if not provided.
    d (number): Number of time lags to use.

  Returns:
    yhat (1D array): Predicted spikes at each timepoint.

  """
  y = spikes
  constant = np.ones_like(spikes)
  X = np.column_stack([constant, make_design_matrix(stim)])
  if theta is None:  # Allow pre-cached weights, as fitting is slow
    theta = fit_lnp(X, y, d)

  yhat = ____
  return yhat


# Predict spike counts
yhat = ____

# Visualize
with plt.xkcd():
  plot_spikes_with_prediction(spikes, yhat, dt_stim)
```

**Blanks:** `yhat` (fill in); `yhat` (Predict spike counts)

→ twin `pseudocode/W1D3_Tutorial1_Pseudocode_ae48f475.md` · answer `solutions/W1D3_Tutorial1_Solution_ae48f475.py`

---
