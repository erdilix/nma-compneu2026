# Pseudocode twin — W1D2 Tutorial 2: `likelihood`

- **Answer twin:** `../solutions/W1D2_Tutorial2_Solution_328a0c30.py`
- **Reading view:** `../W1D2_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `pdf` — Compute Gaussian likelihood
