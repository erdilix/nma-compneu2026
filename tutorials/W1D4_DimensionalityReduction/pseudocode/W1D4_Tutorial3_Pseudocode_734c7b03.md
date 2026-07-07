# Pseudocode twin — W1D4 Tutorial 3: `reconstruct_data`

- **Answer twin:** `../solutions/W1D4_Tutorial3_Solution_734c7b03.py`
- **Reading view:** `../W1D4_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def reconstruct_data(score, evectors, X_mean, K):
  """
  Reconstruct the data based on the top K components.

  Args:
    score (numpy array of floats)    : Score matrix
    evectors (numpy array of floats) : Matrix of eigenvectors
    X_mean (numpy array of floats)   : Vector corresponding to data mean
    K (scalar)                       : Number of components to include

  Returns:
    (numpy array of floats)          : Matrix of reconstructed data

  """

  # Reconstruct the data from the score and eigenvectors
  # Don't forget to add the mean!!
  X_reconstructed = ____

  return X_reconstructed


K = 784  # data dimensions

# Reconstruct the data based on all components
X_mean = np.mean(X, 0)
X_reconstructed = ____

# Plot the data and reconstruction
with plt.xkcd():
  plot_MNIST_reconstruction(X, X_reconstructed, K)
```

Blanks:
1. `X_reconstructed` — Don't forget to add the mean!!
2. `X_reconstructed` — fill in
