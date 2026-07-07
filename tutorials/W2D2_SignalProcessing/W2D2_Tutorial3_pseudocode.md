# W2D2 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **7** code exercise(s).

---

## Exercise 3.1 — 1. Convolve x_pulse with gauss_kernel using np.convolve(...,

Blanked skeleton (fill the `____`):

```text
y_pulse = ____
y_sine = ____
y_noisy = ____
```

**Blanks:** `y_pulse` (fill in); `y_sine` (fill in); `y_noisy` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_4bac5bcb.md` · answer `solutions/W2D2_Tutorial3_Solution_4bac5bcb.py`

---

## Exercise 3.2 — coding exercise

Blanked skeleton (fill the `____`):

```text
b_th, a_th = signal.butter(2, [4.0, 8.0], btype='band', fs=ap_fs)
ibl_theta = ____

from scipy.signal import welch
freqs_raw, psd_raw   = welch(raw_ap,       fs=ap_fs, nperseg=int(ap_fs))
freqs_lfp, psd_lfp   = welch(ibl_lfp_band, fs=ap_fs, nperseg=int(ap_fs))
freqs_th,  psd_theta = welch(ibl_theta,    fs=ap_fs, nperseg=int(ap_fs))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(t_ap, ibl_lfp_band, color='C0', lw=0.8, label='LFP band', alpha=0.7)
axes[0].plot(t_ap, ibl_theta,    color='C2', lw=1.5, label='Theta (4–8 Hz)')
axes[0].set_xlabel('Time (s)'); axes[0].set_ylabel('Amplitude (µV)')
axes[0].set_title('Theta extracted from LFP band'); axes[0].legend()

axes[1].semilogy(freqs_raw, psd_raw,   color='C4', lw=0.8, label='Raw',       alpha=0.6)
axes[1].semilogy(freqs_lfp, psd_lfp,   color='C0', lw=1.2, label='LFP band')
axes[1].semilogy(freqs_th,  psd_theta, color='C2', lw=1.5, label='Theta band')
for lo, hi, name in [(4,8,'θ'),(30,80,'γ')]:
    axes[1].axvspan(lo, hi, alpha=0.12, color='gray', label=name)
axes[1].set_xlim([0, 200]); axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylim([1e-6, 10]);
axes[1].set_ylabel('PSD (µV²/Hz)'); axes[1].set_title('Power Spectra')
axes[1].legend(fontsize=8)
plt.suptitle(f'IBL Ch {BEST_CH} - Theta Extraction (Solution)', fontweight='bold')
plt.tight_layout(); plt.show()
```

**Blanks:** `ibl_theta` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_5bd94f51.md` · answer `solutions/W2D2_Tutorial3_Solution_5bd94f51.py`

---

## Exercise 3.3 — `filter_lfp`

Blanked skeleton (fill the `____`):

```text
def filter_lfp(lfp, fs, filter_type, freqs):
    """
    Design and apply a 4th-order Butterworth filter.

    Parameters
    ----------
    lfp         : 1-D array
    fs          : float, sampling rate in Hz
    filter_type : str, 'low', 'high', or 'band'
    freqs       : float or [float, float]

    Returns
    -------
    filtered, b, a
    """

    b, a = signal.butter(4, freqs, btype=filter_type, fs=fs)
    filtered = ____
    return filtered, b, a
```

**Blanks:** `filtered` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_61122161.md` · answer `solutions/W2D2_Tutorial3_Solution_61122161.py`

---

## Exercise 3.4 — Signal and kernel from Exercise 1

Blanked skeleton (fill the `____`):

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

**Blanks:** `y_time` (1. Time-domain convolution); `X_freq` (fill in); `H_freq` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_769b7eae.md` · answer `solutions/W2D2_Tutorial3_Solution_769b7eae.py`

---

## Exercise 3.5 — `apply_system`

Blanked skeleton (fill the `____`):

```text
def apply_system(x, h, dt):
    """Compute the LTI output y = x * h via the direct convolution sum."""
    N, M = len(x), len(h)
    y = np.zeros(N)

    for n in range(N):
        for m in range(min(n + 1, M)):

            # Multiply the input m steps back by the m-th kernel sample
            contribution = ____
            # Accumulate into the output (don't forget the dt factor)
            y[n] = ____
    return y
```

**Blanks:** `contribution` (Multiply the input m steps back by the m-th kernel sample); `y[n]` (Accumulate into the output (don't forget the dt factor))

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_7e79e925.md` · answer `solutions/W2D2_Tutorial3_Solution_7e79e925.py`

---

## Exercise 3.6 — and compute the amplitude response with freqz.

Blanked skeleton (fill the `____`):

```text
fs = 1000.0
t, lfp = make_lfp_signal(fs=fs, duration=2.0)

orders = [2, 4, 8, 16]
band   = [4.0, 80.0]

fig, axes = plt.subplots(len(orders), 2, figsize=(13, 3.5 * len(orders)))
for i, order in enumerate(orders):

    b, a   = signal.butter(order, band, btype='band', fs=fs)
    x_filt = ____
    w, h   = signal.freqz(b, a, worN=4000, fs=fs)

    axes[i,0].plot(t*1000, lfp,    color='lightgray', lw=0.6, label='Raw')
    axes[i,0].plot(t*1000, x_filt, color='C0',        lw=1.2, label=f'Order {order}')
    axes[i,0].set_xlim([400,700]); axes[i,0].legend(fontsize=8)
    axes[i,0].set_xlabel("Time (ms)"); axes[i,0].set_title(f"Order {order} - Time")
    axes[i,1].plot(w, 20*np.log10(np.abs(h)+1e-10), color='C1')
    axes[i,1].axhline(-3, color='gray', ls='--', alpha=0.5)
    axes[i,1].set_xlabel("Frequency (Hz)"); axes[i,1].set_xlim([0,fs/2])
    axes[i,1].set_title(f"Order {order} - Amplitude Response")

plt.suptitle("Filter Order: Sharpness vs. Ringing (Solution)", fontsize=13, fontweight='bold')
plt.tight_layout(); plt.show()
```

**Blanks:** `x_filt` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_8fcfdb3e.md` · answer `solutions/W2D2_Tutorial3_Solution_8fcfdb3e.py`

---

## Exercise 3.7 — 1. Design a low-pass Butterworth filter (cutoff 300 Hz, orde

Blanked skeleton (fill the `____`):

```text
b_lp, a_lp = signal.butter(4, 300.0, btype='low',  fs=ap_fs)
b_hp, a_hp = signal.butter(4, 300.0, btype='high', fs=ap_fs)
ibl_lfp_band = ____
ibl_spike_band = ____
```

**Blanks:** `ibl_lfp_band` (fill in); `ibl_spike_band` (fill in)

→ twin `pseudocode/W2D2_Tutorial3_Pseudocode_a27401c6.md` · answer `solutions/W2D2_Tutorial3_Solution_a27401c6.py`

---
