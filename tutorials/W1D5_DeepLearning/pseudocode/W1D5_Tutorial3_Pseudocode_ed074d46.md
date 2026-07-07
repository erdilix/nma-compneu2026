# Pseudocode twin — W1D5 Tutorial 3: `RDM`

- **Answer twin:** `../solutions/W1D5_Tutorial3_Solution_ed074d46.py`
- **Reading view:** `../W1D5_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `RDM` — Compute RDM
