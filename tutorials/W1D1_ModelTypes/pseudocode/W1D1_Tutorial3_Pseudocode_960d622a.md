# Pseudocode twin — W1D1 Tutorial 3, Exercise 3.1 (PMF)

- **Solves:** `pmf_from_counts` — turn histogram counts into a probability mass function
- **Answer twin:** `../solutions/W1D1_Tutorial3_Solution_960d622a.py`
- **Reading view:** `../W1D1_Tutorial3_pseudocode.md`

Idea: a PMF is just counts rescaled so they sum to 1.

```text
FUNCTION pmf_from_counts(counts):
    pmf ← ____                 # FILL: normalize = counts / sum(counts)
    RETURN pmf
```

Blank to fill:
1. `pmf` — `counts / np.sum(counts)`.
