# W2D4 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 2.1 — `my_CC`

Blanked skeleton (fill the `____`):

```text
def my_CC(i, j):
  """
  Args:
    i, j  : two time series with the same length

  Returns:
    rij   : correlation coefficient
  """

  # Calculate the covariance of i and j
  cov = ____

  # Calculate the variance of i
  var_i = ____

  # Calculate the variance of j
  var_j = ____

  # Calculate the correlation coefficient
  rij = ____

  return rij


with plt.xkcd():
  example_plot_myCC()
```

**Blanks:** `cov` (Calculate the covariance of i and j); `var_i` (Calculate the variance of i); `var_j` (Calculate the variance of j); `rij` (Calculate the correlation coefficient)

→ twin `pseudocode/W2D4_Tutorial2_Pseudocode_313f41e4.md` · answer `solutions/W2D4_Tutorial2_Solution_313f41e4.py`

---

## Exercise 2.2 — `corr_coeff_pairs`

Blanked skeleton (fill the `____`):

```text
def corr_coeff_pairs(pars, rate, c, trials, bins):
  """
  Calculate the correlation coefficient of two spike trains, for different
  realizations

  Args:
      pars   : parameter dictionary
      rate   : rate of poisson inputs
      c      : correlation coefficient ~ [0, 1]
      trials : number of realizations
      bins   : vector with bins for time discretization

  Returns:
    r12      : correlation coefficient of a pair of inputs
  """

  r12 = np.zeros(trials)

  for i in range(trials):
    # Generate correlated Poisson inputs
    sp1, sp2 = generate_corr_Poisson(pars, poi_rate, c, myseed=2020+i)

    # Bin the spike times of the first input
    sp1_count, _ = np.histogram(sp1, bins=bins)

    # Bin the spike times of the second input
    sp2_count, _ = np.histogram(sp2, bins=bins)

    # Calculate the correlation coefficient
    r12[i] = my_CC(sp1_count, sp2_count)

  return r12


poi_rate = 20.
c = 0.2  # set true correlation
pars = default_pars(T=10000)
# bin the spike time
bin_size = 20  # [ms]
my_bin = np.arange(0, pars['T'], bin_size)
n_trials = 100  # 100 realizations

r12 = corr_coeff_pairs(pars, rate=poi_rate, c=c, trials=n_trials, bins=my_bin)
print(f'True corr coe = {c:.3f}')
print(f'Simu corr coe = {r12.mean():.3f}')
```

→ twin `pseudocode/W2D4_Tutorial2_Pseudocode_f3c21c6b.md` · answer `solutions/W2D4_Tutorial2_Solution_f3c21c6b.py`

---
