# Pseudocode twin — W2D2 Tutorial 2: `create_cos_sin`

- **Answer twin:** `../solutions/W2D2_Tutorial2_Solution_556248a1.py`
- **Reading view:** `../W2D2_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
def create_cos_sin(N, k):
    """
    Create the k-th cosine and sine basis vectors of length N.

    N: number of samples in your signal.
    k: frequency index or "wave number" (0 <= k < N).
    """

    n = np.arange(N)
    cos_k = ____
    sin_k = ____
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

    N = ____
    cos_k, sin_k = create_cos_sin(N, k)

    # Compute the real and imaginary parts of X[k] separately, each with a dot product
    real_part = ____
    imag_part = ____

    # Combine into a complex number, note the negative sign for the imaginary part
    X_k = ____
    return X_k

def compute_DFT(x):
    """
    Compute the Discrete Fourier Transform (DFT) of a signal x.

    x: input signal (1D array).
    """

    N = ____
    X = np.zeros(N, dtype=complex)

    # Loop over all frequency indices k
    for k in range(N):
        X[k] = ____

    return X
```

Blanks:
1. `cos_k` — fill in
2. `sin_k` — fill in
3. `N` — fill in
4. `real_part` — Compute the real and imaginary parts of X[k] separately, each with a dot product
5. `imag_part` — fill in
6. `X_k` — Combine into a complex number, note the negative sign for the imaginary part
7. `N` — fill in
8. `X[k]` — fill in
