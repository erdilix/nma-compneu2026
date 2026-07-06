# Pseudocode twin — W1D1 Tutorial 2, Exercise 2.2

- **Solves:** `lif_neuron_inh` — integrate-and-fire with leak + inhibition
- **Answer twin:** `../solutions/W1D1_Tutorial2_Solution_6bd84e18.py`
- **Reading view:** `../W1D1_Tutorial2_pseudocode.md`

Idea: extend the linear LIF — voltage now leaks (decays toward 0) and receives net input (excitatory minus inhibitory).

```text
FUNCTION lif_neuron_inh(n_steps, alpha, beta, exc_rate, inh_rate):
    exc         ← Poisson(exc_rate) samples of length n_steps
    inh         ← Poisson(inh_rate) samples of length n_steps
    v           ← zeros(n_steps)
    spike_times ← empty list

    FOR i FROM 1 TO n_steps-1:
        dv   ← ____            # FILL: leak + net drive = -beta*v[i-1] + alpha*(exc[i] - inh[i])
        v[i] ← v[i-1] + dv
        IF v[i] > 1:
            append i to spike_times
            v[i] ← 0           # reset
    RETURN v, spike_times
```

Blank to fill:
1. `dv` — `-beta * v[i-1] + alpha * (exc[i] - inh[i])`.
   - `-beta * v[i-1]` = leak (pulls voltage back toward 0).
   - `alpha * (exc[i] - inh[i])` = net excitatory−inhibitory drive.
