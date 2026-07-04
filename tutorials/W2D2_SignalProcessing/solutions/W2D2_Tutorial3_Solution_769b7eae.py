
# Signal and kernel from Exercise 1
# x_noisy is already defined (noisy 5 Hz sine, length n=500)
# gauss_kernel is already defined (length 51)

conv_length = len(x_noisy) + len(gauss_kernel) - 1  # length of full convolution

# 1. Time-domain convolution
y_time = np.convolve(x_noisy, gauss_kernel, mode='full')

# 2. Frequency-domain convolution
x_padded = np.zeros(conv_length)
x_padded[:len(x_noisy)] = x_noisy
h_padded = np.zeros(conv_length)
h_padded[:len(gauss_kernel)] = gauss_kernel
X_freq = np.fft.rfft(x_padded)
H_freq = np.fft.rfft(h_padded)
y_freq = np.real(np.fft.irfft(X_freq * H_freq))

max_diff = np.max(np.abs(y_time - y_freq))
print(f"Max difference: {max_diff:.2e}")