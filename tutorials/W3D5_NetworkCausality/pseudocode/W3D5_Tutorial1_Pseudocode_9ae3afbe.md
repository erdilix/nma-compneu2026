# Pseudocode twin — W3D5 Tutorial 1: `neuron_B`

- **Answer twin:** `../solutions/W3D5_Tutorial1_Solution_9ae3afbe.py`
- **Reading view:** `../W3D5_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def neuron_B(activity_of_A):
  """Model activity of neuron B as neuron A activity + noise

  Args:
    activity_of_A (ndarray): An array of shape (T,) containing the neural activity of neuron A

  Returns:
    ndarray: activity of neuron B
  """
  noise = np.random.randn(activity_of_A.shape[0])
  return activity_of_A + noise

np.random.seed(12)

# Neuron A activity of zeros
A_0 = np.zeros(5000)

# Neuron A activity of ones
A_1 = np.ones(5000)

diff_in_means = ____
print(diff_in_means)
```

Blanks:
1. `diff_in_means` — fill in
