# Pseudocode twin — W1D3 Tutorial 2: `model_selection`

- **Answer twin:** `../solutions/W1D3_Tutorial2_Solution_6bf38e57.py`
- **Reading view:** `../W1D3_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `model` — (Hint, you may need to set max_iter)
2. `accs` — Get the accuracy for each test split using cross-validation
3. `accuracies.append(...)` — Store the average test accuracy for this value of C
