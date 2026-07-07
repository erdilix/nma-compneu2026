# W1D4 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 1.1 — `define_orthonormal_basis`

Blanked skeleton (fill the `____`):

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

**Blanks:** `u` (Normalize vector u); `w` (Calculate vector w that is orthogonal to u); `u` (fill in)

→ twin `pseudocode/W1D4_Tutorial1_Pseudocode_590fa120.md` · answer `solutions/W1D4_Tutorial1_Solution_590fa120.py`

---

## Exercise 1.2 — `change_of_basis`

Blanked skeleton (fill the `____`):

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

**Blanks:** `Y` (Project data onto new basis described by W); `Y` (Project data to new basis)

→ twin `pseudocode/W1D4_Tutorial1_Pseudocode_80a5f41b.md` · answer `solutions/W1D4_Tutorial1_Solution_80a5f41b.py`

---

## Exercise 1.3 — `calculate_cov_matrix`

Blanked skeleton (fill the `____`):

```text
def calculate_cov_matrix(var_1, var_2, corr_coef):
  """
  Calculates the covariance matrix based on the variances and correlation
  coefficient.

  Args:
    var_1 (scalar)          : variance of the first random variable
    var_2 (scalar)          : variance of the second random variable
    corr_coef (scalar)      : correlation coefficient

  Returns:
    (numpy array of floats) : covariance matrix
  """

  # Calculate the covariance from the variances and correlation
  cov = ____

  cov_matrix = np.array([[var_1, cov], [cov, var_2]])

  return cov_matrix


# Set parameters
np.random.seed(2020)  # set random seed
variance_1 = 1
variance_2 = 1
corr_coef = 0.8

# Compute covariance matrix
cov_matrix = calculate_cov_matrix(variance_1, variance_2, corr_coef)

# Generate data with this covariance matrix
X = get_data(cov_matrix)

# Visualize
with plt.xkcd():
  plot_data(X)
```

**Blanks:** `cov` (Calculate the covariance from the variances and correlation)

→ twin `pseudocode/W1D4_Tutorial1_Pseudocode_85104841.md` · answer `solutions/W1D4_Tutorial1_Solution_85104841.py`

---
