# Pseudocode twin — W2D4 Tutorial 2: `my_CC`

- **Answer twin:** `../solutions/W2D4_Tutorial2_Solution_313f41e4.py`
- **Reading view:** `../W2D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def my_CC(i, j):
  """
  Args:
    i, j  : two time series with the same length

  Returns:
    rij   : correlation coefficient
  """

  # Calculate the covariance of i and j
  cov = ____

  # Calculate the variance of i
  var_i = ____

  # Calculate the variance of j
  var_j = ____

  # Calculate the correlation coefficient
  rij = ____

  return rij


with plt.xkcd():
  example_plot_myCC()
```

Blanks:
1. `cov` — Calculate the covariance of i and j
2. `var_i` — Calculate the variance of i
3. `var_j` — Calculate the variance of j
4. `rij` — Calculate the correlation coefficient
