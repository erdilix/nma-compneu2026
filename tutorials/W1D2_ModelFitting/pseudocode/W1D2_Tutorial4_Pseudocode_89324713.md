# Pseudocode twin — W1D2 Tutorial 4: Get prediction for the polynomial regression model of this o

- **Answer twin:** `../solutions/W1D2_Tutorial4_Solution_89324713.py`
- **Reading view:** `../W1D2_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `y_hat` — Get prediction for the polynomial regression model of this order
2. `residuals` — Compute the residuals
3. `mse` — Compute the MSE
