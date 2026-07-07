# W3D3 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 1.1 — `simulate_SPRT_threshold`

Blanked skeleton (fill the `____`):

```text
def simulate_SPRT_threshold(mu, sigma, threshold , true_dist=1):
  """Simulate a Sequential Probability Ratio Test with thresholding stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    mu (float): absolute mean value of the symmetric observation distributions
    sigma (float): Standard deviation
    threshold (float): Desired log likelihood ratio threshold to achieve
                        before making decision

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for pR, 0 for pL
    data (numpy vector): the generated sequences of data in this trial
  """
  assert mu > 0, "Mu should be > 0"
  muL = -mu
  muR = mu

  pL = stats.norm(muL, sigma)
  pR = stats.norm(muR, sigma)

  has_enough_data = False

  data_history = []
  evidence_history = []
  current_evidence = 0.0

  # Keep sampling data until threshold is crossed
  while not has_enough_data:
    if true_dist == 1:
      Mvec = pR.rvs()
    else:
      Mvec = pL.rvs()

    # STEP 1: individual log likelihood ratios
    ll_ratio = log_likelihood_ratio(Mvec, pL, pR)

    # STEP 2: accumulated evidence for this chunk
    evidence_history.append(____)

    # update the collection of all data
    data_history.append(Mvec)
    current_evidence = evidence_history[-1]

    # check if we've got enough data
    if abs(current_evidence) > threshold:
      has_enough_data = True

  data_history = np.array(data_history)
  evidence_history = np.array(evidence_history)

  # Make decision
  if evidence_history[-1] >= 0:
    decision = 1
  elif evidence_history[-1] < 0:
    decision = 0

  return evidence_history, decision, data_history


# Set parameters
np.random.seed(100)
mu = 1.0
sigma = 2.8
num_sample = 10
log10_alpha = -3 # log10(alpha)
alpha = np.power(10.0, log10_alpha)

# Simulate and visualize
with plt.xkcd():
  simulate_and_plot_SPRT_fixedthreshold(mu, sigma, num_sample, alpha)
```

**Blanks:** `evidence_history.append(...)` (STEP 2: accumulated evidence for this chunk)

→ twin `pseudocode/W3D3_Tutorial1_Pseudocode_3559a6a0.md` · answer `solutions/W3D3_Tutorial1_Solution_3559a6a0.py`

---

## Exercise 1.2 — `simulate_accuracy_vs_stoptime`

Blanked skeleton (fill the `____`):

```text
def simulate_accuracy_vs_stoptime(mu, sigma, stop_time_list, num_sample,
                                  no_numerical=False):
  """Calculate the average decision accuracy vs. stopping time by running
  repeated SPRT simulations for each stop time.

  Args:
      mu (float): absolute mean value of the symmetric observation distributions
      sigma (float): standard deviation for observation model
      stop_list_list (list-like object): a list of stopping times to run over
      num_sample (int): number of simulations to run per stopping time
      no_numerical (bool): flag that indicates the function to return analytical values only

  Returns:
      accuracy_list: a list of average accuracies corresponding to input
                      `stop_time_list`
      decisions_list: a list of decisions made in all trials
  """

  # Determine true state (1 or -1)
  true_dist = 1

  # Set up tracker of accuracy and decisions
  accuracies = np.zeros(len(stop_time_list),)
  accuracies_analytical = np.zeros(len(stop_time_list),)
  decisions_list = []

  # Loop over stop times
  for i_stop_time, stop_time in enumerate(stop_time_list):

    if not no_numerical:
      # Set up tracker of decisions for this stop time
      decisions = np.zeros((num_sample,))

      # Loop over samples
      for i in range(num_sample):

        # STEP 1: Simulate run for this stop time (hint: use output from last exercise)
        _, decision, _= simulate_SPRT_fixedtime(mu, sigma, stop_time, true_dist)

        # Log decision
        decisions[i] = decision

      # STEP 2: Calculate accuracy by averaging over trials
      accuracies[i_stop_time] = ____

      # Store the decisions
      decisions_list.append(decisions)

    # Calculate analytical accuracy
    # S_t is a normal variable with SNR scale as sqrt(stop_time)
    sigma_sum_gaussian = sigma / np.sqrt(stop_time)
    accuracies_analytical[i_stop_time] = 0.5 + 0.5 * erf(mu / np.sqrt(2) / sigma_sum_gaussian)

  return accuracies, accuracies_analytical, decisions_list


# Set random seed
np.random.seed(100)

# Set parameters of model
mu = 0.5
sigma = 4.65  # standard deviation for observation noise
num_sample = 100  # number of simulations to run for each stopping time
stop_time_list = np.arange(1, 150, 10) # Array of stopping times to use

# Calculate accuracies for each stop time
accuracies, accuracies_analytical, _ = simulate_accuracy_vs_stoptime(mu, sigma, stop_time_list,
                                                   num_sample)

# Visualize
with plt.xkcd():
  plot_accuracy_vs_stoptime(mu, sigma, stop_time_list, accuracies_analytical, accuracies)
```

**Blanks:** `accuracies[i_stop_time]` (STEP 2: Calculate accuracy by averaging over trials)

→ twin `pseudocode/W3D3_Tutorial1_Pseudocode_59bd207a.md` · answer `solutions/W3D3_Tutorial1_Solution_59bd207a.py`

---

## Exercise 1.3 — `simulate_accuracy_vs_threshold`

Blanked skeleton (fill the `____`):

```text
def simulate_accuracy_vs_threshold(mu, sigma, threshold_list, num_sample):
  """Calculate the average decision accuracy vs. average decision speed by
  running repeated SPRT simulations with thresholding stopping rule for each
  threshold.

  Args:
      mu (float): absolute mean value of the symmetric observation distributions
      sigma (float): standard deviation for observation model
      threshold_list (list-like object): a list of evidence thresholds to run
                                          over
      num_sample (int): number of simulations to run per stopping time

  Returns:
      accuracy_list: a list of average accuracies corresponding to input
                      `threshold_list`
      decision_speed_list: a list of average decision speeds
  """
  decision_speed_list = []
  accuracy_list = []
  for threshold in threshold_list:
    decision_time_list = []
    decision_list = []
    for i in range(num_sample):
      # run simulation and get decision of current simulation
      _, decision, Mvec = simulate_SPRT_threshold(mu, sigma, threshold)
      decision_time = len(Mvec)
      decision_list.append(decision)
      decision_time_list.append(decision_time)

    # Calculate and store average decision speed and accuracy
    decision_speed = ____
    decision_accuracy = ____
    decision_speed_list.append(decision_speed)
    accuracy_list.append(decision_accuracy)

  return accuracy_list, decision_speed_list


# Set parameters
np.random.seed(100)
mu = 1.0
sigma = 3.75
num_sample = 200
alpha_list = np.logspace(-2, -0.1, 8)
threshold_list = threshold_from_errorrate(alpha_list)

# Simulate and visualize
with plt.xkcd():
  simulate_and_plot_accuracy_vs_threshold(mu, sigma, threshold_list, num_sample)
```

**Blanks:** `decision_speed` (Calculate and store average decision speed and accuracy); `decision_accuracy` (fill in)

→ twin `pseudocode/W3D3_Tutorial1_Pseudocode_87825db1.md` · answer `solutions/W3D3_Tutorial1_Solution_87825db1.py`

---

## Exercise 1.4 — `simulate_SPRT_fixedtime`

Blanked skeleton (fill the `____`):

```text
def simulate_SPRT_fixedtime(mu, sigma, stop_time, true_dist = 1):
  """Simulate a Sequential Probability Ratio Test with fixed time stopping
  rule. Two observation models are 1D Gaussian distributions N(1,sigma^2) and
  N(-1,sigma^2).

  Args:
    mu (float): absolute mean value of the symmetric observation distributions
    sigma (float): Standard deviation of observation models
    stop_time (int): Number of samples to take before stopping
    true_dist (1 or -1): Which state is the true state.

  Returns:
    evidence_history (numpy vector): the history of cumulated evidence given
                                      generated data
    decision (int): 1 for s = 1, -1 for s = -1
    Mvec (numpy vector): the generated sequences of measurement data in this trial
  """

  # Set means of observation distributions
  assert mu > 0, "Mu should be > 0"
  mu_pos = mu
  mu_neg = -mu

  # Make observation distributions
  p_pos = stats.norm(loc = mu_pos, scale = sigma)
  p_neg = stats.norm(loc = mu_neg, scale = sigma)

  # Generate a random sequence of measurements
  if true_dist == 1:
    Mvec = p_pos.rvs(size = stop_time)
  else:
    Mvec = p_neg.rvs(size = stop_time)

  # Calculate log likelihood ratio for each measurement (delta_t)
  ll_ratio_vec = log_likelihood_ratio(Mvec, p_neg, p_pos)

  # STEP 1: Calculate accumulated evidence (S) given a time series of evidence (hint: np.cumsum)
  evidence_history = ____

  # STEP 2: Make decision based on the sign of the evidence at the final time.
  decision = ____

  return evidence_history, decision, Mvec


# Set random seed
np.random.seed(100)

# Set model parameters
mu = .2
sigma = 3.5  # standard deviation for p+ and p-
num_sample = 10  # number of simulations to run
stop_time = 150 # number of steps before stopping

# Simulate and visualize
with plt.xkcd():
  simulate_and_plot_SPRT_fixedtime(mu, sigma, stop_time, num_sample)
```

**Blanks:** `evidence_history` (STEP 1: Calculate accumulated evidence (S) given a time series of evidence (hint: np.cumsum)); `decision` (STEP 2: Make decision based on the sign of the evidence at the final time.)

→ twin `pseudocode/W3D3_Tutorial1_Pseudocode_985833af.md` · answer `solutions/W3D3_Tutorial1_Solution_985833af.py`

---
