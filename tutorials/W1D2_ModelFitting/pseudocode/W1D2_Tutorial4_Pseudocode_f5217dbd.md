# Pseudocode twin — W1D2 Tutorial 4: `solve_poly_reg`

- **Answer twin:** `../solutions/W1D2_Tutorial4_Solution_f5217dbd.py`
- **Reading view:** `../W1D2_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def solve_poly_reg(x, y, max_order):
  """Fit a polynomial regression model for each order 0 through max_order.

  Args:
    x (ndarray): input vector of shape (n_samples)
    y (ndarray): vector of measurements of shape (n_samples)
    max_order (scalar): max order for polynomial fits

  Returns:
    dict: fitted weights for each polynomial model (dict key is order)
  """

  # Create a dictionary with polynomial order as keys,
  # and np array of theta_hat (weights) as the values
  theta_hats = {}

  # Loop over polynomial orders from 0 through max_order
  for order in range(max_order + 1):

    # Create design matrix
    X_design = ____

    # Fit polynomial model
    this_theta = ____

    theta_hats[order] = this_theta

  return theta_hats


max_order = 5
theta_hats = solve_poly_reg(x, y, max_order)

# Visualize
with plt.xkcd():
  plot_fitted_polynomials(x, y, theta_hats)
```

Blanks:
1. `X_design` — Create design matrix
2. `this_theta` — Fit polynomial model
