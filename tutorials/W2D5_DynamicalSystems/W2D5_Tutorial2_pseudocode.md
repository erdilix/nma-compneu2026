# W2D5 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **5** code exercise(s).

---

## Exercise 2.1 — Note: aE, thetaE, aI and theta_I are in the dictionary 'pair

Blanked skeleton (fill the `____`):

```text
pars = default_pars()
x = np.arange(0, 10, .1)

print(pars['a_E'], pars['theta_E'])
print(pars['a_I'], pars['theta_I'])

# Compute the F-I curve of the excitatory population
FI_exc = ____

# Compute the F-I curve of the inhibitory population
FI_inh = ____

# Visualize
with plt.xkcd():
  plot_FI_EI(x, FI_exc, FI_inh)
```

**Blanks:** `FI_exc` (Compute the F-I curve of the excitatory population); `FI_inh` (Compute the F-I curve of the inhibitory population)

→ twin `pseudocode/W2D5_Tutorial2_Pseudocode_043dd600.md` · answer `solutions/W2D5_Tutorial2_Solution_043dd600.py`

---

## Exercise 2.2 — `simulate_wc`

Blanked skeleton (fill the `____`):

```text
def simulate_wc(tau_E, a_E, theta_E, tau_I, a_I, theta_I,
                wEE, wEI, wIE, wII, I_ext_E, I_ext_I,
                rE_init, rI_init, dt, range_t, **other_pars):
  """
  Simulate the Wilson-Cowan equations

  Args:
    Parameters of the Wilson-Cowan model

  Returns:
    rE, rI (arrays) : Activity of excitatory and inhibitory populations
  """
  # Initialize activity arrays
  Lt = range_t.size
  rE = np.append(rE_init, np.zeros(Lt - 1))
  rI = np.append(rI_init, np.zeros(Lt - 1))
  I_ext_E = I_ext_E * np.ones(Lt)
  I_ext_I = I_ext_I * np.ones(Lt)

  # Simulate the Wilson-Cowan equations
  for k in range(Lt - 1):

    # Calculate the derivative of the E population
    drE = ____
                                   a_E, theta_E))

    # Calculate the derivative of the I population
    drI = ____
                                   a_I, theta_I))

    # Update using Euler's method
    rE[k + 1] = rE[k] + drE
    rI[k + 1] = rI[k] + drI

  return rE, rI


pars = default_pars()

# Simulate first trajectory
rE1, rI1 = simulate_wc(**default_pars(rE_init=.32, rI_init=.15))

# Simulate second trajectory
rE2, rI2 = simulate_wc(**default_pars(rE_init=.33, rI_init=.15))

# Visualize
with plt.xkcd():
  my_test_plot(pars['range_t'], rE1, rI1, rE2, rI2)
```

**Blanks:** `drE` (Calculate the derivative of the E population); `drI` (Calculate the derivative of the I population)

→ twin `pseudocode/W2D5_Tutorial2_Pseudocode_15eff812.md` · answer `solutions/W2D5_Tutorial2_Solution_15eff812.py`

---

## Exercise 2.3 — `EIderivs`

Blanked skeleton (fill the `____`):

```text
def EIderivs(rE, rI,
             tau_E, a_E, theta_E, wEE, wEI, I_ext_E,
             tau_I, a_I, theta_I, wIE, wII, I_ext_I,
             **other_pars):
  """Time derivatives for E/I variables (dE/dt, dI/dt)."""

  # Compute the derivative of rE
  drEdt = ____

  # Compute the derivative of rI
  drIdt = ____

  return drEdt, drIdt


# Create vector field using EIderivs
with plt.xkcd():
  plot_complete_analysis(default_pars())
```

**Blanks:** `drEdt` (Compute the derivative of rE); `drIdt` (Compute the derivative of rI)

→ twin `pseudocode/W2D5_Tutorial2_Pseudocode_92ba9d03.md` · answer `solutions/W2D5_Tutorial2_Solution_92ba9d03.py`

---

## Exercise 2.4 — `get_E_nullcline`

Blanked skeleton (fill the `____`):

```text
def get_E_nullcline(rE, a_E, theta_E, wEE, wEI, I_ext_E, **other_pars):
  """
  Solve for rI along the rE from drE/dt = 0.

  Args:
    rE    : response of excitatory population
    a_E, theta_E, wEE, wEI, I_ext_E : Wilson-Cowan excitatory parameters
    Other parameters are ignored

  Returns:
    rI    : values of inhibitory population along the nullcline on the rE
  """
  # calculate rI for E nullclines on rI
  rI = ____

  return rI


def get_I_nullcline(rI, a_I, theta_I, wIE, wII, I_ext_I, **other_pars):
  """
  Solve for E along the rI from dI/dt = 0.

  Args:
    rI    : response of inhibitory population
    a_I, theta_I, wIE, wII, I_ext_I : Wilson-Cowan inhibitory parameters
    Other parameters are ignored

  Returns:
    rE    : values of the excitatory population along the nullcline on the rI
  """
  # calculate rE for I nullclines on rI
  rE = ____

  return rE


# Set parameters
pars = default_pars()
Exc_null_rE = np.linspace(-0.01, 0.96, 100)
Inh_null_rI = np.linspace(-.01, 0.8, 100)

# Compute nullclines
Exc_null_rI = get_E_nullcline(Exc_null_rE, **pars)
Inh_null_rE = get_I_nullcline(Inh_null_rI, **pars)

# Visualize
with plt.xkcd():
  plot_nullclines(Exc_null_rE, Exc_null_rI, Inh_null_rE, Inh_null_rI)
```

**Blanks:** `rI` (calculate rI for E nullclines on rI); `rE` (calculate rE for I nullclines on rI)

→ twin `pseudocode/W2D5_Tutorial2_Pseudocode_db10856b.md` · answer `solutions/W2D5_Tutorial2_Solution_db10856b.py`

---

## Exercise 2.5 — `F_inv`

Blanked skeleton (fill the `____`):

```text
def F_inv(x, a, theta):
  """
  Args:
    x         : the population input
    a         : the gain of the function
    theta     : the threshold of the function

  Returns:
    F_inverse : value of the inverse function
  """

  # Calculate Finverse (ln(x) can be calculated as np.log(x))
  F_inverse = ____

  return F_inverse


# Set parameters
pars = default_pars()
x = np.linspace(1e-6, 1, 100)

# Get inverse and visualize
with plt.xkcd():
  plot_FI_inverse(x, a=1, theta=3)
```

**Blanks:** `F_inverse` (Calculate Finverse (ln(x) can be calculated as np.log(x)))

→ twin `pseudocode/W2D5_Tutorial2_Pseudocode_f3500f59.md` · answer `solutions/W2D5_Tutorial2_Solution_f3500f59.py`

---
