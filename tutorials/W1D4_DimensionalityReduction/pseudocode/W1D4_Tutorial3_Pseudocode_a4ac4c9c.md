# Pseudocode twin — W1D4 Tutorial 3: `get_variance_explained`

- **Answer twin:** `../solutions/W1D4_Tutorial3_Solution_a4ac4c9c.py`
- **Reading view:** `../W1D4_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def get_variance_explained(evals):
  """
  Plots eigenvalues.

  Args:
    (numpy array of floats) : Vector of eigenvalues

  Returns:
    Nothing.

  """

  # Cumulatively sum the eigenvalues
  csum = ____

  # Normalize by the sum of eigenvalues
  variance_explained = ____

  return variance_explained


# Calculate the variance explained
variance_explained = ____

# Visualize
with plt.xkcd():
  plot_variance_explained(variance_explained)
```

Blanks:
1. `csum` — Cumulatively sum the eigenvalues
2. `variance_explained` — Normalize by the sum of eigenvalues
3. `variance_explained` — Calculate the variance explained
