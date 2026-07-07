# Pseudocode twin — W1D2 Tutorial 5: `compute_mse`

- **Answer twin:** `../solutions/W1D2_Tutorial5_Solution_bb5f169f.py`
- **Reading view:** `../W1D2_Tutorial5_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def compute_mse(x_train, x_test, y_train, y_test, theta_hats, max_order):
  """Compute MSE on training data and test data.

  Args:
    x_train(ndarray): training data input vector of shape (n_samples)
    x_test(ndarray): test vector of shape (n_samples)
    y_train(ndarray): training vector of measurements of shape (n_samples)
    y_test(ndarray): test vector of measurements of shape (n_samples)
    theta_hats(dict): fitted weights for each polynomial model (dict key is order)
    max_order (scalar): max order of polynomial fit

  Returns:
    ndarray, ndarray: MSE error on training data and test data for each order
  """

  mse_train = ____
  mse_test = ____

  return mse_train, mse_test


# Compute train and test MSE
mse_train, mse_test = compute_mse(x_train, x_test, y_train, y_test, theta_hats, max_order)

# Visualize
with plt.xkcd():
  plot_MSE_poly_fits(mse_train, mse_test, max_order)
```

Blanks:
1. `mse_train` — fill in
2. `mse_test` — fill in
