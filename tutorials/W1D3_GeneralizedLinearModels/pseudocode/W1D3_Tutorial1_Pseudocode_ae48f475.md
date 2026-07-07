# Pseudocode twin — W1D3 Tutorial 1: `predict_spike_counts_lnp`

- **Answer twin:** `../solutions/W1D3_Tutorial1_Solution_ae48f475.py`
- **Reading view:** `../W1D3_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def predict_spike_counts_lnp(stim, spikes, theta=None, d=25):
  """Compute a vector of predicted spike counts given the stimulus.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    theta (1D array): Filter weights; estimated if not provided.
    d (number): Number of time lags to use.

  Returns:
    yhat (1D array): Predicted spikes at each timepoint.

  """
  y = spikes
  constant = np.ones_like(spikes)
  X = np.column_stack([constant, make_design_matrix(stim)])
  if theta is None:  # Allow pre-cached weights, as fitting is slow
    theta = fit_lnp(X, y, d)

  yhat = ____
  return yhat


# Predict spike counts
yhat = ____

# Visualize
with plt.xkcd():
  plot_spikes_with_prediction(spikes, yhat, dt_stim)
```

Blanks:
1. `yhat` — fill in
2. `yhat` — Predict spike counts
