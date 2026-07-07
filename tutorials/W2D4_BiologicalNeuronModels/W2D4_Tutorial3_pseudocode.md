# W2D4 · Tutorial 3 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **1** code exercise(s).

---

## Exercise 3.1 — Get default parameters

Blanked skeleton (fill the `____`):

```text
# Get default parameters
pars = default_pars(T=1000.)

# Add parameters
pars['gE_bar'] = 2.4    # [nS]
pars['VE'] = 0.         # [mV] excitatory reversal potential
pars['tau_syn_E'] = 2.  # [ms]
pars['gI_bar'] = 2.4    # [nS]
pars['VI'] = -80.       # [mV] inhibitory reversal potential
pars['tau_syn_I'] = 5.  # [ms]

# Generate presynaptic spike trains
pre_spike_train_ex = Poisson_generator(pars, rate=10, n=80)
pre_spike_train_in = Poisson_generator(pars, rate=10, n=20)

# Simulate conductance-based LIF model
v, rec_spikes, gE, gI = run_LIF_cond(pars, 0, pre_spike_train_ex,
                                     pre_spike_train_in)

# Show spikes more clearly by setting voltage high
dt, range_t = pars['dt'], pars['range_t']
if rec_spikes.size:
  sp_num = (rec_spikes / dt).astype(int) - 1
  v[sp_num] = 10   # draw nicer spikes

# Change the threshold
pars['V_th'] = 1e3

# Calculate FMP
v_fmp, _, _, _ = run_LIF_cond(pars, 0, pre_spike_train_ex, pre_spike_train_in)

with plt.xkcd():
  my_illus_LIFSYN(pars, v_fmp, v)
```

→ twin `pseudocode/W2D4_Tutorial3_Pseudocode_1248eed5.md` · answer `solutions/W2D4_Tutorial3_Solution_1248eed5.py`

---
