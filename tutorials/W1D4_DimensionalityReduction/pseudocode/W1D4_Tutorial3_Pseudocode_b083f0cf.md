# Pseudocode twin — W1D4 Tutorial 3: TO DO for students

- **Answer twin:** `../solutions/W1D4_Tutorial3_Solution_b083f0cf.py`
- **Reading view:** `../W1D4_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
np.random.seed(2020)  # set random seed

# Add noise to data
X_noisy = ____

# Compute mean of noise-corrupted data
X_noisy_mean = ____

# Project onto the original basis vectors
projX_noisy = ____

# Reconstruct the data using the top 50 components
K = 50
X_reconstructed = ____

# Visualize
with plt.xkcd():
  plot_MNIST_reconstruction(X_noisy, X_reconstructed, K)
```

Blanks:
1. `X_noisy` — Add noise to data
2. `X_noisy_mean` — Compute mean of noise-corrupted data
3. `projX_noisy` — Project onto the original basis vectors
4. `X_reconstructed` — fill in
