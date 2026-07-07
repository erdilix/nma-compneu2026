# Pseudocode twin — W3D2 Tutorial 3: `calculate_posterior_array`

- **Answer twin:** `../solutions/W3D2_Tutorial3_Solution_aa2afc9a.py`
- **Reading view:** `../W3D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def calculate_posterior_array(prior_array, likelihood_array):

  posterior_array = ____
  posterior_array /= posterior_array.sum(axis=1, keepdims=True)  # normalize each row separately

  return posterior_array


posterior_array = ____
with plt.xkcd():
  plot_myarray(posterior_array,
               'Hypothesized Position $x$',
               'Brain encoded Stimulus $\~x$',
               'Posterior as a fcn of $\~x$ : $p(x | \~x)$')
```

Blanks:
1. `posterior_array` — fill in
2. `posterior_array` — fill in
