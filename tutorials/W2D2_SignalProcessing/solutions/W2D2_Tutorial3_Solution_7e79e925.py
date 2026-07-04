
def apply_system(x, h, dt):
    """Compute the LTI output y = x * h via the direct convolution sum."""
    N, M = len(x), len(h)
    y = np.zeros(N)

    for n in range(N):
        for m in range(min(n + 1, M)):

            # Multiply the input m steps back by the m-th kernel sample
            contribution = x[n - m] * h[m]
            # Accumulate into the output (don't forget the dt factor)
            y[n] = y[n] + dt * contribution
    return y