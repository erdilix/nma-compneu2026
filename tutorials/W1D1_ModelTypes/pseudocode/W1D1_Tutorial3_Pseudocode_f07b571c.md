# Pseudocode twin — W1D1 Tutorial 3, Exercise 3.2 (Entropy)

- **Solves:** `entropy` — Shannon entropy of a discrete distribution, in bits
- **Answer twin:** `../solutions/W1D1_Tutorial3_Solution_f07b571c.py`
- **Reading view:** `../W1D1_Tutorial3_pseudocode.md`

Idea: entropy $H = -\sum_i p_i \log_2 p_i$. Drop zero-mass bins first — $\log_2 0$ is undefined.

```text
FUNCTION entropy(pmf):
    pmf ← ____                 # FILL: keep only entries where pmf > 0
    h   ← ____                 # FILL: -sum( pmf * log2(pmf) )
    RETURN ____                # FILL: abs(h)  (avoids a -0.0 result)
```

Blanks to fill:
1. `pmf` — `pmf[pmf > 0]` (mask out zero-probability bins).
2. `h` — `-np.sum(pmf * np.log2(pmf))`.
3. return — `np.abs(h)`.
