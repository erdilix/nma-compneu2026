# W2D5 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **3** code exercise(s).

---

## Exercise 3.1 — Check if x_fp's are the correct with the function check_fp(x

Blanked skeleton (fill the `____`):

```text
pars = default_pars()

with plt.xkcd():
  my_plot_nullcline(pars)

  # Find the first fixed point
  x_fp_1 = my_fp(pars, 0.1, 0.1)
  if check_fp(pars, x_fp_1):
    plot_fp(x_fp_1)

  # Find the second fixed point
  x_fp_2 = my_fp(pars, 0.3, 0.3)
  if check_fp(pars, x_fp_2):
    plot_fp(x_fp_2)

  # Find the third fixed point
  x_fp_3 = my_fp(pars, 0.8, 0.6)
  if check_fp(pars, x_fp_3):
    plot_fp(x_fp_3)
```

→ twin `pseudocode/W2D5_Tutorial3_Pseudocode_0dd7ba5a.md` · answer `solutions/W2D5_Tutorial3_Solution_0dd7ba5a.py`

---

## Exercise 3.2 — `get_dGdE`

Blanked skeleton (fill the `____`):

```text
def get_dGdE(fp, tau_E, a_E, theta_E, wEE, wEI, I_ext_E, **other_pars):
  """
  Compute dGdE

  Args:
    fp   : fixed point (E, I), array
    Other arguments are parameters of the Wilson-Cowan model

  Returns:
    J    : the 2x2 Jacobian matrix
  """
  rE, rI = fp

  # Calculate the J[0,0]
  dGdrE = ____

  return dGdrE


# Get fixed points
pars = default_pars()
x_fp_1 = my_fp(pars, 0.1, 0.1)
x_fp_2 = my_fp(pars, 0.3, 0.3)
x_fp_3 = my_fp(pars, 0.8, 0.6)

# Compute dGdE
dGdrE1 = get_dGdE(x_fp_1, **pars)
dGdrE2 = get_dGdE(x_fp_2, **pars)
dGdrE3 = get_dGdE(x_fp_3, **pars)

print(f'For the default case:')
print(f'dG/drE(fp1) = {dGdrE1:.3f}')
print(f'dG/drE(fp2) = {dGdrE2:.3f}')
print(f'dG/drE(fp3) = {dGdrE3:.3f}')

print('\n')

pars = default_pars(wEE=6.4, wEI=4.8, wIE=6.0, wII=1.2, I_ext_E=0.8)
x_fp_lc = my_fp(pars, 0.8, 0.8)

dGdrE_lc = get_dGdE(x_fp_lc, **pars)

print('For the limit cycle case:')
print(f'dG/drE(fp_lc) = {dGdrE_lc:.3f}')
```

**Blanks:** `dGdrE` (Calculate the J[0,0])

→ twin `pseudocode/W2D5_Tutorial3_Pseudocode_5dc5b86b.md` · answer `solutions/W2D5_Tutorial3_Solution_5dc5b86b.py`

---

## Exercise 3.3 — `get_eig_Jacobian`

Blanked skeleton (fill the `____`):

```text
def get_eig_Jacobian(fp,
                     tau_E, a_E, theta_E, wEE, wEI, I_ext_E,
                     tau_I, a_I, theta_I, wIE, wII, I_ext_I, **other_pars):
  """Compute eigenvalues of the Wilson-Cowan Jacobian matrix at fixed point."""
  # Initialization
  rE, rI = fp
  J = np.zeros((2, 2))

  # Compute the four elements of the Jacobian matrix
  J[0, 0] = (-1 + wEE * dF(wEE * rE - wEI * rI + I_ext_E,
                           a_E, theta_E)) / tau_E

  J[0, 1] = (-wEI * dF(wEE * rE - wEI * rI + I_ext_E,
                       a_E, theta_E)) / tau_E

  J[1, 0] = (wIE * dF(wIE * rE - wII * rI + I_ext_I,
                      a_I, theta_I)) / tau_I

  J[1, 1] = (-1 - wII * dF(wIE * rE - wII * rI + I_ext_I,
                           a_I, theta_I)) / tau_I

  # Compute and return the eigenvalues
  evals = np.linalg.eig(J)[0]
  return evals


# Compute eigenvalues of Jacobian
eig_1 = get_eig_Jacobian(x_fp_1, **pars)
eig_2 = get_eig_Jacobian(x_fp_2, **pars)
eig_3 = get_eig_Jacobian(x_fp_3, **pars)

print(eig_1, 'Stable point')
print(eig_2, 'Unstable point')
print(eig_3, 'Stable point')
```

→ twin `pseudocode/W2D5_Tutorial3_Pseudocode_e4231a54.md` · answer `solutions/W2D5_Tutorial3_Solution_e4231a54.py`

---
