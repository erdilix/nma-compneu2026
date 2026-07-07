# W2D3 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 2.1 — hint: see np.diff()

Blanked skeleton (fill the `____`):

```text
# hint: see np.diff()
inter_switch_intervals = ____

# plot inter-switch intervals
with plt.xkcd():
  plot_interswitch_interval_histogram(inter_switch_intervals)
```

**Blanks:** `inter_switch_intervals` (hint: see np.diff())

→ twin `pseudocode/W2D3_Tutorial2_Pseudocode_15275c81.md` · answer `solutions/W2D3_Tutorial2_Solution_15275c81.py`

---

## Exercise 2.2 — Initialize variables

Blanked skeleton (fill the `____`):

```text
"""
1) Whichever eigenvalue is 1 is the stable solution. There should be another
eigenvalue that is <1, which means it is decaying and goes away after the
transient period.

2) The eigenvector corresponding to this eigenvalue is the stable solution.

3) To see this, we need to normalize this eigenvector so that its 2 elements
sum to one, then we would see that the two numbers correspond to
[P(open), P(closed)] at equilibrium -- hopefully these are exactly the
equilibrium solutions observed in Section 2.
""";

# whichever eigenvalue is 1, the other one makes no sense
print(eigenvector1 / eigenvector1.sum())
print(eigenvector2 / eigenvector2.sum())
```

→ twin `pseudocode/W2D3_Tutorial2_Pseudocode_37abbdad.md` · answer `solutions/W2D3_Tutorial2_Solution_37abbdad.py`

---

## Exercise 2.3 — `simulate_prob_prop`

Blanked skeleton (fill the `____`):

```text
def simulate_prob_prop(A, x0, dt, T):
  """ Simulate the propagation of probabilities given the transition matrix A,
  with initial state x0, for a duration of T at timestep dt.

  Args:
    A (ndarray): state transition matrix
    x0 (ndarray): state probabilities at time 0
    dt (scalar): timestep of the simulation
    T (scalar): total duration of the simulation

  Returns:
    ndarray, ndarray: `x` for all simulation steps and the time `t` at each step
  """

  # Initialize variables
  t = np.arange(0, T, dt)
  x = x0 # x at time t_0

  # Step through the system in time
  for k in range(len(t)-1):
    # Compute the state of x at time k+1
    x_kp1 = np.dot(A, x[-1,:])

    # Stack (append) this new state onto x to keep track of x through time steps
    x = np.vstack((x, x_kp1))

  return x, t


# Set parameters
T = 500     # total Time duration
dt = 0.1   # timestep of our simulation

# same parameters as above
# c: closed rate
# o: open rate
c = 0.02
o = 0.1
A = np.array([[1 - c*dt, o*dt],
              [c*dt,     1 - o*dt]])

# Initial condition: start as Closed
x0 = np.array([[1, 0]])

# Simulate probabilities propagation
x, t = simulate_prob_prop(A, x0, dt, T)

# Visualize
with plt.xkcd():
  plot_state_probabilities(t, x)
```

→ twin `pseudocode/W2D3_Tutorial2_Pseudocode_41ec6e01.md` · answer `solutions/W2D3_Tutorial2_Solution_41ec6e01.py`

---
