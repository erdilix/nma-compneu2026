# Pseudocode twin — W2D2 Tutorial 1: `make_sine_wave`

- **Answer twin:** `../solutions/W2D2_Tutorial1_Solution_60e0f477.py`
- **Reading view:** `../W2D2_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def make_sine_wave(t, A, f, phi):
    """Generate a sine wave.

    Args:
        t (ndarray): time samples in seconds, shape (n_samples,)
        A (float):   amplitude
        f (float):   frequency in Hz
        phi (float): phase offset in radians

    Returns:
        ndarray: s(t) = A * sin(2π f t + φ), shape (n_samples,)
    """

    # Compute the sine wave  s(t) = A · sin(2π f t + φ)
    s = ____
    return s
```

Blanks:
1. `s` — Compute the sine wave  s(t) = A · sin(2π f t + φ)
