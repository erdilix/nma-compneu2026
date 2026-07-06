# Pseudocode twin — W1D1 Tutorial 1, Exercise 1.1

- **Solves:** median spike count + histogram with median/mean markers
- **Answer twin:** `../solutions/W1D1_Tutorial1_Solution_9af91fe0.py`
- **Reading view:** `../W1D1_Tutorial1_pseudocode.md`

Idea: the spike-count distribution is skewed, so contrast the median (typical neuron) against the mean.

```text
median_spike_count ← ____          # FILL: median across neurons (np.median of total_spikes_per_neuron)

PLOT histogram(total_spikes_per_neuron, bins=50, stepfilled)
DRAW vertical line at ____ , color=limegreen, label="Median neuron"   # FILL: median_spike_count
DRAW vertical line at mean_spike_count , color=orange, label="Mean neuron"
LABEL x="Total spikes per neuron", y="Number of neurons"
SHOW legend
```

Blanks to fill:
1. `median_spike_count` — `np.median(total_spikes_per_neuron)`.
2. median `axvline` position — pass `median_spike_count`.
