# Pseudocode twin — W2D2 Tutorial 3: `filter_lfp`

- **Answer twin:** `../solutions/W2D2_Tutorial3_Solution_61122161.py`
- **Reading view:** `../W2D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def filter_lfp(lfp, fs, filter_type, freqs):
    """
    Design and apply a 4th-order Butterworth filter.

    Parameters
    ----------
    lfp         : 1-D array
    fs          : float, sampling rate in Hz
    filter_type : str, 'low', 'high', or 'band'
    freqs       : float or [float, float]

    Returns
    -------
    filtered, b, a
    """

    b, a = signal.butter(4, freqs, btype=filter_type, fs=fs)
    filtered = ____
    return filtered, b, a
```

Blanks:
1. `filtered` — fill in
