---
type: paper-synthesis
source: papers/sohn-narain-2021-neural-bayesian-inference.pdf
doi: 10.1016/j.conb.2021.09.008
ingested: 2026-07-13
status: synthesized
---

# Neural implementations of Bayesian inference — Sohn & Narain (2021)

*Zatsudan-socket ingest. Source PDF in `../../papers/sohn-narain-2021-neural-bayesian-inference.pdf` (open access, CC BY, downloaded from Erasmus EUR repository). Full text extracted with `pdftotext` — quotes/terms verbatim, no AI-guessed numbers. Cross-links point into the Zatsudan vault (`~/Documents/Zatsudan/wiki/`).*

**Cite:** Sohn, H., & Narain, D. (2021). Neural implementations of Bayesian inference. *Current Opinion in Neurobiology*, 70, 121–129. Themed issue: Computational Neuroscience (ed. Gjorgjieva & Fiete). Authors: Hansem Sohn (McGovern/MIT), Devika Narain (Erasmus MC).

## Why this is on-track

Review of *how the brain physically implements* Bayesian estimation — the exact `prior × likelihood → posterior → estimate` machinery behind the owner's NMA project [[nma-project-switching-observer]] and study reference [[bayesian-estimation-terms]]. Sits on the W3D2 Bayesian spine of [[neuromatch-comp-neuro]]. **Laquitaine & Gardner (the project paper) is cited here as ref [42]** — grouped under "limits of learning strategies," a caveat on when Bayes-optimal models hold. Companion socket doc: [[laquitaine_research_questions]] (many of those questions are model-mechanism questions this review frames).

## Core idea — two implementation classes

Behavior can look Bayesian (biased toward the prior mean, optimally so) while the *neural mechanism* differs. The paper splits all current implementation theories into two classes:

| | **Modular** (Fig 1b) | **Transform** (Fig 1c) |
|---|---|---|
| Encoding | prior, likelihood, posterior encoded **independently**, then combined | uncertain measurement **mapped directly** to estimate via latent process; prior embedded in connectivity/dynamics |
| Network shape | feedforward: `r(t=0)`=prior, `r(t=1)`=likelihood, sum → posterior | recurrent network/circuit; prior+likelihood entangled in weights & dynamics, readout gives estimate |
| Needs full distribution per trial? | **Yes** — supports trial-by-trial flexible uncertainty | **No** — implicit prior; cheaper, less flexible |
| Cost | resource-intensive, but rapid sequential re-inference | efficient when trial-wise flexibility not required |
| Best when | task demands constant monitoring of uncertainty | stable environmental statistics suffice |

This is a **many-to-many mapping problem**: many empirical findings, many models. The dichotomy is a proposed lens to interpret findings, not a settled fact.

## Modular class — the frameworks + evidence

**PPC (probabilistic population coding)** [refs 61–63]: population firing rates ≈ log-probability; linearly combining populations ≈ Bayes-optimal under Poisson-like variability. Prior often stored as **log of the prior**. Key modular tell: independent, flexibly-updatable representations of likelihood and prior.

Three nonhuman-primate studies cited as PPC-consistent:
- **Darlington, Beck & Lisberger 2018** [26] ⭐⭐ — smooth pursuit; **preparatory activity in frontal eye fields encodes the prior** before stimulus, pursuit activity encodes the Bayesian estimate. Prior *observable independently* before combining = the strongest modular signature.
- **Hou et al. 2019** [55] ⭐⭐ — LIP cortex, vestibular+visual heading; neurons integrate cues over time per linear PPC (Bayes-optimal).
- **Walker, Cotton, Ma & Tolias 2020** [56] ⭐⭐ — V1 orientation discrimination; **full likelihood function decodable** from V1 population; full-likelihood model beats fixed-uncertainty model trial-by-trial. Directly tests (and supports) the PPC assumption that full likelihoods are represented.

**Sampling codes** [51,67,68]: activity at a time = one sample from a distribution; neural variability *is* the uncertainty, not noise. Berkes/Orbán/Fiser (ferret V1) [21] — spontaneous activity ≈ samples from prior, evoked ≈ samples from posterior. Echeveste et al. 2020 [68] — excitatory-inhibitory recurrent circuit flexibly controls variability → biologically realistic sampling-based Bayes.

## Transform class — the frameworks + evidence

Input→output map: uncertain measurement → estimate through a nonlinear deterministic function, prior baked into the substrate. Two vantage points:

**(1) Population dynamics.** Sohn, Narain, Meirhaeghe & Jazayeri 2019 [28] ⭐⭐ ("Bayesian computation through cortical latent dynamics") — monkeys reproduce time intervals from short/long priors. Longer durations → more variable → Bayesian models predict **larger bias toward prior mean** (observed). Mechanism: DMFC (dorsomedial frontal cortex) population trajectories **warp into semicircular geometries**, one curvature per prior; linear projection onto the diameter **compresses states toward the prior mean** → biased readout. RNNs reproduced it and allowed causal perturbation (more compression → more bias). Prior+likelihood *entangled* → transform class. Aligned with **DDC (distributed distributional code)** [52,83] — uses statistical moments of the prior, linear readout of posterior mean, no full distribution needed.
- Egger et al. 2019 [14] ⭐⭐ — two measurements before reproduction; transform mappings **flexibly adapt** to changing likelihood/prior reliability (bias high on 1st measurement, drops on 2nd as uncertainty falls).
- Funamizu et al. 2016 [19] — rodent spatial navigation under sensory uncertainty; flexible sequential Bayesian correlates.

**(2) Synaptic connectivity.** Narain, Remington, De Zeeuw & Jazayeri 2018 [13] ⭐⭐ — **cerebellar TRACE model**: Purkinje-cell synaptic weights (parallel/climbing-fiber LTD/LTP) *learn and encode the prior* over intervals; incoming measurements via parallel fibers get transformed by embedded prior weights → Bayesian estimate. Output matches Bayes, diverges from MLE (lower RMSE). Ganguli & Simoncelli 2014 [53] ⭐⭐ efficient-coding theory — heterogeneous populations warp tuning curves to embed the prior. Note: cerebellum-timing [13] and visual-cortex [53] share mechanistic features despite different systems → hints at generalizable Bayesian mechanism.

## Synthesis & open divergence

- **Where is the prior?** Same finding (e.g. Darlington [26]) admits both readings: prior in *frontal synaptic weights* (transform) vs. prior *inherited from another area* as preparatory signal (modular). Is prior-reflecting preparatory activity the *driver* or an *epiphenomenon* over a synaptic latent transform? Unresolved — needs tools to observe synaptic-weight influence at scale + interareal inputs.
- **Possible unification:** brain may use **both, switching by task demand & local network compute budget**. Constant uncertainty-monitoring → modular; stable-statistics learning suffices → transform.
- **Dimensionality as the gauge** [ref 76, Gao & Ganguli]: modular (independent prior/likelihood/posterior) should occupy **higher-dimensional** state space than a transform net for a low-flexibility task. Open question: can one RNN be trained along a modular↔transform spectrum by target dimensionality? *(This is the sibling paper's whole topic — Jazayeri & Ostojic, S0959438821000933, on intrinsic vs embedding dimensionality; worth pairing.)*
- **Species gap:** circuit-interrogation toolkit lives in rodents, but nearly all cited studies are nonhuman primates — the reductionist unification needs cross-species + cross-scale (cell/circuit/population) work.

## Hooks for the owner's project

- **Bias toward prior mean under high uncertainty** = the central Laquitaine phenomenon, here given two candidate neural mechanisms. His behavioral estimates biased toward `prior_mean` 225° at low `motion_coherence` is the *behavioral* face of exactly this.
- **Switching vs integration** ([[nma-project-switching-observer]]): Laquitaine argues humans *switch* (bimodal estimates) rather than integrate. This review is about *integration* implementations — so the switching observer is a **third option / boundary case** the modular-vs-transform frame does not cover. That gap is a possible novelty angle: does a transform-class RNN naturally produce switching (bimodality) at low coherence? Ties to socket question **17** (hierarchical Bayesian bimodality) and **7/8** (attractor / DDM mechanism) in [[laquitaine_research_questions]].
- **RNN-as-model-organism** [28,68,70]: precedent for training an RNN to reproduce behavior + population dynamics, then perturbing it — directly reusable for a first-author mechanistic angle on the Laquitaine data.
- **Serial dependence / prior learning**: Akrami et al. 2018 [59] (PPC sensory-history) + the SPE learning notebook (`laquitaine_motion_prior_learning.ipynb`) connect to modular flexible-update claims.

## Related to pull next
- Jazayeri & Ostojic 2021, dimensionality review (S0959438821000933) — the "gauge" this paper leans on; sibling in same themed issue.
- Sohn, Narain, Meirhaeghe & Jazayeri 2019 [28] — the transform flagship, if going the population-dynamics route.
- Narain et al. 2018 [13] — cerebellar TRACE, if going the synaptic/learning route.
