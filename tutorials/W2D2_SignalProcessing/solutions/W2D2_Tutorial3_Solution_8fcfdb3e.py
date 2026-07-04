
fs = 1000.0
t, lfp = make_lfp_signal(fs=fs, duration=2.0)

orders = [2, 4, 8, 16]
band   = [4.0, 80.0]

fig, axes = plt.subplots(len(orders), 2, figsize=(13, 3.5 * len(orders)))
for i, order in enumerate(orders):

    b, a   = signal.butter(order, band, btype='band', fs=fs)
    x_filt = signal.filtfilt(b, a, lfp)
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