# W3D5 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **5** code exercise(s).

---

## Exercise 4.1 — `simulate_neurons_iv`

Blanked skeleton (fill the `____`):

```text
def simulate_neurons_iv(n_neurons, timesteps, eta, random_state=42):
  """
  Simulates a dynamical system for the specified number of neurons and timesteps.

  Args:
      n_neurons (int): the number of neurons in our system.
      timesteps (int): the number of timesteps to simulate our system.
      eta (float): the strength of the instrument
      random_state (int): seed for reproducibility

  Returns:
      The tuple (A,X,Z) of the connectivity matrix, simulated system, and instruments.
      - A has shape (n_neurons, n_neurons)
      - X has shape (n_neurons, timesteps)
      - Z has shape (n_neurons, timesteps)
  """
  np.random.seed(random_state)
  A = create_connectivity(n_neurons, random_state)

  X = np.zeros((n_neurons, timesteps))
  Z = np.random.choice([0, 1], size=(n_neurons, timesteps))
  for t in range(timesteps - 1):

    IV_on_this_timestep = ____

    X[:, t + 1] = sigmoid(A.dot(X[:, t]) + IV_on_this_timestep + np.random.multivariate_normal(np.zeros(n_neurons), np.eye(n_neurons)))

  return A, X, Z


# Set parameters
timesteps = 5000  # Simulate for 5000 timesteps.
n_neurons = 100  # the size of our system
eta = 2  # the strength of our instrument, higher is stronger

# Simulate our dynamical system for the given amount of time
A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta)

# Visualize
with plt.xkcd():
  plot_neural_activity(X)
```

**Blanks:** `IV_on_this_timestep` (fill in)

→ twin `pseudocode/W3D5_Tutorial4_Pseudocode_21f5cd72.md` · answer `solutions/W3D5_Tutorial4_Solution_21f5cd72.py`

---

## Exercise 4.2 — `get_granger_causality`

Blanked skeleton (fill the `____`):

```text
def get_granger_causality(X, selected_neuron, alpha=0.05):
  """
  Estimates the lag-1 granger causality of the given neuron on the other neurons in the system.

  Args:
      X (np.ndarray): the matrix holding our dynamical system of shape (n_neurons, timesteps)
      selected_neuron (int): the index of the neuron we want to estimate granger causality for
      alpha (float): Bonferroni multiple comparisons correction

  Returns:
      A tuple (reject_null, p_vals)
      reject_null (list): a binary list of length n_neurons whether the null was
          rejected for the selected neuron granger causing the other neurons
      p_vals (list): a list of the p-values for the corresponding Granger causality tests
  """
  n_neurons = X.shape[0]
  max_lag = 1

  reject_null = []
  p_vals = []

  for target_neuron in range(n_neurons):
    ts_data = X[[target_neuron, selected_neuron], :].transpose()

    res = grangercausalitytests(ts_data, maxlag=max_lag, verbose=False)

    # Gets the p-value for the log-ratio test
    pval = res[1][0]['lrtest'][1]

    p_vals.append(pval)
    reject_null.append(int(pval < alpha))

  return reject_null, p_vals


# Set up small system
n_neurons = 6
timesteps = 5000
random_state = 42
selected_neuron = 1

A = create_connectivity(n_neurons, random_state)
X = simulate_neurons(A, timesteps, random_state)

# Estimate Granger causality
reject_null, p_vals = get_granger_causality(X, selected_neuron)

# Visualize
with plt.xkcd():
  compare_granger_connectivity(A, reject_null, selected_neuron)
```

→ twin `pseudocode/W3D5_Tutorial4_Pseudocode_2e17e047.md` · answer `solutions/W3D5_Tutorial4_Solution_2e17e047.py`

---

## Exercise 4.3 — `fit_first_stage`

Blanked skeleton (fill the `____`):

```text
def fit_first_stage(T, Z):
  """
  Estimates T_hat as the first stage of a two-stage least squares.

  Args:
      T (np.ndarray): our observed, possibly confounded, treatment of shape (n, 1)
      Z (np.ndarray): our observed instruments of shape (n, 1)

  Returns
      T_hat (np.ndarray): our estimate of the unconfounded portion of T
  """

  # Initialize linear regression model
  stage1 = LinearRegression(fit_intercept=True)

  # Fit linear regression model
  stage1.fit(____)

  # Predict T_hat using linear regression model
  T_hat = stage1.predict(Z)

  return T_hat


# Estimate T_hat
T_hat = fit_first_stage(T, Z)

# Get correlations
T_C_corr = np.corrcoef(T.transpose(), C.transpose())[0, 1]
T_hat_C_corr = np.corrcoef(T_hat.transpose(), C.transpose())[0, 1]

# Print correlations
print(f"Correlation between T and C: {T_C_corr:.3f}")
print(f"Correlation between T_hat and C: {T_hat_C_corr:.3f}")
```

**Blanks:** `stage1.fit(...)` (Fit linear regression model)

→ twin `pseudocode/W3D5_Tutorial4_Pseudocode_431a3d57.md` · answer `solutions/W3D5_Tutorial4_Solution_431a3d57.py`

---

## Exercise 4.4 — `fit_second_stage`

Blanked skeleton (fill the `____`):

```text
def fit_second_stage(T_hat, Y):
  """
  Estimates a scalar causal effect from 2-stage least squares regression using
  an instrument.

  Args:
      T_hat (np.ndarray): the output of the first stage regression
      Y (np.ndarray): our observed response (n, 1)

  Returns:
      beta (float): the estimated causal effect
  """
  # Initialize linear regression model
  stage2 = LinearRegression(fit_intercept=True)

  # Fit model to data
  stage2.fit(____)

  return stage2.coef_


# Fit first stage
T_hat = fit_first_stage(T, Z)

# Fit second stage
beta = fit_second_stage(T_hat, Y)

# Print
print(f"Estimated causal effect is: {beta[0, 0]:.3f}")
```

**Blanks:** `stage2.fit(...)` (Fit model to data)

→ twin `pseudocode/W3D5_Tutorial4_Pseudocode_778b0511.md` · answer `solutions/W3D5_Tutorial4_Solution_778b0511.py`

---

## Exercise 4.5 — `instrument_strength_effect`

Blanked skeleton (fill the `____`):

```text
def instrument_strength_effect(etas, n_neurons, timesteps, n_trials):
  """ Compute IV estimation performance for different instrument strengths

  Args:
    etas (list): different instrument strengths to compare
    n_neurons (int): number of neurons in simulation
    timesteps (int): number of timesteps in simulation
    n_trials (int): number of trials to compute

  Returns:
    ndarray: n_trials x len(etas) array where each element is the correlation
             between true and estimated connectivity matrices for that trial and
             instrument strength
  """

  # Initialize corr array
  corr_data = np.zeros((n_trials, len(etas)))

  # Loop over trials
  for trial in range(n_trials):
    print(f"simulation of trial {trial + 1} of {n_trials}")

    # Loop over instrument strengths
    for j, eta in enumerate(etas):

      # Simulate system
      A, X, Z = simulate_neurons_iv(n_neurons, timesteps, eta, trial)

      # Compute IV estimate
      iv_V = get_iv_estimate_network(X, Z)

      # Compute correlation
      corr_data[trial, j] =  np.corrcoef(A.flatten(), iv_V.flatten())[1, 0]

  return corr_data


# Parameters of system
n_neurons = 20
timesteps = 10000
n_trials = 3
etas = [2, 1, 0.5, 0.25, 0.12]  # instrument strengths to search over

# Get IV estimate performances
corr_data = instrument_strength_effect(etas, n_neurons, timesteps, n_trials)

# Visualize
with plt.xkcd():
  plot_performance_vs_eta(etas, corr_data)
```

→ twin `pseudocode/W3D5_Tutorial4_Pseudocode_b686d55b.md` · answer `solutions/W3D5_Tutorial4_Solution_b686d55b.py`

---
