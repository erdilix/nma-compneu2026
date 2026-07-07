# W2D2 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 4.1 — `compute_stft_spectrogram`

Blanked skeleton (fill the `____`):

```text
def compute_stft_spectrogram(
    x,
    fs,
    nperseg=STFT_NPERSEG,
    noverlap=STFT_NOVERLAP,
    window=STFT_WINDOW,
):
    """
    Compute a short-time Fourier transform spectrogram using scipy.signal.stft.

    Args:
      x (numpy array of floats): time-domain signal
      fs (float): sampling frequency in Hz
      nperseg (int): number of samples in each STFT window
      noverlap (int): number of samples shared by neighboring windows
      window (str): window type passed to scipy.signal.stft

    Returns:
      freqs (numpy array of floats): STFT frequency bins in Hz
      times (numpy array of floats): STFT time bins in seconds
      power_db (numpy array of floats): STFT power in dB, with shape
                                       (n_frequencies, n_times)
    """

    # Compute the complex STFT coefficients
    freqs, times, Z = signal.stft(x, fs=fs, window=window, nperseg=nperseg, noverlap=noverlap)

    # Convert complex coefficients to power in dB.
    power = np.abs(Z) ** 2
    power_db = 10 * np.log10(power + 1e-12)

    return freqs, times, power_db
```

→ twin `pseudocode/W2D2_Tutorial4_Pseudocode_6e68e686.md` · answer `solutions/W2D2_Tutorial4_Solution_6e68e686.py`

---

## Exercise 4.2 — `compute_morlet_power`

Blanked skeleton (fill the `____`):

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

**Blanks:** `power` (Compute power using MNE-Python); `power` (Remove the artificial epoch and channel dimensions.)

→ twin `pseudocode/W2D2_Tutorial4_Pseudocode_d43fdaef.md` · answer `solutions/W2D2_Tutorial4_Solution_d43fdaef.py`

---
