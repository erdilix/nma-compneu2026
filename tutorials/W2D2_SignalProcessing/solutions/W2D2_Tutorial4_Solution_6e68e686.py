
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