# W2D2 · Tutorial 1 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 1.1 — `sinc`

Blanked skeleton (fill the `____`):

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

→ twin `pseudocode/W2D2_Tutorial1_Pseudocode_09e11e80.md` · answer `solutions/W2D2_Tutorial1_Solution_09e11e80.py`

---

## Exercise 1.2 — `subsample`

Blanked skeleton (fill the `____`):

```text
def subsample(t_total, sig_total, fs, phase):
    """Subsample a dense signal at a target rate.

    Parameters
    ----------
    t_total   : (N,) full time axis at FS_TRUE resolution
    sig_total : (N,) full signal
    fs        : float, target sampling rate in Hz

    Returns
    -------
    t_samp : (M,) sample times
    y_samp : (M,) sample values
    """

    step   = max(1, int(round(FS_TRUE / fs)))
    idx    = np.arange(int(np.round(0+phase/2/np.pi*step)), len(t_total), step)
    return t_total[idx], sig_total[idx]
```

→ twin `pseudocode/W2D2_Tutorial1_Pseudocode_18db7688.md` · answer `solutions/W2D2_Tutorial1_Solution_18db7688.py`

---

## Exercise 1.3 — `make_sine_wave`

Blanked skeleton (fill the `____`):

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

**Blanks:** `s` (Compute the sine wave  s(t) = A · sin(2π f t + φ))

→ twin `pseudocode/W2D2_Tutorial1_Pseudocode_60e0f477.md` · answer `solutions/W2D2_Tutorial1_Solution_60e0f477.py`

---

## Exercise 1.4 — `compute_aliased_frequency`

Blanked skeleton (fill the `____`):

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

**Blanks:** `f_alias` (fill in)

→ twin `pseudocode/W2D2_Tutorial1_Pseudocode_cc52b2cd.md` · answer `solutions/W2D2_Tutorial1_Solution_cc52b2cd.py`

---
