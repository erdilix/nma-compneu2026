# Pseudocode twin — W1D2 Tutorial 1: `solve_normal_eqn`

- **Answer twin:** `../solutions/W1D2_Tutorial1_Solution_7a89ba24.py`
- **Reading view:** `../W1D2_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def solve_normal_eqn(x, y):
  """Solve the normal equations to produce the value of theta_hat that minimizes
    MSE.

    Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.

  Returns:
    float: the value for theta_hat arrived from minimizing MSE
  """

  # Compute theta_hat analytically
  theta_hat = ____

  return theta_hat


theta_hat = ____
y_hat = theta_hat * x

with plt.xkcd():
  plot_observed_vs_predicted(x, y, y_hat, theta_hat)
```

Blanks:
1. `theta_hat` — Compute theta_hat analytically
2. `theta_hat` — fill in
