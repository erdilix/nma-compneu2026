# Pseudocode twin — W2D2 Tutorial 1: `compute_aliased_frequency`

- **Answer twin:** `../solutions/W2D2_Tutorial1_Solution_cc52b2cd.py`
- **Reading view:** `../W2D2_Tutorial1_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def compute_aliased_frequency(signal_freq, sampling_rate):
    """Compute the apparent frequency after aliasing.

    Parameters
    ----------
    signal_freq   : float, true signal frequency (Hz)
    sampling_rate : float, sampling rate (Hz)

    Returns
    -------
    float : apparent frequency (Hz). Returns signal_freq if no aliasing.
    """

    if sampling_rate >= 2 * signal_freq:
        # above Nyquist — no aliasing
        return signal_freq

    f_alias = ____
    return f_alias
```

Blanks:
1. `f_alias` — fill in
