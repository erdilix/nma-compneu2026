# Pseudocode twin — W1D2 Tutorial 1: `mse`

- **Answer twin:** `../solutions/W1D2_Tutorial1_Solution_12a57de0.py`
- **Reading view:** `../W1D2_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def mse(x, y, theta_hat):
  """Compute the mean squared error

  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.
    theta_hat (float): An estimate of the slope parameter

  Returns:
    float: The mean squared error of the data with the estimated parameter.
  """

  # Compute the estimated y
  y_hat = ____

  # Compute mean squared error
  mse = ____

  return mse


theta_hats = [0.75, 1.0, 1.5]
for theta_hat in theta_hats:
  print(f"theta_hat of {theta_hat} has an MSE of {mse(x, y, theta_hat):.2f}")
```

Blanks:
1. `y_hat` — Compute the estimated y
2. `mse` — Compute mean squared error
