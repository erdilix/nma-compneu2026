# Pseudocode twin — W2D3 Tutorial 4: define the model order, and use AR_model() to generate the m

- **Answer twin:** `../solutions/W2D3_Tutorial4_Solution_6439815f.py`
- **Reading view:** `../W2D3_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# define the model order, and use AR_model() to generate the model and prediction
r = ____ # remove later
x1, x2, p = AR_model(x, r)

# Plot the Training data fit
# Note that this adds a small amount of jitter to horizontal axis for visualization purposes
with plt.xkcd():
  plot_training_fit(x1, x2, p)
```

Blanks:
1. `r` — define the model order, and use AR_model() to generate the model and prediction
