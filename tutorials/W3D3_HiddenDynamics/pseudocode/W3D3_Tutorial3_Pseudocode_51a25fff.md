# Pseudocode twin — W3D3 Tutorial 3: `simulate`

- **Answer twin:** `../solutions/W3D3_Tutorial3_Solution_51a25fff.py`
- **Reading view:** `../W3D3_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def simulate(D, s0, sigma_p, T):
  """ Compute the response of the linear dynamical system.

  Args:
    D (scalar): dynamics multiplier
    s0 (scalar): initial position
    sigma_p (scalar): amount of noise in the system (standard deviation)
    T (scalar): total duration of the simulation

  Returns:
    ndarray: `s`: astrocat's trajectory up to time T
  """

  # Initialize variables
  s = np.zeros(T+1)
  s[0] = s0

  # Compute the position at time t given the position at time t-1 for all t
  # Consider that np.random.normal(mu, sigma) generates a random sample from
  # a gaussian with mean = mu and standard deviation = sigma

  for t in range(1, len(s)):

    # Update position
    s[t] = ____

  return s


# Set random seed
np.random.seed(0)

# Set parameters
D = 0.9  # parameter in s(t)
T = 50  # total time duration
s0 = 5.  # initial condition of s at time 0
sigma_p = 2 # amount of noise in the actuators of astrocat's propulsion unit

# Simulate Astrocat
s = simulate(D, s0, sigma_p, T)

# Visualize
with plt.xkcd():
  visualize_Astrocat(s, T)
```

Blanks:
1. `s[t]` — Update position
