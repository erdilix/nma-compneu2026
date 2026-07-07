# Pseudocode twin — W2D2 Tutorial 1: `sinc`

- **Answer twin:** `../solutions/W2D2_Tutorial1_Solution_09e11e80.py`
- **Reading view:** `../W2D2_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def sinc(u):
    """Evaluate the sinc function at u.

    Parameters
    ----------
    u : float or np.ndarray
        Argument(s) to evaluate. Units are normalised sample intervals.

    Returns
    -------
    float or np.ndarray
        sinc(u) = sin(pi * u) / (pi * u), with sinc(0) = 1.
    """

    u = np.asarray(u, dtype=float)
    denom = np.pi * u
    y     = np.where(u == 0, 1.0, np.sin(denom) / denom)
    return y
```
