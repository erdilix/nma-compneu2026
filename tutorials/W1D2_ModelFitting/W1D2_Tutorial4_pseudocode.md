# W1D2 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 4.1 — `ordinary_least_squares`

Blanked skeleton (fill the `____`):

```text
def ordinary_least_squares(X, y):
  """Ordinary least squares estimator for linear regression.

  Args:
    X (ndarray): design matrix of shape (n_samples, n_regressors)
    y (ndarray): vector of measurements of shape (n_samples)

  Returns:
    ndarray: estimated parameter values of shape (n_regressors)
  """

  # Compute theta_hat using OLS
  theta_hat = ____

  return theta_hat


theta_hat = ____
print(theta_hat)
```

**Blanks:** `theta_hat` (Compute theta_hat using OLS); `theta_hat` (fill in)

→ twin `pseudocode/W1D2_Tutorial4_Pseudocode_25849be9.md` · answer `solutions/W1D2_Tutorial4_Solution_25849be9.py`

---

## Exercise 4.2 — `make_design_matrix`

Blanked skeleton (fill the `____`):

```text
def make_design_matrix(x, order):
  """Create the design matrix of inputs for use in polynomial regression

  Args:
    x (ndarray): input vector of shape (samples,)
    order (scalar): polynomial regression order

  Returns:
    ndarray: design matrix for polynomial regression of shape (samples, order+1)
  """

  # Broadcast to shape (n x 1) so dimensions work
  if x.ndim == 1:
    x = x[:, None]

  #if x has more than one feature, we don't want multiple columns of ones so we assign
  # x^0 here
  design_matrix = ____

  # Loop through rest of degrees and stack columns (hint: np.hstack)
  for degree in range(1, order + 1):
      design_matrix = ____

  return design_matrix


order = 5
X_design = make_design_matrix(x, order)

print(X_design[0:2, 0:2])
```

**Blanks:** `design_matrix` (x^0 here); `design_matrix` (fill in)

→ twin `pseudocode/W1D2_Tutorial4_Pseudocode_5e30078a.md` · answer `solutions/W1D2_Tutorial4_Solution_5e30078a.py`

---

## Exercise 4.3 — Get prediction for the polynomial regression model of this o

Blanked skeleton (fill the `____`):

```text
mse_list = []
order_list = list(range(max_order + 1))

for order in order_list:

  X_design = make_design_matrix(x, order)

  # Get prediction for the polynomial regression model of this order
  y_hat = ____

  # Compute the residuals
  residuals = ____

  # Compute the MSE
  mse = ____

  mse_list.append(mse)


# Visualize MSE of fits
with plt.xkcd():
  evaluate_fits(order_list, mse_list)
```

**Blanks:** `y_hat` (Get prediction for the polynomial regression model of this order); `residuals` (Compute the residuals); `mse` (Compute the MSE)

→ twin `pseudocode/W1D2_Tutorial4_Pseudocode_89324713.md` · answer `solutions/W1D2_Tutorial4_Solution_89324713.py`

---

## Exercise 4.4 — `solve_poly_reg`

Blanked skeleton (fill the `____`):

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

**Blanks:** `X_design` (Create design matrix); `this_theta` (Fit polynomial model)

→ twin `pseudocode/W1D2_Tutorial4_Pseudocode_f5217dbd.md` · answer `solutions/W1D2_Tutorial4_Solution_f5217dbd.py`

---
