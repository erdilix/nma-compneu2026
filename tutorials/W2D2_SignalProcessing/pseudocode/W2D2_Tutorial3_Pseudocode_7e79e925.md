# Pseudocode twin — W2D2 Tutorial 3: `apply_system`

- **Answer twin:** `../solutions/W2D2_Tutorial3_Solution_7e79e925.py`
- **Reading view:** `../W2D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def apply_system(x, h, dt):
    """Compute the LTI output y = x * h via the direct convolution sum."""
    N, M = len(x), len(h)
    y = np.zeros(N)

    for n in range(N):
        for m in range(min(n + 1, M)):

            # Multiply the input m steps back by the m-th kernel sample
            contribution = ____
            # Accumulate into the output (don't forget the dt factor)
            y[n] = ____
    return y
```

Blanks:
1. `contribution` — Multiply the input m steps back by the m-th kernel sample
2. `y[n]` — Accumulate into the output (don't forget the dt factor)
