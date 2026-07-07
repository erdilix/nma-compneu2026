# W1D2 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 3.1 — `resample_with_replacement`

Blanked skeleton (fill the `____`):

```text
def resample_with_replacement(x, y):
  """Resample data points with replacement from the dataset of `x` inputs and
  `y` measurements.

  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.

  Returns:
    ndarray, ndarray: The newly resampled `x` and `y` data points.
  """

  # Get array of indices for resampled points
  sample_idx = ____

  # Sample from x and y according to sample_idx
  x_ = ____
  y_ = ____

  return x_, y_

x_, y_ = resample_with_replacement(x, y)

with plt.xkcd():
  plot_original_and_resample(x, y, x_, y_)
```

**Blanks:** `sample_idx` (Get array of indices for resampled points); `x_` (Sample from x and y according to sample_idx); `y_` (fill in)

→ twin `pseudocode/W1D2_Tutorial3_Pseudocode_81af3bd6.md` · answer `solutions/W1D2_Tutorial3_Solution_81af3bd6.py`

---

## Exercise 3.2 — `bootstrap_estimates`

Blanked skeleton (fill the `____`):

```text
def bootstrap_estimates(x, y, n=2000):
  """Generate a set of theta_hat estimates using the bootstrap method.

  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.
    n (int): The number of estimates to compute

  Returns:
    ndarray: An array of estimated parameters with size (n,)
  """
  theta_hats = np.zeros(n)

  # Loop over number of estimates
  for i in range(n):

    # Resample x and y
    x_, y_ = resample_with_replacement(x, y)

    # Compute theta_hat for this sample
    theta_hats[i] = ____

  return theta_hats

# Set random seed
np.random.seed(123)

# Get bootstrap estimates
theta_hats = bootstrap_estimates(x, y, n=2000)
print(theta_hats[0:5])
```

**Blanks:** `theta_hats[i]` (Compute theta_hat for this sample)

→ twin `pseudocode/W1D2_Tutorial3_Pseudocode_d73b40e4.md` · answer `solutions/W1D2_Tutorial3_Solution_d73b40e4.py`

---
