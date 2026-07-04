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

    f_alias = abs(signal_freq - round(signal_freq / sampling_rate) * sampling_rate)
    return f_alias