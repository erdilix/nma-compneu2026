# Pseudocode twin — W1D3 Tutorial 2: `count_non_zero_coefs`

- **Answer twin:** `../solutions/W1D3_Tutorial2_Solution_19d58990.py`
- **Reading view:** `../W1D3_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def count_non_zero_coefs(X, y, C_values):
  """Fit models with different L1 penalty values and count non-zero coefficients.

  Args:
    X (2D array): Data matrix
    y (1D array): Label vector
    C_values (1D array): List of hyperparameter values

  Returns:
    non_zero_coefs (list): number of coefficients in each model that are nonzero

  """
  non_zero_coefs = []
  for C in C_values:

    # Initialize and fit the model
    # (Hint, you may need to set max_iter)
    model = ____
    model.fit(X,y)

    # Get the coefs of the fit model (in sklearn, we can do this using model.coef_)
    coefs = ____

    # Count the number of non-zero elements in coefs
    non_zero = ____
    non_zero_coefs.append(non_zero)

  return non_zero_coefs


# Use log-spaced values for C
C_values = np.logspace(-4, 4, 5)

# Count non zero coefficients
non_zero_l1 = count_non_zero_coefs(X, y, C_values)

# Visualize
with plt.xkcd():
  plot_non_zero_coefs(C_values, non_zero_l1, n_voxels=X.shape[1])
```

Blanks:
1. `model` — (Hint, you may need to set max_iter)
2. `coefs` — Get the coefs of the fit model (in sklearn, we can do this using model.coef_)
3. `non_zero` — Count the number of non-zero elements in coefs
