# Pseudocode twin — W1D4 Tutorial 2: `pca`

- **Answer twin:** `../solutions/W1D4_Tutorial2_Solution_3fc5faa0.py`
- **Reading view:** `../W1D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def pca(X):
  """
  Performs PCA on multivariate data.

  Args:
    X (numpy array of floats) : Data matrix each column corresponds to a
                                different random variable

  Returns:
    (numpy array of floats)   : Data projected onto the new basis
    (numpy array of floats)   : Vector of eigenvalues
    (numpy array of floats)   : Corresponding matrix of eigenvectors

  """

  # Calculate the sample covariance matrix
  cov_matrix = ____

  # Calculate the eigenvalues and eigenvectors
  evals, evectors = np.linalg.eigh(cov_matrix)

  # Sort the eigenvalues in descending order
  evals, evectors = sort_evals_descending(evals, evectors)

  # Project the data onto the new eigenvector basis
  score = ____

  return score, evectors, evals


# Perform PCA on the data matrix X
score, evectors, evals = pca(X)

# Plot the data projected into the new basis
with plt.xkcd():
  plot_data_new_basis(score)
```

Blanks:
1. `cov_matrix` — Calculate the sample covariance matrix
2. `score` — Project the data onto the new eigenvector basis
