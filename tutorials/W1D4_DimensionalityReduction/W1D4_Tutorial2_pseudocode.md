# W1D4 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 2.1 — `pca`

Blanked skeleton (fill the `____`):

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

**Blanks:** `cov_matrix` (Calculate the sample covariance matrix); `score` (Project the data onto the new eigenvector basis)

→ twin `pseudocode/W1D4_Tutorial2_Pseudocode_3fc5faa0.md` · answer `solutions/W1D4_Tutorial2_Solution_3fc5faa0.py`

---

## Exercise 2.2 — `get_sample_cov_matrix`

Blanked skeleton (fill the `____`):

```text
def get_sample_cov_matrix(X):
  """
  Returns the sample covariance matrix of data X

  Args:
    X (numpy array of floats) : Data matrix each column corresponds to a
                                different random variable

  Returns:
    (numpy array of floats)   : Covariance matrix
  """

  # Subtract the mean of X
  X = ____

  # Calculate the covariance matrix (hint: use np.matmul)
  cov_matrix = ____

  return cov_matrix


# Set parameters
np.random.seed(2020)  # set random seed
variance_1 = 1
variance_2 = 1
corr_coef = 0.8

# Calculate covariance matrix
cov_matrix = ____
print(cov_matrix)

# Generate data with that covariance matrix
X = ____

# Get sample covariance matrix
sample_cov_matrix = get_sample_cov_matrix(X)
print(sample_cov_matrix)
```

**Blanks:** `X` (Subtract the mean of X); `cov_matrix` (Calculate the covariance matrix (hint: use np.matmul)); `cov_matrix` (Calculate covariance matrix); `X` (Generate data with that covariance matrix)

→ twin `pseudocode/W1D4_Tutorial2_Pseudocode_43b4daa8.md` · answer `solutions/W1D4_Tutorial2_Solution_43b4daa8.py`

---

## Exercise 2.3 — Calculate the eigenvalues and eigenvectors

Blanked skeleton (fill the `____`):

```text
# Calculate the eigenvalues and eigenvectors
evals, evectors = np.linalg.eigh(cov_matrix)

# Sort the eigenvalues in descending order
evals, evectors = sort_evals_descending(evals, evectors)

# Visualize
with plt.xkcd():
  plot_basis_vectors(X, evectors)
```

→ twin `pseudocode/W1D4_Tutorial2_Pseudocode_97bca56d.md` · answer `solutions/W1D4_Tutorial2_Solution_97bca56d.py`

---
