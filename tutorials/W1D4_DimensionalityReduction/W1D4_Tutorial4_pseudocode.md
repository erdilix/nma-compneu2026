# W1D4 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 4.1 — `explore_perplexity`

Blanked skeleton (fill the `____`):

```text
def explore_perplexity(values, X, labels):
  """
  Plots a 2D representation of the data for visualization with categories
  labeled as different colors using different perplexities.

  Args:
    values (list of floats) : list with perplexities to be visualized
    X (np.ndarray of floats) : matrix with the dataset
    labels (np.ndarray of int) : array with the labels

  Returns:
    Nothing.

  """

  for perp in values:

    # Perform t-SNE
    tsne_model = ____

    embed = tsne_model.fit_transform(X)
    visualize_components(embed[:, 0], embed[:, 1], labels, show=False)
    plt.title(f"perplexity: {perp}")
    plt.show()


# Visualize
values = [50, 5, 2]
with plt.xkcd():
  explore_perplexity(values, X, labels)
```

**Blanks:** `tsne_model` (Perform t-SNE)

→ twin `pseudocode/W1D4_Tutorial4_Pseudocode_2e8ff78c.md` · answer `solutions/W1D4_Tutorial4_Solution_2e8ff78c.py`

---

## Exercise 4.2 — Comment once you've completed the code

Blanked skeleton (fill the `____`):

```text
# Perform t-SNE
embed = ____

# Visualize the data
with plt.xkcd():
visualize_components(____, ____, labels)
```

**Blanks:** `embed` (Perform t-SNE); `visualize_components(...)` (fill the ____ argument(s))

→ twin `pseudocode/W1D4_Tutorial4_Pseudocode_4e6f6604.md` · answer `solutions/W1D4_Tutorial4_Solution_4e6f6604.py`

---

## Exercise 4.3 — Comment once you've completed the code

Blanked skeleton (fill the `____`):

```text
# Take only the first 2000 samples with the corresponding labels
X, labels = X_all[:2000, :], labels_all[:2000]

# Perform PCA
scores = pca_model.transform(X)

# Plot the data and reconstruction
with plt.xkcd():
visualize_components(____)
```

**Blanks:** `visualize_components(...)` (fill the ____ argument(s))

→ twin `pseudocode/W1D4_Tutorial4_Pseudocode_58cf80ab.md` · answer `solutions/W1D4_Tutorial4_Solution_58cf80ab.py`

---
