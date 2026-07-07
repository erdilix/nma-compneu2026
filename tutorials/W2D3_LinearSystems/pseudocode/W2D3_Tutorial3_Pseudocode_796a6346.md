# Pseudocode twin — W2D3 Tutorial 3: Simulate random walks

- **Answer twin:** `../solutions/W2D3_Tutorial3_Solution_796a6346.py`
- **Reading view:** `../W2D3_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# Simulate random walks
np.random.seed(2020) # set random seed
sim = random_walk_simulator(5000, 1000, mu=0, sigma=1)

# Compute mean
mu = ____

# Compute variance
var = ____

# Visualize
with plt.xkcd():
  plot_mean_var_by_timestep(mu, var)
```

Blanks:
1. `mu` — Compute mean
2. `var` — Compute variance
