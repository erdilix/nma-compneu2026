# W1D1 · Tutorial 1 — Neural Rate Coding · pseudocode companion

Reading view: each coding exercise's original (blanked) code cell, followed by a fill-in-the-blank pseudocode box. Twin files (lookup from the solutions side) live in `pseudocode/`; the filled answers live in `solutions/`.

Tutorial 1 has **2** coding exercises (the other two `solutions/` files here are text "Think!" answers, no code).

---

## Exercise 1.1 — median spike count + histogram

Original code cell (from `student/W1D1_Tutorial1.ipynb`):

```python
# Compute median spike count
median_spike_count = ...  # Hint: Try the function np.median

# Visualize median, mean, and histogram
plt.hist(..., bins=50, histtype="stepfilled")
plt.axvline(..., color="limegreen", label="Median neuron")
plt.axvline(mean_spike_count, color="orange", label="Mean neuron")
plt.xlabel("Total spikes per neuron")
plt.ylabel("Number of neurons")
plt.legend()
```

**Pseudocode (fill the `____`):**

```text
median_spike_count ← ____          # median across neurons (np.median of total_spikes_per_neuron)

PLOT histogram(total_spikes_per_neuron, bins=50, stepfilled)
DRAW vertical line at ____ , color=limegreen, label="Median neuron"   # median_spike_count
DRAW vertical line at mean_spike_count , color=orange, label="Mean neuron"
LABEL x="Total spikes per neuron", y="Number of neurons"; SHOW legend
```

→ twin `pseudocode/W1D1_Tutorial1_Pseudocode_9af91fe0.md` · answer `solutions/W1D1_Tutorial1_Solution_9af91fe0.py`

---

## Exercise 1.2 — `compute_single_neuron_isis`

Original code cell:

```python
def compute_single_neuron_isis(spike_times, neuron_idx):
  """Compute a vector of ISIs for a single neuron given spike times."""
  # Extract the spike times for the specified neuron
  single_neuron_spikes = ...
  # Compute the ISIs for this set of spikes (Hint: np.diff)
  isis = ...
  return isis
```

**Pseudocode (fill the `____`):**

```text
FUNCTION compute_single_neuron_isis(spike_times, neuron_idx):
    single_neuron_spikes ← ____   # this neuron's spike-time array = spike_times[neuron_idx]
    isis                 ← ____   # consecutive differences of those times (np.diff)
    RETURN isis
```

→ twin `pseudocode/W1D1_Tutorial1_Pseudocode_2972c168.md` · answer `solutions/W1D1_Tutorial1_Solution_2972c168.py`
