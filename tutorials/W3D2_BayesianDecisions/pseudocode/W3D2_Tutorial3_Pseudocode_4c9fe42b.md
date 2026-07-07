# Pseudocode twin — W3D2 Tutorial 3: `compute_likelihood_array`

- **Answer twin:** `../solutions/W3D2_Tutorial3_Solution_4c9fe42b.py`
- **Reading view:** `../W3D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
x = np.arange(-10, 10, 0.1)
hypothetical_stim = np.linspace(-8, 8, 1000)

def compute_likelihood_array(x_points, stim_array, sigma=1.):

  # initializing likelihood_array
  likelihood_array = np.zeros((len(stim_array), len(x_points)))
  # looping over stimulus array
  for i in range(len(stim_array)):
    likelihood_array[i, :] = my_gaussian(x_points, stim_array[i], sigma)

  return likelihood_array


likelihood_array = compute_likelihood_array(x, hypothetical_stim)
with plt.xkcd():
  plot_myarray(likelihood_array,
               '$x$ : Potential true stimulus $x$',
               'Possible brain encoding $\~x$',
               'Likelihood as a function of $\~x$ : $p(\~x | x)$')
```
