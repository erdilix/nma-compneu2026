# W3D4 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 2.1 — `update_action_value`

Blanked skeleton (fill the `____`):

```text
def update_action_value(q, action, reward, alpha):
  """ Compute the updated action value given the learning rate and observed
  reward.

  Args:
    q (ndarray): an array of action values
    action (int): the action taken
    reward (float): the reward received for taking the action
    alpha (float): the learning rate

  Returns:
    float: the updated value for the selected action
  """

  # Write an expression for the updated action value
  value = ____

  return value


# Set parameters
q = [-2, 5, 0, 1]
action = 2
print(f"Original q({action}) value = {q[action]}")

# Update action
q[action] = update_action_value(q, 2, 10, 0.01)
print(f"Updated q({action}) value = {q[action]}")
```

**Blanks:** `value` (Write an expression for the updated action value)

→ twin `pseudocode/W3D4_Tutorial2_Pseudocode_249eeffa.md` · answer `solutions/W3D4_Tutorial2_Solution_249eeffa.py`

---

## Exercise 2.2 — `epsilon_greedy`

Blanked skeleton (fill the `____`):

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

**Blanks:** `be_greedy` (write a boolean expression that determines if we should take the best action); `action` (write an expression for selecting the best action from the action values); `action` (write an expression for selecting a random action)

→ twin `pseudocode/W3D4_Tutorial2_Pseudocode_8cb39bba.md` · answer `solutions/W3D4_Tutorial2_Solution_8cb39bba.py`

---
