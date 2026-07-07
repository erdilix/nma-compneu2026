# W3D3 · Tutorial 5 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **1** code exercise(s).

---

## Exercise 5.1 — `m_step`

Blanked skeleton (fill the `____`):

```text
def m_step(gamma, xi, dt):
  """Calculate the M-step updates for the HMM spiking model.
  Args:
    gamma (numpy 3d array): singleton marginal distribution.
                            Has shape (n_trials, T, K)
    xi (numpy 3d array): Tensor of recordings, has shape (n_trials, T, C)
    dt (float):         Duration of a time bin
  Returns:
    psi_new (numpy vector): Updated initial probabilities for each state
    A_new (numpy matrix):   Updated transition matrix, A[i,j] represents the
                            prob. to switch from j to i. Has shape (K,K)
    L_new (numpy matrix):   Updated Poisson rate parameter for different
                            cells. Has shape (C,K)
  """
  # Calculate and normalize the new initial probabilities, psi_new
  psi_new = ____
  # Make sure the probabilities are normalized

  psi_new /= psi_new.sum()
  # Calculate new transition matrix
  A_new = xi.sum(axis=(0, 1)) / gamma[:, :-1].sum(axis=(0, 1))[:, np.newaxis]
  # Calculate new firing rates
  L_new = (np.swapaxes(Y, -1, -2) @ gamma).sum(axis=0) / gamma.sum(axis=(0, 1)) / dt
  return psi_new, A_new, L_new
```

**Blanks:** `psi_new` (Calculate and normalize the new initial probabilities, psi_new)

→ twin `pseudocode/W3D3_Tutorial5_Pseudocode_a471c4a4.md` · answer `solutions/W3D3_Tutorial5_Solution_a471c4a4.py`

---
