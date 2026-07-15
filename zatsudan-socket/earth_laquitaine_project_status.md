# Laquitaine Bayesian-observer notebooks — project status

> Status board for the `earth_laquitaine*` notebook series in `projects/behavior_and_theory/`.
> Last updated 2026-07-15. Companions: [`earth_laquitaine_fit_flowchart.md`](earth_laquitaine_fit_flowchart.md) (math pipeline + Colab links), [`laquitaine_model_proposal.md`](laquitaine_model_proposal.md) (full model space), [`earth_laquitaine_gen_ext.md`](earth_laquitaine_gen_ext.md) (rung-1 twin).

## What this project is

A teaching ladder that builds the Laquitaine motion-direction Bayesian observer one property at a time, from a simple generative Gaussian toy up to a circular model fit to real human data. Inspired by [Laquitaine & Gardner, Neuron 2017](https://www.cell.com/neuron/fulltext/S0896-6273(17)31134-0). Method lectures: **W3D2 Bayesian Decisions (Tut 2 + Tut 3)** and **W1D2 Model Fitting**.

## Naming scheme

Each notebook is named by three properties:

```
earth_laquitaine[_circular]_<gen|fit>[_simple|_ext].ipynb
  _circular  present = von Mises (circle);  absent = Gaussian (line)
  gen | fit  generative (produce estimates) | fit to real data (NLL)
  _simple    static prior only;  _ext = online / warm-up / AIC comparison
```

## The ladder (intended learning path)

| rung | notebook | circular? · mode · scope | one-line |
|---|---|---|---|
| 1 | `earth_laquitaine_gen_ext.ipynb` | linear · gen · ext | Gaussian observer, generative; static + online + warm-up |
| 2 | `earth_laquitaine_fit_simple.ipynb` | linear · fit · simple | fit the static Gaussian to real data via analytic MAP likelihood |
| 3 | `earth_laquitaine_circular_gen_simple.ipynb` | circular · gen · simple | add the circle (von Mises, κ≈1/σ²); generative |
| 4 | `earth_laquitaine_circular_fit_ext.ipynb` | circular · fit · ext | full circular fit: static/online/warm-up + AIC, marginalized |
| — | `earth_laquitaine_fit_ext.ipynb` | linear · fit · ext | off-ladder **control**: the rung-4 machine without the circle |

## Coverage — the 8-slot property grid

3 binary axes → 8 slots. Filled: **5**. Empty: **3**.

| # | circular? · mode · scope | file | status |
|---|---|---|---|
| 1 | linear · gen · simple | — | ⚠️ only embedded as early steps in `gen_ext` |
| 2 | linear · gen · ext | `gen_ext` | ✅ |
| 3 | linear · fit · simple | `fit_simple` | ✅ |
| 4 | linear · fit · ext | `fit_ext` | ✅ |
| 5 | circular · gen · simple | `circular_gen_simple` | ✅ |
| 6 | circular · gen · ext | — | ❌ |
| 7 | circular · fit · simple | — | ❌ |
| 8 | circular · fit · ext | `circular_fit_ext` | ✅ |

## Gaps still open

### A. Grid gaps (structural)

- **Slot 7 — `circular_fit_simple`** *(highest value)*. Static-only circular fit; the clean bridge between rung 3 (circular generative) and rung 4 (circular extended). Closes the only real hole in the ladder.
- **Slot 6 — `circular_gen_ext`**. Circular generative with online / warm-up priors.
- **Slot 1 — `linear_gen_simple`** standalone. Currently exists only as the opening cells of `gen_ext`.

### B. Modeling gaps (rung-5 "more complex", none built)

Even `circular_fit_ext` still omits what the real study has:

- **Prior width should track the block.** `kappa_prior` is one fitted number; the experiment has 4 prior widths (10/20/40/80°) — width should follow `prior_std`.
- **Online model should update the width too**, not just the mean $\mu$.
- **Separate motor/report noise** distinct from sensory `kappa_llh`.
- **Readout choice:** MAP vs posterior-mean (squared-error loss) — Laquitaine compares both.
- **Group-level fit:** loop subjects × blocks, sum AIC (currently subject 1 / 80° block only).
- **Reaction times** — unused data column, part of the full model space.

## Shortest path to "complete"

Build **slot 7 `circular_fit_simple`** next — it finishes the contiguous ladder. Slots 6 and the section-B items are the genuine research frontier, not teaching rungs.

## Build / delivery status

| notebook | built | pushed to `github/main` | run-verified |
|---|---|---|---|
| `earth_laquitaine_gen_ext.ipynb` | ✅ | ✅ | ❌ |
| `earth_laquitaine_fit_simple.ipynb` | ✅ | ✅ | ❌ |
| `earth_laquitaine_circular_gen_simple.ipynb` | ✅ | ✅ | ❌ |
| `earth_laquitaine_circular_fit_ext.ipynb` | ✅ | ✅ | ❌ |
| `earth_laquitaine_fit_ext.ipynb` | ✅ | ✅ | ❌ |

⚠️ **None are run-verified** — no Python in the working shell; execute in the flake devshell to confirm plots and fits. Colab links for all five live in [`earth_laquitaine_fit_flowchart.md`](earth_laquitaine_fit_flowchart.md).
