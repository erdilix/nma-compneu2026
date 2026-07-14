def compute_aliased_frequency(signal_freq, sampling_freq):
    """Compute the apparent frequency after aliasing.

    Parameters
    ----------
    signal_freq   : float, true signal frequency (Hz)
    sampling_freq : float, sampling frequency (Hz)

    Returns
    -------
    float : apparent frequency (Hz). Returns signal_freq if no aliasing.
    """

    if sampling_freq >= 2 * signal_freq:
        # above Nyquist — no aliasing
        return signal_freq

    f_alias = abs(signal_freq - round(signal_freq / sampling_freq) * sampling_freq)
    return f_alias