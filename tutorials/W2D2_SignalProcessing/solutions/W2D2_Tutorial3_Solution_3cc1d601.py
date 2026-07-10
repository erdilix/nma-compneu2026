"""
1. A narrower Gaussian has a wider frequency response, so it passes more high-frequency content and smooths less.
2. A boxcar or rectangular kernel in time has a sinc-shaped frequency response, with stronger side lobes.
3. A high-pass filter removes low frequencies and keeps high frequencies. The shape of such a filter kernel in time looks like a sharp transient (derivative-like) response, which removes slowly fluctuating components.
""";