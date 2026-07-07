# W2D4 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 4.1 — `generate_P`

Blanked skeleton (fill the `____`):

```text
def generate_P(pars, pre_spike_train_ex):
  """
  track of pre-synaptic spikes

  Args:
    pars               : parameter dictionary
    pre_spike_train_ex : binary spike train input from
                         presynaptic excitatory neuron

  Returns:
    P                  : LTP ratio
  """

  # Get parameters
  A_plus, tau_stdp = pars['A_plus'], pars['tau_stdp']
  dt, range_t = pars['dt'], pars['range_t']
  Lt = range_t.size

  # Initialize
  P = np.zeros(pre_spike_train_ex.shape)
  for it in range(Lt - 1):
    # Calculate the delta increment dP
    dP = ____
    # Update P
    P[:, it + 1] = P[:, it] + dP

  return P


pars = default_pars_STDP(T=200., dt=1.)
pre_spike_train_ex = Poisson_generator(pars, rate=10, n=5, myseed=2020)
P = generate_P(pars, pre_spike_train_ex)
with plt.xkcd():
  my_example_P(pre_spike_train_ex, pars, P)
```

**Blanks:** `dP` (Calculate the delta increment dP)

→ twin `pseudocode/W2D4_Tutorial4_Pseudocode_4e3afedb.md` · answer `solutions/W2D4_Tutorial4_Solution_4e3afedb.py`

---

## Exercise 4.2 — `Delta_W`

Blanked skeleton (fill the `____`):

```text
def Delta_W(pars, A_plus, A_minus, tau_stdp):
  """
  Plot STDP biphasic exponential decaying function

  Args:
    pars       : parameter dictionary
    A_plus     : (float) maximum amount of synaptic modification
                 which occurs when the timing difference between pre- and
                 post-synaptic spikes is positive
    A_minus    : (float) maximum amount of synaptic modification
                 which occurs when the timing difference between pre- and
                 post-synaptic spikes is negative
    tau_stdp   : the ranges of pre-to-postsynaptic interspike intervals
                 over which synaptic strengthening or weakening occurs

  Returns:
    dW         : instantaneous change in weights
  """

  # STDP change
  dW = np.zeros(len(time_diff))
  # Calculate dW for LTP
  dW[time_diff <= 0] = A_plus * np.exp(time_diff[time_diff <= 0] / tau_stdp)
  # Calculate dW for LTD
  dW[time_diff > 0] = -A_minus * np.exp(-time_diff[time_diff > 0] / tau_stdp)

  return dW


pars = default_pars_STDP()
# Get parameters
A_plus, A_minus, tau_stdp = pars['A_plus'], pars['A_minus'], pars['tau_stdp']
# pre_spike time - post_spike time
time_diff = np.linspace(-5 * tau_stdp, 5 * tau_stdp, 50)

dW = Delta_W(pars, A_plus, A_minus, tau_stdp)
with plt.xkcd():
  mySTDP_plot(A_plus, A_minus, tau_stdp, time_diff, dW)
```

→ twin `pseudocode/W2D4_Tutorial4_Pseudocode_54b83ed8.md` · answer `solutions/W2D4_Tutorial4_Solution_54b83ed8.py`

---
