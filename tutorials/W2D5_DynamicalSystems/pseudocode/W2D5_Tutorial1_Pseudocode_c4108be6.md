# Pseudocode twin — W2D5 Tutorial 1: `compute_drdt`

- **Answer twin:** `../solutions/W2D5_Tutorial1_Solution_c4108be6.py`
- **Reading view:** `../W2D5_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def compute_drdt(r, I_ext, w, a, theta, tau, **other_pars):
  """Given parameters, compute dr/dt as a function of r.

  Args:
    r (1D array) : Average firing rate of the excitatory population
    I_ext, w, a, theta, tau (numbers): Simulation parameters to use
    other_pars : Other simulation parameters are unused by this function

  Returns
    drdt function for each value of r
  """
  # Calculate drdt
  drdt = ____

  return drdt


# Define a vector of r values and the simulation parameters
r = np.linspace(0, 1, 1000)
pars = default_pars_single(I_ext=0.5, w=5)

# Compute dr/dt
drdt = ____

# Visualize
with plt.xkcd():
  plot_dr_r(r, drdt)
```

Blanks:
1. `drdt` — Calculate drdt
2. `drdt` — Compute dr/dt
