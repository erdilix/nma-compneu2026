# W1D1 · Tutorial 2 — "How" Models (LIF neuron) · pseudocode companion

Reading view: each coding exercise's blanked code cell + a fill-in-the-blank pseudocode box. Twins in `pseudocode/`, answers in `solutions/`.

Tutorial 2 has **2** coding exercises (the other two `solutions/` files are text "Think!" answers).

---

## Exercise 2.1 — `lif_neuron` (compute $dV_m$)

Original code cell:

```python
def lif_neuron(n_steps=1000, alpha=0.01, rate=10):
  """Simulate a linear integrate-and-fire neuron."""
  exc = stats.poisson(rate).rvs(n_steps)   # precomputed Poisson input
  v = np.zeros(n_steps)
  spike_times = []
  for i in range(1, n_steps):
    dv = ...
    v[i] = v[i-1] + dv
    if v[i] > 1:
      spike_times.append(i)
      v[i] = 0
  return v, spike_times
```

**Pseudocode (fill the `____`):**

```text
FUNCTION lif_neuron(n_steps, alpha, rate):
    exc ← Poisson(rate) samples, length n_steps
    v ← zeros(n_steps); spike_times ← []
    FOR i FROM 1 TO n_steps-1:
        dv   ← ____            # input drive this step = alpha * exc[i]
        v[i] ← v[i-1] + dv
        IF v[i] > 1:           # threshold → spike + reset
            append i to spike_times; v[i] ← 0
    RETURN v, spike_times
```

→ twin `pseudocode/W1D1_Tutorial2_Pseudocode_9e5a4843.md` · answer `solutions/W1D1_Tutorial2_Solution_9e5a4843.py`

---

## Exercise 2.2 — `lif_neuron_inh` (leak + inhibition)

Original code cell:

```python
def lif_neuron_inh(n_steps=1000, alpha=0.5, beta=0.1, exc_rate=10, inh_rate=10):
  """LIF neuron with excitatory and inhibitory inputs."""
  exc = stats.poisson(exc_rate).rvs(n_steps)
  inh = stats.poisson(inh_rate).rvs(n_steps)
  v = np.zeros(n_steps)
  spike_times = []
  for i in range(1, n_steps):
    dv = ...
    v[i] = v[i-1] + dv
    if v[i] > 1:
      spike_times.append(i)
      v[i] = 0
  return v, spike_times
```

**Pseudocode (fill the `____`):**

```text
FUNCTION lif_neuron_inh(n_steps, alpha, beta, exc_rate, inh_rate):
    exc ← Poisson(exc_rate) samples; inh ← Poisson(inh_rate) samples
    v ← zeros; spike_times ← []
    FOR i FROM 1 TO n_steps-1:
        dv   ← ____            # leak + net drive = -beta*v[i-1] + alpha*(exc[i] - inh[i])
        v[i] ← v[i-1] + dv
        IF v[i] > 1: append i; v[i] ← 0
    RETURN v, spike_times
```

Note vs 2.1: `-beta*v[i-1]` adds leak; input becomes net `(exc − inh)`.

→ twin `pseudocode/W1D1_Tutorial2_Pseudocode_6bd84e18.md` · answer `solutions/W1D1_Tutorial2_Solution_6bd84e18.py`
