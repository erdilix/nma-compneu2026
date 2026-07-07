# Pseudocode twin — W2D5 Tutorial 2: Note: aE, thetaE, aI and theta_I are in the dictionary 'pair

- **Answer twin:** `../solutions/W2D5_Tutorial2_Solution_043dd600.py`
- **Reading view:** `../W2D5_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
pars = default_pars()
x = np.arange(0, 10, .1)

print(pars['a_E'], pars['theta_E'])
print(pars['a_I'], pars['theta_I'])

# Compute the F-I curve of the excitatory population
FI_exc = ____

# Compute the F-I curve of the inhibitory population
FI_inh = ____

# Visualize
with plt.xkcd():
  plot_FI_EI(x, FI_exc, FI_inh)
```

Blanks:
1. `FI_exc` — Compute the F-I curve of the excitatory population
2. `FI_inh` — Compute the F-I curve of the inhibitory population
