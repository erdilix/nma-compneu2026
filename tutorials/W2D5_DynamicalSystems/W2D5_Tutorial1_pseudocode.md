# W2D5 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 1.1 — `F`

Blanked skeleton (fill the `____`):

```text
def F(x, a, theta):
  """
  Population activation function.

  Args:
    x (float): the population input
    a (float): the gain of the function
    theta (float): the threshold of the function

  Returns:
    float: the population activation response F(x) for input x
  """

  # Define the sigmoidal transfer function f = F(x)
  f = ____

  return f


# Set parameters
pars = default_pars_single()  # get default parameters
x = np.arange(0, 10, .1)      # set the range of input

# Compute transfer function
f = ____

# Visualize
with plt.xkcd():
  plot_fI(x, f)
```

**Blanks:** `f` (Define the sigmoidal transfer function f = F(x)); `f` (Compute transfer function)

→ twin `pseudocode/W2D5_Tutorial1_Pseudocode_04e84428.md` · answer `solutions/W2D5_Tutorial1_Solution_04e84428.py`

---

## Exercise 1.2 — `eig_single`

Blanked skeleton (fill the `____`):

```text
def eig_single(fp, tau, a, theta, w, I_ext, **other_pars):
  """
  Args:
    fp   : fixed point r_fp
    tau, a, theta, w, I_ext : Simulation parameters

  Returns:
    eig : eigenvalue of the linearized system
  """
  # Compute the eigenvalue
  eig = ____

  return eig


# Find the eigenvalues for all fixed points
pars = default_pars_single(w=5, I_ext=.5)
r_guess_vector = [0, .4, .9]
x_fp = my_fp_finder(pars, r_guess_vector)

for fp in x_fp:
  eig_fp = eig_single(fp, **pars)
  print(f'Fixed point1 at {fp:.3f} with Eigenvalue={eig_fp:.3f}')
```

**Blanks:** `eig` (Compute the eigenvalue)

→ twin `pseudocode/W2D5_Tutorial1_Pseudocode_12b2b44c.md` · answer `solutions/W2D5_Tutorial1_Solution_12b2b44c.py`

---

## Exercise 1.3 — Set parameters

Blanked skeleton (fill the `____`):

```text
# Set parameters
r = np.linspace(0, 1, 1000)
pars = default_pars_single(I_ext=0.5, w=5)

# Compute dr/dt
drdt = compute_drdt(r, **pars)

# Initial guesses for fixed points
r_guess_vector = [0, .4, .9]

# Find fixed point numerically
x_fps = my_fp_finder(pars, r_guess_vector)

# Visualize
with plt.xkcd():
  plot_dr_r(r, drdt, x_fps)
```

→ twin `pseudocode/W2D5_Tutorial1_Pseudocode_1c599fac.md` · answer `solutions/W2D5_Tutorial1_Solution_1c599fac.py`

---

## Exercise 1.4 — `compute_drdt`

Blanked skeleton (fill the `____`):

```text
def compute_drdt(r, I_ext, w, a, theta, tau, **other_pars):
  """Given parameters, compute dr/dt as a function of r.

  Args:
    r (1D array) : Average firing rate of the excitatory population
    I_ext, w, a, theta, tau (numbers): Simulation parameters to use
    other_pars : Other simulation parameters are unused by this function

  Returns
    drdt function for each value of r
  """
  # Calculate drdt
  drdt = ____

  return drdt


# Define a vector of r values and the simulation parameters
r = np.linspace(0, 1, 1000)
pars = default_pars_single(I_ext=0.5, w=5)

# Compute dr/dt
drdt = ____

# Visualize
with plt.xkcd():
  plot_dr_r(r, drdt)
```

**Blanks:** `drdt` (Calculate drdt); `drdt` (Compute dr/dt)

→ twin `pseudocode/W2D5_Tutorial1_Pseudocode_c4108be6.md` · answer `solutions/W2D5_Tutorial1_Solution_c4108be6.py`

---
