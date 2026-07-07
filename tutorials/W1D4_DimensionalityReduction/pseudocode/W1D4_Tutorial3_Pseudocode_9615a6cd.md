# Pseudocode twin — W1D4 Tutorial 3: TO DO for students

- **Answer twin:** `../solutions/W1D4_Tutorial3_Solution_9615a6cd.py`
- **Reading view:** `../W1D4_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `X_noisy` — Add noise to data
2. `variance_explained_noisy` — Compute variance explained
