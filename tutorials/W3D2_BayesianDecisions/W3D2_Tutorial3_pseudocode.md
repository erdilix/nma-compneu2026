# W3D2 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **7** code exercise(s).

---

## Exercise 3.1 — `calculate_prior_array`

Blanked skeleton (fill the `____`):

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

**Blanks:** `prior_mixed` (fill in)

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_06f6683a.md` · answer `solutions/W3D2_Tutorial3_Solution_06f6683a.py`

---

## Exercise 3.2 — `my_marginalization`

Blanked skeleton (fill the `____`):

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

**Blanks:** `marginalization_array` (fill in); `marginal` (note axis)

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_2d90e38d.md` · answer `solutions/W3D2_Tutorial3_Solution_2d90e38d.py`

---

## Exercise 3.3 — `compute_likelihood_array`

Blanked skeleton (fill the `____`):

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

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_4c9fe42b.md` · answer `solutions/W3D2_Tutorial3_Solution_4c9fe42b.py`

---

## Exercise 3.4 — `my_Bayes_model_mse`

Blanked skeleton (fill the `____`):

```text
def my_Bayes_model_mse(params):
  """
  Function fits the Bayesian model from Tutorial 4

  Args :
      params (list of positive floats):  parameters used by the model
      (params[0]  = posterior scaling)

  Returns :
      (scalar) negative log-likelihood :sum of log probabilities
  """
  # Create the prior array
  p_independent=params[0]
  prior_array = calculate_prior_array(x,
                                      hypothetical_stim,
                                      p_independent,
                                      prior_sigma_indep= 3.)

  # Create posterior array
  posterior_array = calculate_posterior_array(prior_array, likelihood_array)
  # Create Binary decision array
  binary_decision_array = calculate_binary_decision_array(x, posterior_array)
  # we will use trial_ll (trial log likelihood) to register each trial
  trial_ll = np.zeros_like(true_stim)

  # Loop over stimuli
  for i_stim in range(len(true_stim)):
    # create the input array with true_stim as mean
    input_array = np.zeros_like(posterior_array)
    for i in range(len(x)):
      input_array[:, i] = my_gaussian(hypothetical_stim, true_stim[i_stim], 1)
      input_array[:, i] = input_array[:, i] / np.sum(input_array[:, i])

    # calculate the marginalizations
    marginalization_array, marginal = my_marginalization(input_array,
                                                         binary_decision_array)
    action = behaviour[i_stim]
    idx = np.argmin(np.abs(x - action))
    # Get the marginal likelihood corresponding to the action
    marginal_nonzero = ____  # avoid log(0)
    trial_ll[i_stim] = np.log(marginal_nonzero)

  neg_ll = -trial_ll.sum()

  return neg_ll


with plt.xkcd():
  plot_my_bayes_model(my_Bayes_model_mse)
```

**Blanks:** `marginal_nonzero` (Get the marginal likelihood corresponding to the action)

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_87fb5dcf.md` · answer `solutions/W3D2_Tutorial3_Solution_87fb5dcf.py`

---

## Exercise 3.5 — `calculate_posterior_array`

Blanked skeleton (fill the `____`):

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

**Blanks:** `posterior_array` (fill in); `posterior_array` (fill in)

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_aa2afc9a.md` · answer `solutions/W3D2_Tutorial3_Solution_aa2afc9a.py`

---

## Exercise 3.6 — `generate_input_array`

Blanked skeleton (fill the `____`):

```text
def generate_input_array(x_points, stim_array, posterior_array,
                         mean=2.5, sigma=1.):

  input_array = np.zeros_like(posterior_array)
  for i in range(len(x_points)):
    input_array[:, i] = my_gaussian(stim_array, mean, sigma)

  return input_array


input_array = generate_input_array(x, hypothetical_stim, posterior_array)
with plt.xkcd():
  plot_myarray(input_array,
               'Hypothetical Stimulus $x$', '$\~x$',
               'Sample Distribution over Encodings:\n $p(\~x | x = 2.5)$')
```

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_e37eb6db.md` · answer `solutions/W3D2_Tutorial3_Solution_e37eb6db.py`

---

## Exercise 3.7 — `calculate_binary_decision_array`

Blanked skeleton (fill the `____`):

```text
def calculate_binary_decision_array(x_points, posterior_array):

  binary_decision_array = np.zeros_like(posterior_array)

  for i in range(len(posterior_array)):
    # calculate mean of posterior using 'moments_myfunc'
    mean, _, _ = moments_myfunc(x_points, posterior_array[i])
    # find the position of mean in x_points (closest position)
    idx = ____
    binary_decision_array[i, idx] = 1

  return binary_decision_array


binary_decision_array = calculate_binary_decision_array(x, posterior_array)
with plt.xkcd():
  plot_myarray(binary_decision_array,
               'Chosen position $\hat x$', 'Brain-encoded Stimulus $\~ x$',
               'Sample Binary Decision Array')
```

**Blanks:** `idx` (find the position of mean in x_points (closest position))

→ twin `pseudocode/W3D2_Tutorial3_Pseudocode_fc2e7c22.md` · answer `solutions/W3D2_Tutorial3_Solution_fc2e7c22.py`

---
