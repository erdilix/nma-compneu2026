# Pseudocode twin — W3D4 Tutorial 2: `epsilon_greedy`

- **Answer twin:** `../solutions/W3D4_Tutorial2_Solution_8cb39bba.py`
- **Reading view:** `../W3D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def epsilon_greedy(q, epsilon):
  """Epsilon-greedy policy: selects the maximum value action with probability
  (1-epsilon) and selects randomly with epsilon probability.

  Args:
    q (ndarray): an array of action values
    epsilon (float): probability of selecting an action randomly

  Returns:
    int: the chosen action
  """
  # write a boolean expression that determines if we should take the best action
  be_greedy = ____

  if be_greedy:

    # write an expression for selecting the best action from the action values
    action = ____

  else:

    # write an expression for selecting a random action
    action = ____

  return action


# Set parameters
q = [-2, 5, 0, 1]
epsilon = 0.1

# Visualize
with plt.xkcd():
  plot_choices(q, epsilon, epsilon_greedy)
```

Blanks:
1. `be_greedy` — write a boolean expression that determines if we should take the best action
2. `action` — write an expression for selecting the best action from the action values
3. `action` — write an expression for selecting a random action
