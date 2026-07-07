# Pseudocode twin — W3D2 Tutorial 3: `calculate_prior_array`

- **Answer twin:** `../solutions/W3D2_Tutorial3_Solution_06f6683a.py`
- **Reading view:** `../W3D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def calculate_prior_array(x_points, stim_array, p_indep,
                          prior_mean_common=.0, prior_sigma_common=.5,
                          prior_mean_indep=.0, prior_sigma_indep=10):
  """
      'common' stands for common
      'indep' stands for independent
  """

  prior_common = my_gaussian(x_points, prior_mean_common, prior_sigma_common)
  prior_indep = my_gaussian(x_points, prior_mean_indep, prior_sigma_indep)

  prior_mixed = ____
  prior_mixed /= np.sum(prior_mixed)  # normalize

  prior_array = np.tile(prior_mixed, len(stim_array)).reshape(len(stim_array), -1)
  return prior_array


x = np.arange(-10, 10, 0.1)
p_independent = .05
prior_array = calculate_prior_array(x, hypothetical_stim, p_independent)
with plt.xkcd():
  plot_myarray(prior_array,
               'Hypothesized position $x$', 'Brain encoded position $\~x$',
               'Prior as a fcn of $\~x$ : $p(x|\~x)$')
```

Blanks:
1. `prior_mixed` — fill in
