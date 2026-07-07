# W3D3 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 4.1 — `kalman_filter`

Blanked skeleton (fill the `____`):

```text
def kalman_filter(data, params):
  """ Perform Kalman filtering (forward pass) on the data given the provided
  system parameters.

  Args:
    data (ndarray): a sequence of observations of shape(n_timesteps, n_dim_obs)
    params (dict): a dictionary of model parameters: (D, Q, H, R, mu_0, sigma_0)

  Returns:
    ndarray, ndarray: the filtered system means and noise covariance values
  """
  # pulled out of the params dict for convenience
  D = params['D']
  Q = params['Q']
  H = params['H']
  R = params['R']

  n_dim_state = D.shape[0]
  n_dim_obs = H.shape[0]
  I = np.eye(n_dim_state)  # identity matrix

  # state tracking arrays
  mu = np.zeros((len(data), n_dim_state))
  sigma = np.zeros((len(data), n_dim_state, n_dim_state))

  # filter the data
  for t, y in enumerate(data):
    if t == 0:
      mu_pred = params['mu_0']
      sigma_pred = params['sigma_0']
    else:
      mu_pred = D @ mu[t-1]
      sigma_pred = D @ sigma[t-1] @ D.T + Q

    # write the expression for computing the Kalman gain
    K = ____
    # write the expression for computing the filtered state mean
    mu[t] = ____
    # write the expression for computing the filtered state noise covariance
    sigma[t] = ____

  return mu, sigma


filtered_state_means, filtered_state_covariances = kalman_filter(obs, params)
with plt.xkcd():
  plot_kalman(state, obs, filtered_state_means, title="my kf-filter",
              color='r', label='my kf-filter')
```

**Blanks:** `K` (write the expression for computing the Kalman gain); `mu[t]` (write the expression for computing the filtered state mean); `sigma[t]` (write the expression for computing the filtered state noise covariance)

→ twin `pseudocode/W3D3_Tutorial4_Pseudocode_3549ecf3.md` · answer `solutions/W3D3_Tutorial4_Solution_3549ecf3.py`

---

## Exercise 4.2 — `sample_lds`

Blanked skeleton (fill the `____`):

```text
def sample_lds(n_timesteps, params, seed=0):
  """ Generate samples from a Linear Dynamical System specified by the provided
  parameters.

  Args:
  n_timesteps (int): the number of time steps to simulate
  params (dict): a dictionary of model parameters: (D, Q, H, R, mu_0, sigma_0)
  seed (int): a random seed to use for reproducibility checks

  Returns:
  ndarray, ndarray: the generated state and observation data
  """
  n_dim_state = params['D'].shape[0]
  n_dim_obs = params['H'].shape[0]

  # set seed
  np.random.seed(seed)

  # precompute random samples from the provided covariance matrices
  # mean defaults to 0
  mi = stats.multivariate_normal(cov=params['Q']).rvs(n_timesteps)
  eta = stats.multivariate_normal(cov=params['R']).rvs(n_timesteps)

  # initialize state and observation arrays
  state = np.zeros((n_timesteps, n_dim_state))
  obs = np.zeros((n_timesteps, n_dim_obs))

  # simulate the system
  for t in range(n_timesteps):
    # write the expressions for computing state values given the time step
    if t == 0:
      state[t] = ____
                                           cov=params['sigma_0']).rvs(1)
    else:
      state[t] = ____

    # write the expression for computing the observation
    obs[t] = ____

  return state, obs


state, obs = sample_lds(100, params)
print('sample at t=3 ', state[3])
with plt.xkcd():
  plot_kalman(state, obs, title='sample')
```

**Blanks:** `state[t]` (fill in); `state[t]` (fill in); `obs[t]` (write the expression for computing the observation)

→ twin `pseudocode/W3D3_Tutorial4_Pseudocode_82cbb57a.md` · answer `solutions/W3D3_Tutorial4_Solution_82cbb57a.py`

---

## Exercise 4.3 — `kalman_smooth`

Blanked skeleton (fill the `____`):

```text
def kalman_smooth(data, params):
  """ Perform Kalman smoothing (backward pass) on the data given the provided
  system parameters.

  Args:
    data (ndarray): a sequence of observations of shape(n_timesteps, n_dim_obs)
    params (dict): a dictionary of model parameters: (D, Q, H, R, mu_0, sigma_0)

  Returns:
    ndarray, ndarray: the smoothed system means and noise covariance values
  """
  # pulled out of the params dict for convenience
  D= params['D']
  Q = params['Q']
  H = params['H']
  R = params['R']

  n_dim_state = D.shape[0]
  n_dim_obs = H.shape[0]

  # first run the forward pass to get the filtered means and covariances
  mu, sigma = kalman_filter(data, params)

  # initialize state mean and covariance estimates
  mu_hat = np.zeros_like(mu)
  sigma_hat = np.zeros_like(sigma)
  mu_hat[-1] = mu[-1]
  sigma_hat[-1] = sigma[-1]

  # smooth the data
  for t in reversed(range(len(data)-1)):
    sigma_pred = D@ sigma[t] @ D.T + Q  # sigma_pred at t+1

    # write the expression to compute the Kalman gain for the backward process
    J = ____
    # write the expression to compute the smoothed state mean estimate
    mu_hat[t] = ____
    # write the expression to compute the smoothed state noise covariance estimate
    sigma_hat[t] = ____

  return mu_hat, sigma_hat


smoothed_state_means, smoothed_state_covariances = kalman_smooth(obs, params)
with plt.xkcd():
  axes = plot_kalman(state, obs, filtered_state_means, color="r",
                     label="my kf-filter")
  plot_kalman(state, obs, smoothed_state_means, color="b",
              label="my kf-smoothed", axes=axes)
```

**Blanks:** `J` (write the expression to compute the Kalman gain for the backward process); `mu_hat[t]` (write the expression to compute the smoothed state mean estimate); `sigma_hat[t]` (write the expression to compute the smoothed state noise covariance estimate)

→ twin `pseudocode/W3D3_Tutorial4_Pseudocode_a7cea8e4.md` · answer `solutions/W3D3_Tutorial4_Solution_a7cea8e4.py`

---
