# W1D5 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 3.1 — `correlate_rdms`

Blanked skeleton (fill the `____`):

```text
def correlate_rdms(rdm1, rdm2):
  """Correlate off-diagonal elements of two RDM's

  Args:
    rdm1 (np.ndarray): S x S representational dissimilarity matrix
    rdm2 (np.ndarray): S x S representational dissimilarity matrix to
      correlate with rdm1

  Returns:
    float: correlation coefficient between the off-diagonal elements
      of rdm1 and rdm2

  """

  # Extract off-diagonal elements of each RDM
  ioffdiag = np.triu_indices(rdm1.shape[0], k=1)  # indices of off-diagonal elements
  rdm1_offdiag = rdm1[ioffdiag]
  rdm2_offdiag = rdm2[ioffdiag]

  corr_coef = np.corrcoef(rdm1_offdiag, rdm2_offdiag)[0,1]

  return corr_coef


# Split RDMs into V1 responses and model responses
rdm_model = rdm_dict.copy()
rdm_v1 = rdm_model.pop('V1 data')

# Correlate off-diagonal terms of dissimilarity matrices
rdm_sim = {label: correlate_rdms(rdm_v1, rdm) for label, rdm in rdm_model.items()}

# Visualize
with plt.xkcd():
  plot_rdm_rdm_correlations(rdm_sim)
```

→ twin `pseudocode/W1D5_Tutorial3_Pseudocode_ce2f98e6.md` · answer `solutions/W1D5_Tutorial3_Solution_ce2f98e6.py`

---

## Exercise 3.2 — `RDM`

Blanked skeleton (fill the `____`):

```text
def RDM(resp):
  """Compute the representational dissimilarity matrix (RDM)

  Args:
    resp (ndarray): S x N matrix with population responses to
      each stimulus in each row

  Returns:
    ndarray: S x S representational dissimilarity matrix
  """

  # z-score responses to each stimulus
  zresp = zscore(resp, axis=1)

  # Compute RDM
  RDM = ____

  return RDM


# Compute RDMs for each layer
rdm_dict = {label: RDM(resp) for label, resp in resp_dict.items()}

# Plot RDMs
with plt.xkcd():
  plot_multiple_rdm(rdm_dict)
```

**Blanks:** `RDM` (Compute RDM)

→ twin `pseudocode/W1D5_Tutorial3_Pseudocode_ed074d46.md` · answer `solutions/W1D5_Tutorial3_Solution_ed074d46.py`

---
