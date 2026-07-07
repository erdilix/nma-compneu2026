# Pseudocode twin — W3D5 Tutorial 4: `fit_second_stage`

- **Answer twin:** `../solutions/W3D5_Tutorial4_Solution_778b0511.py`
- **Reading view:** `../W3D5_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def fit_second_stage(T_hat, Y):
  """
  Estimates a scalar causal effect from 2-stage least squares regression using
  an instrument.

  Args:
      T_hat (np.ndarray): the output of the first stage regression
      Y (np.ndarray): our observed response (n, 1)

  Returns:
      beta (float): the estimated causal effect
  """
  # Initialize linear regression model
  stage2 = LinearRegression(fit_intercept=True)

  # Fit model to data
  stage2.fit(____)

  return stage2.coef_


# Fit first stage
T_hat = fit_first_stage(T, Z)

# Fit second stage
beta = fit_second_stage(T_hat, Y)

# Print
print(f"Estimated causal effect is: {beta[0, 0]:.3f}")
```

Blanks:
1. `stage2.fit(...)` — Fit model to data
