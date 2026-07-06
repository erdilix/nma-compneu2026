# Pseudocode twin — W1D1 Tutorial 2, Exercise 2.1

- **Solves:** `lif_neuron` — linear integrate-and-fire neuron, compute $dV_m$
- **Answer twin:** `../solutions/W1D1_Tutorial2_Solution_9e5a4843.py`
- **Reading view:** `../W1D1_Tutorial2_pseudocode.md`

Idea: each step the membrane voltage rises by the scaled excitatory input; crossing threshold 1 fires a spike and resets.

```text
FUNCTION lif_neuron(n_steps, alpha, rate):
    exc         ← Poisson(rate) samples of length n_steps
    v           ← zeros(n_steps)
    spike_times ← empty list

    FOR i FROM 1 TO n_steps-1:
        dv   ← ____            # FILL: input drive this step = alpha * exc[i]
        v[i] ← v[i-1] + dv
        IF v[i] > 1:           # threshold reached
            append i to spike_times
            v[i] ← 0           # reset
    RETURN v, spike_times
```

Blank to fill:
1. `dv` — `alpha * exc[i]` (voltage increment from this step's excitatory count).
