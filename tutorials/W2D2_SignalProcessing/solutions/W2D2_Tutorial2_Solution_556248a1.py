
def create_cos_sin(N, k):
    """
    Create the k-th cosine and sine basis vectors of length N.

    N: number of samples in your signal.
    k: frequency index or "wave number" (0 <= k < N).
    """

    n = np.arange(N)
    cos_k = np.cos(2 * np.pi * k * n / N)
    sin_k = np.sin(2 * np.pi * k * n / N)
    return cos_k, sin_k

def dot_product(x, y):
    """
    Compute the dot product of two vectors x and y.
    Identical to np.dot(x,y) but implemented manually.

    x: first vector.
    y: second vector.
    """

    return np.sum(x * y)

def compute_Xk(x, k):
    """
    Compute the k-th DFT coefficient X[k] for a signal x.

    x: input signal (1D array).
    k: frequency index (0 <= k < N).
    """

    N = len(x)
    cos_k, sin_k = create_cos_sin(N, k)

    # Compute the real and imaginary parts of X[k] separately, each with a dot product
    real_part = dot_product(x, cos_k)
    imag_part = dot_product(x, sin_k)

    # Combine into a complex number, note the negative sign for the imaginary part
    X_k = real_part - 1j * imag_part
    return X_k

def compute_DFT(x):
    """
    Compute the Discrete Fourier Transform (DFT) of a signal x.

    x: input signal (1D array).
    """

    N = len(x)
    X = np.zeros(N, dtype=complex)

    # Loop over all frequency indices k
    for k in range(N):
        X[k] = compute_Xk(x, k)

    return X