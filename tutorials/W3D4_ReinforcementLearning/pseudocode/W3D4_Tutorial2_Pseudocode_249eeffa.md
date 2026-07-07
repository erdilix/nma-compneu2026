# Pseudocode twin — W3D4 Tutorial 2: `update_action_value`

- **Answer twin:** `../solutions/W3D4_Tutorial2_Solution_249eeffa.py`
- **Reading view:** `../W3D4_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `value` — Write an expression for the updated action value
