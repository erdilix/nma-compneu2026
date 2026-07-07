# Pseudocode twin — W1D3 Tutorial 1: `make_design_matrix`

- **Answer twin:** `../solutions/W1D3_Tutorial1_Solution_03ed3adf.py`
- **Reading view:** `../W1D3_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def make_design_matrix(stim, d=25):
  """Create time-lag design matrix from stimulus intensity vector.

  Args:
    stim (1D array): Stimulus intensity at each time point.
    d (number): Number of time lags to use.

  Returns
    X (2D array): GLM design matrix with shape T, d

  """
  # Create version of stimulus vector with zeros before onset
  padded_stim = np.concatenate([np.zeros(d - 1), stim])

  # Construct a matrix where each row has the d frames of
  # the stimulus preceding and including timepoint t
  T = len(stim)  # Total number of timepoints (hint: number of stimulus frames)
  X = np.zeros((T, d))
  for t in range(T):
      X[t] = ____

  return X


# Make design matrix
X = make_design_matrix(stim)

# Visualize
with plt.xkcd():
  plot_glm_matrices(X, spikes, nt=50)
```

Blanks:
1. `X[t]` — fill in
