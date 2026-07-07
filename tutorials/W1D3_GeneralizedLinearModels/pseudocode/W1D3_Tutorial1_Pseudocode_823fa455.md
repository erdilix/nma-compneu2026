# Pseudocode twin — W1D3 Tutorial 1: `predict_spike_counts_lg`

- **Answer twin:** `../solutions/W1D3_Tutorial1_Solution_823fa455.py`
- **Reading view:** `../W1D3_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def predict_spike_counts_lg(stim, spikes, d=25):
  """Compute a vector of predicted spike counts given the stimulus.

  Args:
    stim (1D array): Stimulus values at each timepoint
    spikes (1D array): Spike counts measured at each timepoint
    d (number): Number of time lags to use.

  Returns:
    yhat (1D array): Predicted spikes at each timepoint.

  """

  # Create the design matrix
  y = spikes
  constant = ____
  X = ____

  # Get the MLE weights for the LG model
  theta = ____

  # Compute predicted spike counts
  yhat = X @ theta

  return yhat


# Predict spike counts
predicted_counts = predict_spike_counts_lg(stim, spikes)

# Visualize
with plt.xkcd():
  plot_spikes_with_prediction(spikes, predicted_counts, dt_stim)
```

Blanks:
1. `constant` — fill in
2. `X` — fill in
3. `theta` — Get the MLE weights for the LG model
