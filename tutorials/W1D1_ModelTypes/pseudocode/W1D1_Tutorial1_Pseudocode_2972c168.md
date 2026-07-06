# Pseudocode twin — W1D1 Tutorial 1, Exercise 1.2

- **Solves:** `compute_single_neuron_isis` — inter-spike intervals (ISIs) for one neuron
- **Answer twin:** `../solutions/W1D1_Tutorial1_Solution_2972c168.py`
- **Reading view:** `../W1D1_Tutorial1_pseudocode.md`

Idea: a neuron's ISIs are just the gaps between its consecutive spike times.

```text
FUNCTION compute_single_neuron_isis(spike_times, neuron_idx):
    single_neuron_spikes ← ____   # FILL: this neuron's spike-time array = spike_times[neuron_idx]
    isis                 ← ____   # FILL: consecutive differences of those times (np.diff)
    RETURN isis
```

Blanks to fill:
1. `single_neuron_spikes` — index into `spike_times` with `neuron_idx`.
2. `isis` — `np.diff(single_neuron_spikes)` (gap between each spike and the next).
