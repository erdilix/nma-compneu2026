
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
    s = A * np.sin(2 * np.pi * f * t + phi)
    return s