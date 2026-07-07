# Pseudocode twin — W1D4 Tutorial 1: `define_orthonormal_basis`

- **Answer twin:** `../solutions/W1D4_Tutorial1_Solution_590fa120.py`
- **Reading view:** `../W1D4_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def define_orthonormal_basis(u):
  """
  Calculates an orthonormal basis given an arbitrary vector u.

  Args:
    u (numpy array of floats) : arbitrary 2-dimensional vector used for new
                                basis

  Returns:
    (numpy array of floats)   : new orthonormal basis
                                columns correspond to basis vectors
  """

  # Normalize vector u
  u = ____

  # Calculate vector w that is orthogonal to u
  w = ____

  # Put in matrix form
  W = np.column_stack([u, w])

  return W


# Set up parameters
np.random.seed(2020)  # set random seed
variance_1 = 1
variance_2 = 1
corr_coef = 0.8
u = ____

# Compute covariance matrix
cov_matrix = calculate_cov_matrix(variance_1, variance_2, corr_coef)

# Generate data
X = get_data(cov_matrix)

# Get orthonomal basis
W = define_orthonormal_basis(u)

# Visualize
with plt.xkcd():
  plot_basis_vectors(X, W)
```

Blanks:
1. `u` — Normalize vector u
2. `w` — Calculate vector w that is orthogonal to u
3. `u` — fill in
