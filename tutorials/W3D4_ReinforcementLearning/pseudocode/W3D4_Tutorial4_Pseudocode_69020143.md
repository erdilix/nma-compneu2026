# Pseudocode twin — W3D4 Tutorial 4: `dyna_q_model_update`

- **Answer twin:** `../solutions/W3D4_Tutorial4_Solution_69020143.py`
- **Reading view:** `../W3D4_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def dyna_q_model_update(model, state, action, reward, next_state):
  """ Dyna-Q model update

  Args:
    model (ndarray): An array of shape (n_states, n_actions, 2) that represents
                     the model of the world i.e. what reward and next state do
                     we expect from taking an action in a state.
    state (int): the current state identifier
    action (int): the action taken
    reward (float): the reward received
    next_state (int): the transitioned to state identifier

  Returns:
    ndarray: the updated model
  """
  # Update our model with the observed reward and next state
  model[state, action] = reward, next_state

  return model
```
