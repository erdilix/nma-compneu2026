# Pseudocode twin — W1D4 Tutorial 2: Calculate the eigenvalues and eigenvectors

- **Answer twin:** `../solutions/W1D4_Tutorial2_Solution_97bca56d.py`
- **Reading view:** `../W1D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# Calculate the eigenvalues and eigenvectors
evals, evectors = np.linalg.eigh(cov_matrix)

# Sort the eigenvalues in descending order
evals, evectors = sort_evals_descending(evals, evectors)

# Visualize
with plt.xkcd():
  plot_basis_vectors(X, evectors)
```
