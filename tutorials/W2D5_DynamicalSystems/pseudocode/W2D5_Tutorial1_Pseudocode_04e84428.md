# Pseudocode twin — W2D5 Tutorial 1: `F`

- **Answer twin:** `../solutions/W2D5_Tutorial1_Solution_04e84428.py`
- **Reading view:** `../W2D5_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def F(x, a, theta):
  """
  Population activation function.

  Args:
    x (float): the population input
    a (float): the gain of the function
    theta (float): the threshold of the function

  Returns:
    float: the population activation response F(x) for input x
  """

  # Define the sigmoidal transfer function f = F(x)
  f = ____

  return f


# Set parameters
pars = default_pars_single()  # get default parameters
x = np.arange(0, 10, .1)      # set the range of input

# Compute transfer function
f = ____

# Visualize
with plt.xkcd():
  plot_fI(x, f)
```

Blanks:
1. `f` — Define the sigmoidal transfer function f = F(x)
2. `f` — Compute transfer function
