# W3D3 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 3.1 — `compare`

Blanked skeleton (fill the `____`):

```text
def compare(s, m):
  """ Compute a scatter plot

  Args:
    s (ndarray): astrocat's true position over time
    m (ndarray): astrocat's measured position over time according to the sensor

  """
  fig = plt.figure()
  ax = fig.add_subplot(111)
  sbounds = 1.1*max(max(np.abs(s)), max(np.abs(m)))
  ax.plot([-sbounds, sbounds], [-sbounds, sbounds], 'k')    # plot line of equality
  ax.set_xlabel('state')
  ax.set_ylabel('measurement')
  ax.set_aspect('equal')

  # Complete a scatter plot: true state versus measurements
  plt.scatter(s, m, marker='.', color='red', s=100)
  plt.show()


# Set parameters
np.random.seed(0)
D = 0.9  # parameter in s(t)
T = 50  # total time duration
s0 = 5.  # initial condition of s at time 0
sigma_p = 2 # amount of noise in the actuators of astrocat's propulsion unit
sigma_measurements = 4 # amount of noise in astrocat's collar

# Simulate Astrocat
s = simulate(D, s0, sigma_p, T)

# Take measurement from collar
m = read_collar(s, sigma_measurements)

# Visualize true vs measured states
with plt.xkcd():
  compare(s, m)
```

→ twin `pseudocode/W3D3_Tutorial3_Pseudocode_34768073.md` · answer `solutions/W3D3_Tutorial3_Solution_34768073.py`

---

## Exercise 3.2 — `simulate`

Blanked skeleton (fill the `____`):

```text
def simulate(D, s0, sigma_p, T):
  """ Compute the response of the linear dynamical system.

  Args:
    D (scalar): dynamics multiplier
    s0 (scalar): initial position
    sigma_p (scalar): amount of noise in the system (standard deviation)
    T (scalar): total duration of the simulation

  Returns:
    ndarray: `s`: astrocat's trajectory up to time T
  """

  # Initialize variables
  s = np.zeros(T+1)
  s[0] = s0

  # Compute the position at time t given the position at time t-1 for all t
  # Consider that np.random.normal(mu, sigma) generates a random sample from
  # a gaussian with mean = mu and standard deviation = sigma

  for t in range(1, len(s)):

    # Update position
    s[t] = ____

  return s


# Set random seed
np.random.seed(0)

# Set parameters
D = 0.9  # parameter in s(t)
T = 50  # total time duration
s0 = 5.  # initial condition of s at time 0
sigma_p = 2 # amount of noise in the actuators of astrocat's propulsion unit

# Simulate Astrocat
s = simulate(D, s0, sigma_p, T)

# Visualize
with plt.xkcd():
  visualize_Astrocat(s, T)
```

**Blanks:** `s[t]` (Update position)

→ twin `pseudocode/W3D3_Tutorial3_Pseudocode_51a25fff.md` · answer `solutions/W3D3_Tutorial3_Solution_51a25fff.py`

---

## Exercise 3.3 — Set random seed

Blanked skeleton (fill the `____`):

```text
# Set random seed
np.random.seed(0)

# Set parameters
T = 50                  # Time duration
tau = 25                # dynamics time constant
process_noise = 2       # process noise in Astrocat's propulsion unit (standard deviation)
measurement_noise = 9   # measurement noise in Astrocat's collar (standard deviation)

# Auxiliary variables
process_noise_cov = process_noise**2          # process noise in Astrocat's propulsion unit (variance)
measurement_noise_cov = measurement_noise**2  # measurement noise in Astrocat's collar (variance)

# Initialize arrays
t = np.arange(0, T, 1)   # timeline
s = np.zeros(T)          # states
D = np.exp(-1/tau)       # dynamics multiplier (matrix if s is vector)

m = np.zeros(T)          # measurement
s_ = np.zeros(T)         # estimate (posterior mean)
cov_ = np.zeros(T)       # uncertainty (posterior covariance)

# Initial guess of the posterior at time 0
initial_guess = gaussian(0, process_noise_cov/(1-D**2))    # In this case, the initial guess (posterior distribution
                                                           # at time 0) is the equilibrium distribution, but feel free to
                                                           # experiment with other gaussians
posterior = initial_guess

# Sample initial conditions
s[0] = posterior.mean + np.sqrt(posterior.cov) * np.random.randn()   # Sample initial condition from posterior distribution at time 0
s_[0] = posterior.mean
cov_[0] = posterior.cov

# Loop over steps
for i in range(1, T):

  # Sample true states and corresponding measurements
  s[i] = D * s[i-1] + np.random.normal(0, process_noise)    # variable `s` records the true position of Astrocat
  m[i] = s[i] + np.random.normal(0, measurement_noise)      # variable `m` records the measurements of Astrocat's collar

  # Step 1. Shift yesterday's posterior to match the deterministic change of the system's dynamics,
  #         and broad it to account for the random change (i.e., add mean and variance of process noise).
  todays_prior = ____

  # Step 2. Now that yesterday's posterior has become today's prior, integrate new evidence
  #         (i.e., multiply gaussians from today's prior and likelihood)
  likelihood = ____

  # Step 2a:  To find the posterior variance, add information (inverse variances) of prior and likelihood
  info_prior = 1/todays_prior.cov
  info_likelihood = 1/likelihood.cov
  info_posterior = ____

  # Step 2b: To find the posterior mean, calculate a weighted average of means from prior and likelihood;
  #          the weights are just the fraction of information that each gaussian provides!
  prior_weight = info_prior / info_posterior
  likelihood_weight = info_likelihood / info_posterior
  posterior_mean = ____

  # Don't forget to convert back posterior information to posterior variance!
  posterior_cov = 1/info_posterior
  posterior = gaussian(posterior_mean, posterior_cov)

  s_[i] = posterior.mean
  cov_[i] = posterior.cov

# Visualize
with plt.xkcd():
  paintMyFilter(D, initial_guess, process_noise_cov, measurement_noise_cov, s, m, s_, cov_)
```

**Blanks:** `todays_prior` (and broad it to account for the random change (i.e., add mean and variance of process noise).); `likelihood` ((i.e., multiply gaussians from today's prior and likelihood)); `info_posterior` (fill in); `posterior_mean` (fill in)

→ twin `pseudocode/W3D3_Tutorial3_Pseudocode_8c82f6d1.md` · answer `solutions/W3D3_Tutorial3_Solution_8c82f6d1.py`

---

## Exercise 3.4 — `read_collar`

Blanked skeleton (fill the `____`):

```text
def read_collar(s, sigma_measurements):
  """ Compute the measurements of the noisy sensor attached to astrocat's collar

  Args:
    s (ndarray): astrocat's true position over time
    sigma_measurements (scalar): amount of noise in the sensor (standard deviation)

  Returns:
    ndarray: `m`: astrocat's position over time according to the sensor
  """

  # Initialize variables
  m = np.zeros(len(s))

  # For all time t, add white Gaussian noise with magnitude sigma_measurements
  # Consider that np.random.normal(mu, sigma) generates a random sample from
  # a gaussian with mean = mu and standard deviation = sigma

  for t in range(len(s)):

    # Read measurement
    m[t] = ____

  return m


# Set parameters
np.random.seed(0)
D = 0.9    # parameter in s(t)
T = 50      # total time duration
s0 = 5.     # initial condition of s at time 0
sigma_p = 2 # amount of noise in the actuators of astrocat's propulsion unit
sigma_measurements = 4 # amount of noise in astrocat's collar

# Simulate Astrocat
s = simulate(D, s0, sigma_p, T)

# Take measurement from collar
m = read_collar(s, sigma_measurements)

# Visualize
with plt.xkcd():
  plot_measurement(s, m, T)
```

**Blanks:** `m[t]` (Read measurement)

→ twin `pseudocode/W3D3_Tutorial3_Pseudocode_95010058.md` · answer `solutions/W3D3_Tutorial3_Solution_95010058.py`

---
