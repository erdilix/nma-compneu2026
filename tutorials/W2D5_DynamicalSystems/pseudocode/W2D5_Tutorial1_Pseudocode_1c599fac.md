# Pseudocode twin — W2D5 Tutorial 1: Set parameters

- **Answer twin:** `../solutions/W2D5_Tutorial1_Solution_1c599fac.py`
- **Reading view:** `../W2D5_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# Set parameters
r = np.linspace(0, 1, 1000)
pars = default_pars_single(I_ext=0.5, w=5)

# Compute dr/dt
drdt = compute_drdt(r, **pars)

# Initial guesses for fixed points
r_guess_vector = [0, .4, .9]

# Find fixed point numerically
x_fps = my_fp_finder(pars, r_guess_vector)

# Visualize
with plt.xkcd():
  plot_dr_r(r, drdt, x_fps)
```
