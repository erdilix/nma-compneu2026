
y_pulse = np.convolve(x_pulse, gauss_kernel, mode='full')[:n]
y_sine = np.convolve(x_sine, gauss_kernel, mode='full')[:n]
y_noisy = np.convolve(x_noisy, gauss_kernel, mode='full')[:n]