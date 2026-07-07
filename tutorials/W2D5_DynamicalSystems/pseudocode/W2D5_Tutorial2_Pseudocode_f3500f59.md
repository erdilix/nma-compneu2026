# Pseudocode twin — W2D5 Tutorial 2: `F_inv`

- **Answer twin:** `../solutions/W2D5_Tutorial2_Solution_f3500f59.py`
- **Reading view:** `../W2D5_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def F_inv(x, a, theta):
  """
  Args:
    x         : the population input
    a         : the gain of the function
    theta     : the threshold of the function

  Returns:
    F_inverse : value of the inverse function
  """

  # Calculate Finverse (ln(x) can be calculated as np.log(x))
  F_inverse = ____

  return F_inverse


# Set parameters
pars = default_pars()
x = np.linspace(1e-6, 1, 100)

# Get inverse and visualize
with plt.xkcd():
  plot_FI_inverse(x, a=1, theta=3)
```

Blanks:
1. `F_inverse` — Calculate Finverse (ln(x) can be calculated as np.log(x))
