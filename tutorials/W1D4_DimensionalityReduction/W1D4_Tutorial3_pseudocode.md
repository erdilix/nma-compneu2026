# W1D4 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **6** code exercise(s).

---

## Exercise 3.1 — Perform PCA

Blanked skeleton (fill the `____`):

```text
# Perform PCA
score, evectors, evals = pca(X)

# Plot the eigenvalues
with plt.xkcd():
  plot_eigenvalues(evals, xlimit=True)  # limit x-axis up to 100 for zooming
```

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_1ea6324a.md` · answer `solutions/W1D4_Tutorial3_Solution_1ea6324a.py`

---

## Exercise 3.2 — `reconstruct_data`

Blanked skeleton (fill the `____`):

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

**Blanks:** `X_reconstructed` (Don't forget to add the mean!!); `X_reconstructed` (fill in)

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_734c7b03.md` · answer `solutions/W1D4_Tutorial3_Solution_734c7b03.py`

---

## Exercise 3.3 — TO DO for students

Blanked skeleton (fill the `____`):

```text
np.random.seed(2020)  # set random seed

# Add noise to data
X_noisy = ____

# Perform PCA on noisy data
score_noisy, evectors_noisy, evals_noisy = pca(X_noisy)

# Compute variance explained
variance_explained_noisy = ____

# Visualize
with plt.xkcd():
  plot_MNIST_sample(X_noisy)
  plot_variance_explained(variance_explained_noisy)
```

**Blanks:** `X_noisy` (Add noise to data); `variance_explained_noisy` (Compute variance explained)

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_9615a6cd.md` · answer `solutions/W1D4_Tutorial3_Solution_9615a6cd.py`

---

## Exercise 3.4 — `get_variance_explained`

Blanked skeleton (fill the `____`):

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

**Blanks:** `csum` (Cumulatively sum the eigenvalues); `variance_explained` (Normalize by the sum of eigenvalues); `variance_explained` (Calculate the variance explained)

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_a4ac4c9c.md` · answer `solutions/W1D4_Tutorial3_Solution_a4ac4c9c.py`

---

## Exercise 3.5 — TO DO for students

Blanked skeleton (fill the `____`):

```text
np.random.seed(2020)  # set random seed

# Add noise to data
X_noisy = ____

# Compute mean of noise-corrupted data
X_noisy_mean = ____

# Project onto the original basis vectors
projX_noisy = ____

# Reconstruct the data using the top 50 components
K = 50
X_reconstructed = ____

# Visualize
with plt.xkcd():
  plot_MNIST_reconstruction(X_noisy, X_reconstructed, K)
```

**Blanks:** `X_noisy` (Add noise to data); `X_noisy_mean` (Compute mean of noise-corrupted data); `projX_noisy` (Project onto the original basis vectors); `X_reconstructed` (fill in)

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_b083f0cf.md` · answer `solutions/W1D4_Tutorial3_Solution_b083f0cf.py`

---

## Exercise 3.6 — Comment once you've filled in the function

Blanked skeleton (fill the `____`):

```text
# Plot the weights of the first principal component
with plt.xkcd():
plot_MNIST_weights(____)
```

**Blanks:** `plot_MNIST_weights(...)` (fill the ____ argument(s))

→ twin `pseudocode/W1D4_Tutorial3_Pseudocode_d27990ad.md` · answer `solutions/W1D4_Tutorial3_Solution_d27990ad.py`

---
