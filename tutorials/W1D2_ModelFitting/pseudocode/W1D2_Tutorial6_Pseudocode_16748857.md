# Pseudocode twin — W1D2 Tutorial 6: Compute predictions for this model

- **Answer twin:** `../solutions/W1D2_Tutorial6_Solution_16748857.py`
- **Reading view:** `../W1D2_Tutorial6_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
AIC_list = []
order_list = list(range(max_order + 1))

for order in order_list:

  # Compute predictions for this model
  X_design = make_design_matrix(x_train, order)
  y_hat = np.dot(X_design, theta_hats[order])

  # Compute SSE
  residuals = ____
  sse = ____

  # Get K
  K = len(theta_hats[order])

  # Compute AIC
  AIC = ____

  AIC_list.append(AIC)

# Visualize
with plt.xkcd():
  plt.bar(order_list, AIC_list)
  plt.ylabel('AIC')
  plt.xlabel('polynomial order')
  plt.title('comparing polynomial fits')
  plt.show()
```

Blanks:
1. `residuals` — Compute SSE
2. `sse` — fill in
3. `AIC` — Compute AIC
