# Pseudocode twin — W1D4 Tutorial 2: `get_sample_cov_matrix`

- **Answer twin:** `../solutions/W1D4_Tutorial2_Solution_43b4daa8.py`
- **Reading view:** `../W1D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `X` — Subtract the mean of X
2. `cov_matrix` — Calculate the covariance matrix (hint: use np.matmul)
3. `cov_matrix` — Calculate covariance matrix
4. `X` — Generate data with that covariance matrix
