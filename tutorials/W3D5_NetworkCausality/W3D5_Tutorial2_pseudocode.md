# W3D5 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 2.1 — `get_coarse_corr`

Blanked skeleton (fill the `____`):

```text
def get_coarse_corr(n_groups, X):
  """
  A wrapper function for our correlation calculations between coarsely sampled
  A and R.

  Args:
    n_groups (int): the number of groups. should divide the number of neurons evenly
    X: the simulated system

  Returns:
    A single float correlation value representing the similarity between A and R
    ndarray: estimated connectivity matrix
    ndarray: true connectivity matrix
  """

  coarse_X = ____

  # Make sure coarse_X is the right shape
  assert coarse_X.shape == (n_groups, timesteps)

  # Estimate connectivity from coarse system
  R = correlation_for_all_neurons(coarse_X)

  # Compute true coarse connectivity
  coarse_A = A.reshape(n_groups, n_neurons // n_groups, n_groups, n_neurons // n_groups).mean(3).mean(1)

  # Compute true vs estimated connectivity correlation
  corr = np.corrcoef(coarse_A.flatten(), R.flatten())[0, 1]

  return corr, R, coarse_A


n_groups = 16

# Call function
corr, R, coarse_A = get_coarse_corr(n_groups, X)

# Visualize
with plt.xkcd():
  plot_true_vs_estimated_connectivity(R, coarse_A, correlation=corr)
```

**Blanks:** `coarse_X` (fill in)

→ twin `pseudocode/W3D5_Tutorial2_Pseudocode_12df1439.md` · answer `solutions/W3D5_Tutorial2_Solution_12df1439.py`

---

## Exercise 2.2 — `compute_connectivity_from_single_neuron`

Blanked skeleton (fill the `____`):

```text
def compute_connectivity_from_single_neuron(X, selected_neuron):
  """
  Computes the connectivity matrix from a single neuron neurons using correlations

  Args:
      X (ndarray): the matrix of activities
      selected_neuron (int): the index of the selected neuron

  Returns:
      estimated_connectivity (ndarray): estimated connectivity for the selected neuron, of shape (n_neurons,)
  """

  # Extract the current activity of selected_neuron, t
  current_activity = X[selected_neuron, :-1]

  # Extract the observed outcomes of all the neurons
  next_activity = X[:, 1:]

  # Initialize estimated connectivity matrix
  estimated_connectivity = np.zeros(n_neurons)

  # Loop through all neurons
  for neuron_idx in range(n_neurons):

    # Get the activity of neuron_idx
    this_output_activity = next_activity[neuron_idx]

    # Compute correlation
    correlation = np.corrcoef(this_output_activity, current_activity)[0, 1]

    # Store this neuron's correlation
    estimated_connectivity[neuron_idx] = correlation

  return estimated_connectivity


# Simulate a 6 neuron system for 5000 timesteps again.
n_neurons = 6
timesteps = 5000
selected_neuron = 1

# Invoke a helper function that generates our nxn causal connectivity matrix
A = create_connectivity(n_neurons)

# Invoke a helper function that simulates the neural activity
X = simulate_neurons(A, timesteps)

# Estimate connectivity
estimated_connectivity = compute_connectivity_from_single_neuron(X, selected_neuron)

# Visualize
with plt.xkcd():
  plot_true_vs_estimated_connectivity(estimated_connectivity, A, selected_neuron)
```

→ twin `pseudocode/W3D5_Tutorial2_Pseudocode_3d6bc00e.md` · answer `solutions/W3D5_Tutorial2_Solution_3d6bc00e.py`

---
