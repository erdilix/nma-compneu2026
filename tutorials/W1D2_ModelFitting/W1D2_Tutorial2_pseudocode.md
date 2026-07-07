# W1D2 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **1** code exercise(s).

---

## Exercise 2.1 — `likelihood`

Blanked skeleton (fill the `____`):

```text
def likelihood(theta_hat, x, y):
  """The likelihood function for a linear model with noise sampled from a
    Gaussian distribution with zero mean and unit variance.

  Args:
    theta_hat (float): An estimate of the slope parameter.
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.

  Returns:
    float: the likelihood value for the theta_hat estimate
  """
  sigma = 1

  # Compute Gaussian likelihood
  pdf = ____

  return pdf


print(likelihood(1.0, x[1], y[1]))
```

**Blanks:** `pdf` (Compute Gaussian likelihood)

→ twin `pseudocode/W1D2_Tutorial2_Pseudocode_328a0c30.md` · answer `solutions/W1D2_Tutorial2_Solution_328a0c30.py`

---
