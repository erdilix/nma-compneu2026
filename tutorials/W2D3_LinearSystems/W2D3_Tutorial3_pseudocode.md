# W2D3 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 3.1 — `random_walk_simulator`

Blanked skeleton (fill the `____`):

```text
def random_walk_simulator(N, T, mu=0, sigma=1):
  '''Simulate N random walks for T time points. At each time point, the step
      is drawn from a Gaussian distribution with mean mu and standard deviation
      sigma.

  Args:
    T (integer) : Duration of simulation in time steps
    N (integer) : Number of random walks
    mu (float) : mean of step distribution
    sigma (float) : standard deviation of step distribution

  Returns:
    (numpy array) : NxT array in which each row corresponds to trajectory
  '''
  # generate all the random steps for all steps in all simulations in one go
  # produces a N x T array
  steps = np.random.normal(mu, sigma, size=(N, T))

  # compute the cumulative sum of all the steps over the time axis
  sim = np.cumsum(steps, axis=1)

  return sim


np.random.seed(2020) # set random seed

# simulate 1000 random walks for 10000 time steps
sim = random_walk_simulator(1000, 10000,  mu=0, sigma=1)

# take a peek at the first 10 simulations
with plt.xkcd():
  plot_random_walk_sims(sim, nsims=10)
```

→ twin `pseudocode/W2D3_Tutorial3_Pseudocode_39e8cb46.md` · answer `solutions/W2D3_Tutorial3_Solution_39e8cb46.py`

---

## Exercise 3.2 — Simulate random walks

Blanked skeleton (fill the `____`):

```text
# Simulate random walks
np.random.seed(2020) # set random seed
sim = random_walk_simulator(5000, 1000, mu=0, sigma=1)

# Compute mean
mu = ____

# Compute variance
var = ____

# Visualize
with plt.xkcd():
  plot_mean_var_by_timestep(mu, var)
```

**Blanks:** `mu` (Compute mean); `var` (Compute variance)

→ twin `pseudocode/W2D3_Tutorial3_Pseudocode_796a6346.md` · answer `solutions/W2D3_Tutorial3_Solution_796a6346.py`

---

## Exercise 3.3 — `ddm`

Blanked skeleton (fill the `____`):

```text
def ddm(T, x0, xinfty, lam, sig):
  t = np.arange(0, T, 1.)
  x = np.zeros_like(t)
  x[0] = x0

  for k in range(len(t)-1):
    x[k+1] = xinfty + lam * (x[k] - xinfty) + sig * np.random.standard_normal(size=1)

  return t, x


# computes equilibrium variance of ddm
# returns variance
def ddm_eq_var(T, x0, xinfty, lam, sig):
  t, x = ddm(T, x0, xinfty, lam, sig)

  # returns variance of the second half of the simulation
  # this is a hack: assumes system has settled by second half
  return x[-round(T/2):].var()


np.random.seed(2020) # set random seed

# sweep through values for lambda
lambdas = np.arange(0.05, 0.95, 0.01)
empirical_variances = np.zeros_like(lambdas)
analytical_variances = ____

sig = 0.87

# compute empirical equilibrium variance
for i, lam in enumerate(lambdas):
  empirical_variances[i] = ddm_eq_var(5000, x0, xinfty, lambdas[i], sig)

# Hint: you can also do this in one line outside the loop!
analytical_variances = ____

# Plot the empirical variance vs analytical variance
with plt.xkcd():
  var_comparison_plot(empirical_variances, analytical_variances)
```

**Blanks:** `analytical_variances` (fill in); `analytical_variances` (Hint: you can also do this in one line outside the loop!)

→ twin `pseudocode/W2D3_Tutorial3_Pseudocode_d35fe99c.md` · answer `solutions/W2D3_Tutorial3_Solution_d35fe99c.py`

---

## Exercise 3.4 — `simulate_ddm`

Blanked skeleton (fill the `____`):

```text
def simulate_ddm(lam, sig, x0, xinfty, T):
  """
  Simulate the drift-diffusion model with given parameters and initial condition.
  Args:
    lam (scalar): decay rate
    sig (scalar): standard deviation of normal distribution
    x0 (scalar): initial condition (x at time 0)
    xinfty (scalar): drift towards convergence in the limit
    T (scalar): total duration of the simulation (in steps)

  Returns:
    ndarray, ndarray: `x` for all simulation steps and the time `t` at each step
  """

  # initialize variables
  t = np.arange(0, T, 1.)
  x = np.zeros_like(t)
  x[0] = x0

  # Step through in time
  for k in range(len(t)-1):
    # update x at time k+1 with a deterministic and a stochastic component
    # hint: the deterministic component will be like above, and
    #   the stochastic component is drawn from a scaled normal distribution
    x[k+1] = xinfty + lam * (x[k] - xinfty) + sig * np.random.standard_normal(size=1)

  return t, x


lam = 0.9  # decay rate
sig = 0.1  # standard deviation of diffusive process
T = 500  # total Time duration in steps
x0 = 4.  # initial condition of x at time 0
xinfty = 1.  # x drifts towards this value in long time

# Plot x as it evolves in time
np.random.seed(2020)
t, x = simulate_ddm(lam, sig, x0, xinfty, T)
with plt.xkcd():
  plot_ddm(t, x, xinfty, lam, x0)
```

→ twin `pseudocode/W2D3_Tutorial3_Pseudocode_efebd1e4.md` · answer `solutions/W2D3_Tutorial3_Solution_efebd1e4.py`

---
