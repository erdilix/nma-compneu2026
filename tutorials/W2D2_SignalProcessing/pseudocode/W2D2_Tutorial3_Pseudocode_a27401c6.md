# Pseudocode twin — W2D2 Tutorial 3: 1. Design a low-pass Butterworth filter (cutoff 300 Hz, orde

- **Answer twin:** `../solutions/W2D2_Tutorial3_Solution_a27401c6.py`
- **Reading view:** `../W2D2_Tutorial3_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
b_lp, a_lp = signal.butter(4, 300.0, btype='low',  fs=ap_fs)
b_hp, a_hp = signal.butter(4, 300.0, btype='high', fs=ap_fs)
ibl_lfp_band = ____
ibl_spike_band = ____
```

Blanks:
1. `ibl_lfp_band` — fill in
2. `ibl_spike_band` — fill in
