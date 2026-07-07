# W1D2 · Tutorial 6 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 6.1 — Compute predictions for this model

Blanked skeleton (fill the `____`):

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

**Blanks:** `residuals` (Compute SSE); `sse` (fill in); `AIC` (Compute AIC)

→ twin `pseudocode/W1D2_Tutorial6_Pseudocode_16748857.md` · answer `solutions/W1D2_Tutorial6_Solution_16748857.py`

---

## Exercise 6.2 — `cross_validate`

Blanked skeleton (fill the `____`):

```text
def cross_validate(x_train, y_train, max_order, n_splits):
  """ Compute MSE for k-fold validation for each order polynomial

  Args:
    x_train (ndarray): training data input vector of shape (n_samples)
    y_train (ndarray): training vector of measurements of shape (n_samples)
    max_order (scalar): max order of polynomial fit
    n_split (scalar): number of folds for k-fold validation

  Return:
    ndarray: MSE over splits for each model order, shape (n_splits, max_order + 1)

  """
  # Initialize the split method
  kfold_iterator = KFold(n_splits)

  # Initialize np array mse values for all models for each split
  mse_all = np.zeros((n_splits, max_order + 1))

  for i_split, (train_indices, val_indices) in enumerate(kfold_iterator.split(x_train)):

      # Split up the overall training data into cross-validation training and validation sets
      x_cv_train = x_train[train_indices]
      y_cv_train = y_train[train_indices]
      x_cv_val = x_train[val_indices]
      y_cv_val = y_train[val_indices]

      # Fit models
      theta_hats = ____

      # Compute MSE
      mse_this_split = ____

      mse_all[i_split] = mse_this_split

  return mse_all


# Cross-validate
max_order = 5
n_splits = 10
mse_all = cross_validate(x_train, y_train, max_order, n_splits)

# Visualize
with plt.xkcd():
  plot_cross_validate_MSE(mse_all)
```

**Blanks:** `theta_hats` (Fit models); `mse_this_split` (Compute MSE)

→ twin `pseudocode/W1D2_Tutorial6_Pseudocode_ddce210a.md` · answer `solutions/W1D2_Tutorial6_Solution_ddce210a.py`

---
