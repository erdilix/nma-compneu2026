# Pseudocode twin — W3D3 Tutorial 4: `kalman_smooth`

- **Answer twin:** `../solutions/W3D3_Tutorial4_Solution_a7cea8e4.py`
- **Reading view:** `../W3D3_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `J` — write the expression to compute the Kalman gain for the backward process
2. `mu_hat[t]` — write the expression to compute the smoothed state mean estimate
3. `sigma_hat[t]` — write the expression to compute the smoothed state noise covariance estimate
