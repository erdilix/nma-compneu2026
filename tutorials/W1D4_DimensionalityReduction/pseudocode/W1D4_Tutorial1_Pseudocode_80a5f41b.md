# Pseudocode twin — W1D4 Tutorial 1: `change_of_basis`

- **Answer twin:** `../solutions/W1D4_Tutorial1_Solution_80a5f41b.py`
- **Reading view:** `../W1D4_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def change_of_basis(X, W):
  """
  Projects data onto new basis W.

  Args:
    X (numpy array of floats) : Data matrix each column corresponding to a
                                different random variable
    W (numpy array of floats) : new orthonormal basis columns correspond to
                                basis vectors

  Returns:
    (numpy array of floats)    : Data matrix expressed in new basis
  """

  # Project data onto new basis described by W
  Y = ____

  return Y


# Project data to new basis
Y = ____

# Visualize
with plt.xkcd():
  plot_data_new_basis(Y)
```

Blanks:
1. `Y` — Project data onto new basis described by W
2. `Y` — Project data to new basis
