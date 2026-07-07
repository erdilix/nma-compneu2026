# Pseudocode twin — W2D2 Tutorial 3: Signal and kernel from Exercise 1

- **Answer twin:** `../solutions/W2D2_Tutorial3_Solution_769b7eae.py`
- **Reading view:** `../W2D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
# Signal and kernel from Exercise 1
# x_noisy is already defined (noisy 5 Hz sine, length n=500)
# gauss_kernel is already defined (length 51)

conv_length = len(x_noisy) + len(gauss_kernel) - 1  # length of full convolution

# 1. Time-domain convolution
y_time = ____

# 2. Frequency-domain convolution
x_padded = np.zeros(conv_length)
x_padded[:len(x_noisy)] = x_noisy
h_padded = np.zeros(conv_length)
h_padded[:len(gauss_kernel)] = gauss_kernel
X_freq = ____
H_freq = ____
y_freq = np.real(np.fft.irfft(X_freq * H_freq))

max_diff = np.max(np.abs(y_time - y_freq))
print(f"Max difference: {max_diff:.2e}")
```

Blanks:
1. `y_time` — 1. Time-domain convolution
2. `X_freq` — fill in
3. `H_freq` — fill in
