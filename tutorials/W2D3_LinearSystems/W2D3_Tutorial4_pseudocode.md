# W2D3 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 4.1 — Insert your code here take to compute the residual (error)

Blanked skeleton (fill the `____`):

```text
# compute the predicted values using the autoregressive model (lam_hat), and
# the residual is the difference between x2 and the prediction
res = ____

# Visualize
with plt.xkcd():
  plot_residual_histogram(res)
```

**Blanks:** `res` (the residual is the difference between x2 and the prediction)

→ twin `pseudocode/W2D3_Tutorial4_Pseudocode_4d89c578.md` · answer `solutions/W2D3_Tutorial4_Solution_4d89c578.py`

---

## Exercise 4.2 — define the model order, and use AR_model() to generate the m

Blanked skeleton (fill the `____`):

```text
# define the model order, and use AR_model() to generate the model and prediction
r = ____ # remove later
x1, x2, p = AR_model(x, r)

# Plot the Training data fit
# Note that this adds a small amount of jitter to horizontal axis for visualization purposes
with plt.xkcd():
  plot_training_fit(x1, x2, p)
```

**Blanks:** `r` (define the model order, and use AR_model() to generate the model and prediction)

→ twin `pseudocode/W2D3_Tutorial4_Pseudocode_6439815f.md` · answer `solutions/W2D3_Tutorial4_Solution_6439815f.py`

---
