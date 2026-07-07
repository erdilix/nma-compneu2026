# Pseudocode twin — W1D4 Tutorial 4: Comment once you've completed the code

- **Answer twin:** `../solutions/W1D4_Tutorial4_Solution_58cf80ab.py`
- **Reading view:** `../W1D4_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# Take only the first 2000 samples with the corresponding labels
X, labels = X_all[:2000, :], labels_all[:2000]

# Perform PCA
scores = pca_model.transform(X)

# Plot the data and reconstruction
with plt.xkcd():
visualize_components(____)
```

Blanks:
1. `visualize_components(...)` — fill the ____ argument(s)
