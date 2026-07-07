# Pseudocode twin — W1D2 Tutorial 3: `resample_with_replacement`

- **Answer twin:** `../solutions/W1D2_Tutorial3_Solution_81af3bd6.py`
- **Reading view:** `../W1D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def resample_with_replacement(x, y):
  """Resample data points with replacement from the dataset of `x` inputs and
  `y` measurements.

  Args:
    x (ndarray): An array of shape (samples,) that contains the input values.
    y (ndarray): An array of shape (samples,) that contains the corresponding
      measurement values to the inputs.

  Returns:
    ndarray, ndarray: The newly resampled `x` and `y` data points.
  """

  # Get array of indices for resampled points
  sample_idx = ____

  # Sample from x and y according to sample_idx
  x_ = ____
  y_ = ____

  return x_, y_

x_, y_ = resample_with_replacement(x, y)

with plt.xkcd():
  plot_original_and_resample(x, y, x_, y_)
```

Blanks:
1. `sample_idx` — Get array of indices for resampled points
2. `x_` — Sample from x and y according to sample_idx
3. `y_` — fill in
