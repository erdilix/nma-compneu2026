# W3D2 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **1** code exercise(s).

---

## Exercise 1.1 — `compute_posterior`

Blanked skeleton (fill the `____`):

```text
def compute_posterior(likelihood, prior):
  """ Use Bayes' Rule to compute posterior from likelihood and prior

  Args:
    likelihood (ndarray): i x j array with likelihood probabilities where i is
                    number of state options, j is number of measurement options
    prior (ndarray): i x 1 array with prior probability of each state

  Returns:
    ndarray: i x j array with posterior probabilities where i is
            number of state options, j is number of measurement options

  """

  # Compute unnormalized posterior (likelihood times prior)
  posterior = ____ # first row is s = left, second row is s = right

  # Compute p(m)
  p_m = np.sum(posterior, axis = 0)

  # Normalize posterior (divide elements by p_m)
  posterior /= p_m

  return posterior


# Make prior
prior = np.array([0.3, 0.7]).reshape((2, 1)) # first row is s = left, second row is s = right

# Make likelihood
likelihood = np.array([[0.5, 0.5], [0.1, 0.9]]) # first row is s = left, second row is s = right

# Compute posterior
posterior = ____

# Visualize
with plt.xkcd():
  plot_prior_likelihood_posterior(prior, likelihood, posterior)
```

**Blanks:** `posterior` (Compute unnormalized posterior (likelihood times prior)); `posterior` (Compute posterior)

→ twin `pseudocode/W3D2_Tutorial1_Pseudocode_1a2cc907.md` · answer `solutions/W3D2_Tutorial1_Solution_1a2cc907.py`

---
