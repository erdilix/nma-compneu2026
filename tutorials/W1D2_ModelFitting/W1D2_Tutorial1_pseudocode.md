# W1D2 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 1.1 — `mse`

Blanked skeleton (fill the `____`):

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

**Blanks:** `y_hat` (Compute the estimated y); `mse` (Compute mean squared error)

→ twin `pseudocode/W1D2_Tutorial1_Pseudocode_12a57de0.md` · answer `solutions/W1D2_Tutorial1_Solution_12a57de0.py`

---

## Exercise 1.2 — `solve_normal_eqn`

Blanked skeleton (fill the `____`):

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

**Blanks:** `theta_hat` (Compute theta_hat analytically); `theta_hat` (fill in)

→ twin `pseudocode/W1D2_Tutorial1_Pseudocode_7a89ba24.md` · answer `solutions/W1D2_Tutorial1_Solution_7a89ba24.py`

---
