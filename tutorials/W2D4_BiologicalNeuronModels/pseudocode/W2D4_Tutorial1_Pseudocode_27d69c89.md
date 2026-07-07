# Pseudocode twin — W2D4 Tutorial 1: `isi_cv_LIF`

- **Answer twin:** `../solutions/W2D4_Tutorial1_Solution_27d69c89.py`
- **Reading view:** `../W2D4_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def isi_cv_LIF(spike_times):
  """
  Calculates the inter-spike intervals (isi) and
  the coefficient of variation (cv) for a given spike_train

  Args:
    spike_times : (n, ) vector with the spike times (ndarray)

  Returns:
    isi         : (n-1,) vector with the inter-spike intervals (ms)
    cv          : coefficient of variation of isi (float)

  """

  if len(spike_times) >= 2:
    # Compute isi
    isi = ____
    # Compute cv
    cv = ____
  else:
    isi = ____
    cv = ____

  return isi, cv


# Set parameters
pars = default_pars(T=1000.)
mu_gwn = 250
sig_gwn1 = 0.5
sig_gwn2 = 3.0

# Run LIF model for sigma = 0.5
I_GWN1 = my_GWN(pars, mu=mu_gwn, sig=sig_gwn1, myseed=2020)
_, sp1 = run_LIF(pars, Iinj=I_GWN1)

# Run LIF model for sigma = 3
I_GWN2 = my_GWN(pars, mu=mu_gwn, sig=sig_gwn2, myseed=2020)
_, sp2 = run_LIF(pars, Iinj=I_GWN2)

# Compute ISIs/CV
isi1, cv1 = isi_cv_LIF(sp1)
isi2, cv2 = isi_cv_LIF(sp2)

# Visualize
with plt.xkcd():
  my_hists(isi1, isi2, cv1, cv2, sig_gwn1, sig_gwn2)
```

Blanks:
1. `isi` — Compute isi
2. `cv` — Compute cv
3. `isi` — fill in
4. `cv` — fill in
