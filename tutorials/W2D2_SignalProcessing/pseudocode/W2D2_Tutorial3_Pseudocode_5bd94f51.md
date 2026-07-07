# Pseudocode twin — W2D2 Tutorial 3: coding exercise

- **Answer twin:** `../solutions/W2D2_Tutorial3_Solution_5bd94f51.py`
- **Reading view:** `../W2D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

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

Blanks:
1. `ibl_theta` — fill in
