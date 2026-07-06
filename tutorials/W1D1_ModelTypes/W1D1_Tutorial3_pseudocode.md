# W1D1 · Tutorial 3 — "Why" Models (information / entropy) · pseudocode companion

Reading view: each coding exercise's blanked code cell + a fill-in-the-blank pseudocode box. Twins in `pseudocode/`, answers in `solutions/`.

Tutorial 3 has **2** coding exercises.

---

## Exercise 3.1 — `pmf_from_counts`

Original code cell:

```python
def pmf_from_counts(counts):
  """Given counts, normalize by the total to estimate probabilities."""
  pmf = ...
  return pmf
```

**Pseudocode (fill the `____`):**

```text
FUNCTION pmf_from_counts(counts):
    pmf ← ____                 # normalize = counts / sum(counts)
    RETURN pmf
```

→ twin `pseudocode/W1D1_Tutorial3_Pseudocode_960d622a.md` · answer `solutions/W1D1_Tutorial3_Solution_960d622a.py`

---

## Exercise 3.2 — `entropy`

Original code cell:

```python
def entropy(pmf):
  """Return the Shannon entropy (bits) of a discrete distribution."""
  # 1. exclude zero-mass points (log2(0) undefined)
  # 2. implement H = -sum(p * log2 p)
  # 3. return abs value
  ...
```

**Pseudocode (fill the `____`):**

```text
FUNCTION entropy(pmf):
    pmf ← ____                 # keep only entries where pmf > 0
    h   ← ____                 # -sum( pmf * log2(pmf) )
    RETURN ____                # abs(h)
```

→ twin `pseudocode/W1D1_Tutorial3_Pseudocode_f07b571c.md` · answer `solutions/W1D1_Tutorial3_Solution_f07b571c.py`
