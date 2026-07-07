# Pseudocode twin — W3D5 Tutorial 3: `get_regression_estimate`

- **Answer twin:** `../solutions/W3D5_Tutorial3_Solution_9134c469.py`
- **Reading view:** `../W3D5_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def get_regression_estimate(X, neuron_idx):
  """
  Estimates the connectivity matrix using lasso regression.

  Args:
    X (np.ndarray): our simulated system of shape (n_neurons, timesteps)
    neuron_idx (int):  a neuron index to compute connectivity for

  Returns:
    V (np.ndarray): estimated connectivity matrix of shape (n_neurons, n_neurons).
                    if neuron_idx is specified, V is of shape (n_neurons,).
  """
  # Extract Y and W as defined above
  W = X[:, :-1].transpose()
  Y = X[[neuron_idx], 1:].transpose()

  # Apply inverse sigmoid transformation
  Y = logit(Y)

  # Initialize regression model with no intercept and alpha=0.01
  regression = ____

  # Fit regression to the data
  regression.fit(____)

  V = regression.coef_

  return V


# Estimate causality with regression
V = get_regression_estimate(X, neuron_idx)

print(f"Regression: correlation of estimated with true connectivity: {np.corrcoef(A[neuron_idx, :], V)[1, 0]:.3f}")
print(f"Lagged correlation of estimated with true connectivity: {get_sys_corr(n_neurons, timesteps, random_state, neuron_idx=neuron_idx):.3f}")
```

Blanks:
1. `regression` — Initialize regression model with no intercept and alpha=0.01
2. `regression.fit(...)` — Fit regression to the data
