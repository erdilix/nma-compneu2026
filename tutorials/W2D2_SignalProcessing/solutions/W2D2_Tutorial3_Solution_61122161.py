
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
    filtered = apply_filter(lfp, b, a, causal=False)
    return filtered, b, a