# Pseudocode twin — W1D4 Tutorial 4: `explore_perplexity`

- **Answer twin:** `../solutions/W1D4_Tutorial4_Solution_2e8ff78c.py`
- **Reading view:** `../W1D4_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `tsne_model` — Perform t-SNE
