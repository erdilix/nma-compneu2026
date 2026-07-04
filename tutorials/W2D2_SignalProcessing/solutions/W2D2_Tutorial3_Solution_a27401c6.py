
b_lp, a_lp = signal.butter(4, 300.0, btype='low',  fs=ap_fs)
b_hp, a_hp = signal.butter(4, 300.0, btype='high', fs=ap_fs)
ibl_lfp_band   = signal.filtfilt(b_lp, a_lp, raw_ap)
ibl_spike_band = signal.filtfilt(b_hp, a_hp, raw_ap)