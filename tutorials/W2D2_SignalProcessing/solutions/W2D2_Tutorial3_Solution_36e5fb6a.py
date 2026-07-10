
"""
1. The sharp edge is smoothed by the Gaussian kernel, which acts as a low-pass filter, removing the high-frequency components that create sharp boundaries (remember in Tutorial 1's reconstruction demo).
2. The 10 Hz sine did not change much because its frequency is within the "passband" of the Gaussian kernel, which allows low frequencies to pass through while attenuating higher frequencies (again, low-pass).
3. The noise is reduced and the underlying sine is exposed, because convolution with the Gaussian kernel performs a running average, essentially "smoothing out" random fluctuations in the signal.
""";