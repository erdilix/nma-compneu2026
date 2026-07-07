# W1D3 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 2.1 — `compute_accuracy`

Blanked skeleton (fill the `____`):

```text
def compute_accuracy(X, y, model):
  """Compute accuracy of classifier predictions.

  Args:
    X (2D array): Data matrix
    y (1D array): Label vector
    model (sklearn estimator): Classifier with trained weights.

  Returns:
    accuracy (float): Proportion of correct predictions.
  """

  y_pred = model.predict(X)

  accuracy = ____

  return accuracy


# Compute train accuracy
train_accuracy = compute_accuracy(X, y, log_reg)
print(f"Accuracy on the training data: {train_accuracy:.2%}")
```

**Blanks:** `accuracy` (fill in)

→ twin `pseudocode/W1D3_Tutorial2_Pseudocode_1485808c.md` · answer `solutions/W1D3_Tutorial2_Solution_1485808c.py`

---

## Exercise 2.2 — `count_non_zero_coefs`

Blanked skeleton (fill the `____`):

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

**Blanks:** `model` ((Hint, you may need to set max_iter)); `coefs` (Get the coefs of the fit model (in sklearn, we can do this using model.coef_)); `non_zero` (Count the number of non-zero elements in coefs)

→ twin `pseudocode/W1D3_Tutorial2_Pseudocode_19d58990.md` · answer `solutions/W1D3_Tutorial2_Solution_19d58990.py`

---

## Exercise 2.3 — `model_selection`

Blanked skeleton (fill the `____`):

```text
def model_selection(X, y, C_values):
  """Compute CV accuracy for each C value.

  Args:
    X (2D array): Data matrix
    y (1D array): Label vector
    C_values (1D array): Array of hyperparameter values.

  Returns:
    accuracies (1D array): CV accuracy with each value of C.

  """
  accuracies = []
  for C in C_values:

    # Initialize and fit the model
    # (Hint, you may need to set max_iter)
    model = ____

    # Get the accuracy for each test split using cross-validation
    accs = ____

    # Store the average test accuracy for this value of C
    accuracies.append(____)

  return accuracies


# Use log-spaced values for C
C_values = np.logspace(-4, 4, 9)

# Compute accuracies
accuracies = model_selection(X, y, C_values)

# Visualize
with plt.xkcd():
  plot_model_selection(C_values, accuracies)
```

**Blanks:** `model` ((Hint, you may need to set max_iter)); `accs` (Get the accuracy for each test split using cross-validation); `accuracies.append(...)` (Store the average test accuracy for this value of C)

→ twin `pseudocode/W1D3_Tutorial2_Pseudocode_6bf38e57.md` · answer `solutions/W1D3_Tutorial2_Solution_6bf38e57.py`

---

## Exercise 2.4 — `sigmoid`

Blanked skeleton (fill the `____`):

```text
def sigmoid(z):
  """Return the logistic transform of z."""

  sigmoid = ____

  return sigmoid


# Visualize
with plt.xkcd():
  plot_function(sigmoid, "\sigma", "z", (-10, 10))
```

**Blanks:** `sigmoid` (fill in)

→ twin `pseudocode/W1D3_Tutorial2_Pseudocode_89590c8d.md` · answer `solutions/W1D3_Tutorial2_Solution_89590c8d.py`

---
