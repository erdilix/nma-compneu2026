# Pseudocode twin — W2D2 Tutorial 4: `compute_morlet_power`

- **Answer twin:** `../solutions/W2D2_Tutorial4_Solution_d43fdaef.py`
- **Reading view:** `../W2D2_Tutorial4_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def compute_morlet_power(x, fs, freqs, n_cycles=12):
    """
    Compute Morlet wavelet power using mne.time_frequency.tfr_array_morlet.

    Args:
      x (numpy array of floats): time-domain signal
      fs (float): sampling frequency in Hz
      freqs (numpy array of floats): frequencies of interest in Hz
      n_cycles (float or array): number of cycles in the Morlet wavelet

    Returns:
      power_db (numpy array of floats): Morlet power in dB, with shape
                                       (n_frequencies, n_times)
    """

    # MNE expects shape: (n_epochs, n_channels, n_times)
    data_mne = x[np.newaxis, np.newaxis, :]

    # Compute power using MNE-Python
    power = ____
        data_mne,
        sfreq=fs,
        freqs=freqs,
        n_cycles=n_cycles,
        output="power",
        zero_mean=True,
        use_fft=True,
        verbose=False,
    )

    # Remove the artificial epoch and channel dimensions.
    power = ____

    # Convert power to dB.
    power_db = 10 * np.log10(power + 1e-12)

    return power_db
```

Blanks:
1. `power` — Compute power using MNE-Python
2. `power` — Remove the artificial epoch and channel dimensions.
