
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