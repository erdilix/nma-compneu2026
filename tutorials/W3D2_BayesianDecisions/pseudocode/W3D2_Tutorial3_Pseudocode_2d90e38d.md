# Pseudocode twin — W3D2 Tutorial 3: `my_marginalization`

- **Answer twin:** `../solutions/W3D2_Tutorial3_Solution_2d90e38d.py`
- **Reading view:** `../W3D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def my_marginalization(input_array, binary_decision_array):

  marginalization_array = ____
  marginal = ____  # note axis
  marginal /= marginal.sum()  # normalize

  return marginalization_array, marginal


marginalization_array, marginal = my_marginalization(input_array, binary_decision_array)
with plt.xkcd():
  plot_myarray(marginalization_array,
               'estimated $\hat x$',
               '$\~x$',
               'Marginalization array: $p(\^x | \~x)$')
  plt.figure()
  plt.plot(x, marginal)
  plt.xlabel('$\^x$')
  plt.ylabel('probability')
  plt.show()
```

Blanks:
1. `marginalization_array` — fill in
2. `marginal` — note axis
