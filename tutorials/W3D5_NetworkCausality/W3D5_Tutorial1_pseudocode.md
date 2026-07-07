# W3D5 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 1.1 — `simulate_neurons`

Blanked skeleton (fill the `____`):

```text
def simulate_neurons(A, timesteps, random_state=42):
  """Simulates a dynamical system for the specified number of neurons and timesteps.

  Args:
    A (np.array): the connectivity matrix
    timesteps (int): the number of timesteps to simulate our system.
    random_state (int): random seed for reproducibility

  Returns:
    - X has shape (n_neurons, timeteps). A schematic:
                ___t____t+1___
    neuron  0  |   0    1     |
              |   1    0     |
    neuron  i  |   0 -> 1     |
              |   0    0     |
              |___1____0_____|
  """
  np.random.seed(random_state)

  n_neurons = len(A)
  X = np.zeros((n_neurons, timesteps))

  for t in range(timesteps - 1):

    # Create noise vector
    epsilon = np.random.multivariate_normal(np.zeros(n_neurons), np.eye(n_neurons))

    # Update activity vector for next step
    X[:, t + 1] = sigmoid(A @ X[:, t] + epsilon)  # we are using helper function sigmoid

  return X


# Set simulation length
timesteps = 5000

# Simulate our dynamical system
X = simulate_neurons(A, timesteps)

# Visualize
with plt.xkcd():
  plot_neural_activity(X)
```

→ twin `pseudocode/W3D5_Tutorial1_Pseudocode_4eb489b5.md` · answer `solutions/W3D5_Tutorial1_Solution_4eb489b5.py`

---

## Exercise 1.2 — `neuron_B`

Blanked skeleton (fill the `____`):

```text
def neuron_B(activity_of_A):
  """Model activity of neuron B as neuron A activity + noise

  Args:
    activity_of_A (ndarray): An array of shape (T,) containing the neural activity of neuron A

  Returns:
    ndarray: activity of neuron B
  """
  noise = np.random.randn(activity_of_A.shape[0])
  return activity_of_A + noise

np.random.seed(12)

# Neuron A activity of zeros
A_0 = np.zeros(5000)

# Neuron A activity of ones
A_1 = np.ones(5000)

diff_in_means = ____
print(diff_in_means)
```

**Blanks:** `diff_in_means` (fill in)

→ twin `pseudocode/W3D5_Tutorial1_Pseudocode_9ae3afbe.md` · answer `solutions/W3D5_Tutorial1_Solution_9ae3afbe.py`

---

## Exercise 1.3 — `get_perturbed_connectivity_from_single_neuron`

Blanked skeleton (fill the `____`):

```text
def get_perturbed_connectivity_from_single_neuron(perturbed_X, selected_neuron):
  """
  Computes the connectivity matrix from the selected neuron using differences in means.

  Args:
    perturbed_X (np.ndarray): the perturbed dynamical system matrix of shape
                              (n_neurons, timesteps)
    selected_neuron (int): the index of the neuron we want to estimate connectivity for

  Returns:
      estimated_connectivity (np.ndarray): estimated connectivity for the selected neuron,
                                           of shape (n_neurons,)
  """
  # Extract the perturbations of neuron 1 (every other timestep)
  neuron_perturbations = perturbed_X[selected_neuron, ::2]

  # Extract the observed outcomes of all the neurons (every other timestep)
  all_neuron_output = perturbed_X[:, 1::2]

  # Initialize estimated connectivity matrix
  estimated_connectivity = np.zeros(n_neurons)

  # Loop over neurons
  for neuron_idx in range(n_neurons):

    # Get this output neurons (neuron_idx) activity
    this_neuron_output = all_neuron_output[neuron_idx, :]

    # Get timesteps where the selected neuron == 0 vs == 1
    one_idx = np.argwhere(neuron_perturbations == 1)
    zero_idx = np.argwhere(neuron_perturbations == 0)

    difference_in_means = ____

    estimated_connectivity[neuron_idx] = difference_in_means

  return estimated_connectivity


# Initialize the system
n_neurons = 6
timesteps = 5000
selected_neuron = 1

# Simulate our perturbed dynamical system
perturbed_X = simulate_neurons_perturb(A, timesteps)

# Measure connectivity of neuron 1
estimated_connectivity = get_perturbed_connectivity_from_single_neuron(perturbed_X, selected_neuron)
with plt.xkcd():
  plot_true_vs_estimated_connectivity(estimated_connectivity, A, selected_neuron)
```

**Blanks:** `difference_in_means` (fill in)

→ twin `pseudocode/W3D5_Tutorial1_Pseudocode_fb7d91ed.md` · answer `solutions/W3D5_Tutorial1_Solution_fb7d91ed.py`

---
