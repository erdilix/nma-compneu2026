# Pseudocode twin — W2D5 Tutorial 2: `EIderivs`

- **Answer twin:** `../solutions/W2D5_Tutorial2_Solution_92ba9d03.py`
- **Reading view:** `../W2D5_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def EIderivs(rE, rI,
             tau_E, a_E, theta_E, wEE, wEI, I_ext_E,
             tau_I, a_I, theta_I, wIE, wII, I_ext_I,
             **other_pars):
  """Time derivatives for E/I variables (dE/dt, dI/dt)."""

  # Compute the derivative of rE
  drEdt = ____

  # Compute the derivative of rI
  drIdt = ____

  return drEdt, drIdt


# Create vector field using EIderivs
with plt.xkcd():
  plot_complete_analysis(default_pars())
```

Blanks:
1. `drEdt` — Compute the derivative of rE
2. `drIdt` — Compute the derivative of rI
