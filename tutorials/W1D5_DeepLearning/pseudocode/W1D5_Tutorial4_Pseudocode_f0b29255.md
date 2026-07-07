# Pseudocode twin — W1D5 Tutorial 4: first let's smooth the tuning curves resp_all to make sure w

- **Answer twin:** `../solutions/W1D5_Tutorial4_Solution_f0b29255.py`
- **Reading view:** `../W1D5_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
from scipy.ndimage import gaussian_filter1d

# first let's smooth the tuning curves resp_all to make sure we get
# an accurate peak that isn't just noise
# resp_all is size (n_stimuli, n_neurons)
resp_smoothed = gaussian_filter1d(resp_all, 5, axis=0)
# resp_smoothed is size (n_stimuli, n_neurons)

# find position of max response for each neuron
# aka preferred orientation for each neuron
preferred_orientation = ____

# Resort W_in matrix by preferred orientation
isort = preferred_orientation.argsort()
W_in_sorted = W_in[:, isort]

# plot resorted W_in matrix
with plt.xkcd():
  visualize_weights(W_in_sorted, W_out)
```

Blanks:
1. `preferred_orientation` — aka preferred orientation for each neuron
