# Laquitaine Project — From Assumptions to a Fittable Model

Turns the 19 assumptions in [`laquitaine_research_questions.md`](laquitaine_research_questions.md) (§ Candidate model assumptions) into one mathematical model space. Punchline: the 19 are **not** 19 models. They are settings of a **single circular Bayesian observer** along two orthogonal axes — a *prior-dynamics core* and a *readout mode* — plus a small set of overlay parameters. Fit the axes, compare, and each research question (Q9, Q11, Q14, Q16, Q17) becomes a model-comparison result.

---

## 0. Notation (common scaffold)

Everything lives on the circle. Directions in radians, $\theta \in (-\pi, \pi]$; report in degrees for plots.

- Trial index $t$. Block index $b$. Stimulus direction $\theta_t$. Coherence $c_t \in \{0.06, 0.12, 0.24\}$. Block prior width condition $\sigma_b \in \{10,20,40,80\}°$, prior mean $\mu_0 = 225°$ (fixed). Feedback (true direction, shown post-response) $f_t = \theta_t$. Report $\hat\theta_t$. Reaction time $\mathrm{RT}_t$.
- Circular difference: $a \ominus b \equiv \operatorname{atan2}\big(\sin(a-b),\,\cos(a-b)\big)$.
- Von Mises: $\mathrm{VM}(\theta;\mu,\kappa) = \dfrac{e^{\kappa\cos(\theta-\mu)}}{2\pi I_0(\kappa)}$; concentration $\kappa \approx 1/\sigma^2$ (inverse circular variance).
- **VM product rule** (exact mean, standard concentration approx): $\mathrm{VM}(\mu_1,\kappa_1)\cdot\mathrm{VM}(\mu_2,\kappa_2)\ \propto\ \mathrm{VM}(\mu_{12},\kappa_{12})$ with the **vector (phasor) sum**
$$\kappa_{12}\,e^{i\mu_{12}} \;=\; \kappa_1 e^{i\mu_1} + \kappa_2 e^{i\mu_2}.$$

### The observer, in three lines

1. **Sensory likelihood** (coherence sets reliability): $\;m_t \mid \theta_t \sim \mathrm{VM}\big(\theta_t,\ \kappa_s(c_t)\big)$, $\kappa_s$ increasing in $c$.
2. **Prior belief** at trial $t$: $\;p_t(\theta) = \mathrm{VM}(\mu_t,\ \kappa_t)$ — belief state $(\mu_t,\kappa_t)$.
3. **Posterior** = phasor sum: $\;\kappa^*_t e^{i\mu^*_t} = \kappa_s(c_t)\,e^{i m_t} + \kappa_t\,e^{i\mu_t}$.

Prior weight $w_t = \dfrac{\kappa_t}{\kappa_s(c_t)+\kappa_t}$ — bias toward $\mu_t$ grows as coherence falls ($\kappa_s\downarrow$). That is the core Laquitaine effect, for free.

**Everything else is choosing (a) how $(\mu_t,\kappa_t)$ evolve, and (b) how the posterior becomes a report.** Those are the two axes.

---

## 1. Axis A — prior-dynamics core: one update rule, one dial

Belief mean update is a **circular leaky delta-rule**:
$$\boxed{\;\mu_{t+1} \;=\; \mu_t \;\oplus\; \alpha_t\,\delta_t,\qquad \delta_t = f_t \ominus \mu_t\;}$$
(prediction error $\delta_t$; $\oplus$ = wrapped rotation). **The entire M-a assumption family is just the learning-rate schedule $\alpha_t$:**

| Assumption | Mechanism | $\alpha_t$ |
|---|---|---|
| **A8** fixed / oracle | no learning | $0$ |
| **A1 / A7** online-Bayes / exp-weighted | leaky integrator | const $\alpha \in (0,1)$ |
| **A11** cumulative average | all past trials | $1/n_t$ (trials seen in block) |
| **A6** sliding window-5 | boxcar memory | equal weight on last 5 (FIR form) |
| **A2** static | learn then freeze | $\alpha$ for $t\le N$, else $0$ |
| **A3** SPE / error-modulated | Pearce–Hall-like | $\sigma\!\big(a_0 + \lambda\,|\delta_t|\big)$ |

A7 (exp-weight) and A1 (online serial) are **the same equation** — a leaky integrator is an exponentially-weighted mean. A11 is the same rule with $\alpha_t = 1/n_t$. So **8 assumptions collapse to one recursion with a scheduled gain.**

**Width belief (A14).** Second delta-rule on the variance, so the observer also *learns how wide the prior is*:
$$v_{t+1} = v_t + \alpha_\sigma\big(\delta_t^2 - v_t\big), \qquad \kappa_t = \phi(v_t)\ \big(\text{e.g. }\kappa_t \approx 1/v_t\big).$$
$v_t \to$ true block variance $\sigma_b^2$ over trials — exactly A14's "latent prior-variance approaching true width."

**Cores worth fitting (nested):**
- **C0** — fixed prior: $\alpha=0$, $\kappa_t=\kappa_b$. (A8) Baseline / null.
- **C1** — leaky-delta prior: const $\alpha$. (A1/A7; A11 as $1/n_t$; A6 as boxcar). $\alpha\to0$ recovers C0.
- **C2** — SPE + width-learning: $\alpha_t=\sigma(a_0+\lambda|\delta_t|)$, plus $v_t$ update. (A3, A14).
- **C3** — hierarchical / volatility: below.

---

## 2. Axis B — readout mode: integrate vs switch vs sample

How posterior $(\mu^*_t,\kappa^*_t)$ becomes report $\hat\theta_t$. **This axis is orthogonal to Axis A** — any core pairs with any readout.

- **R-int-mean** (classic Bayes): $\hat\theta_t = \mu^*_t + \epsilon_t$, report noise $\epsilon_t\sim\mathrm{VM}(0,\kappa_r)$. Unimodal.
- **R-int-sample** (sampling account, **Q9**): $\hat\theta_t \sim \mathrm{VM}(\mu^*_t,\ \kappa^*_t)$ — a *draw*, so trial variance carries the posterior width itself (extra variability vs PPC). PPC = R-int-mean; Sampling = R-int-sample. Same core, toggle distinguishes them.
- **R-switch** (**A4** switching observer): pick a source each trial,
$$z_t \sim \mathrm{Bern}(\pi_t),\quad \pi_t = \frac{\kappa_t}{\kappa_t + \kappa_s(c_t)},\qquad \hat\theta_t = \begin{cases}\mu_t + \epsilon_t & z_t=1\ (\text{prior})\\ m_t + \epsilon_t & z_t=0\ (\text{evidence})\end{cases}$$
Mixture, not product → **bimodal** report distribution. This is the only readout that produces the bimodality flagged in Q11/Q17.

**Switch trial-likelihood** (marginalize latent $m_t \sim \mathrm{VM}(\theta_t,\kappa_s)$), directly fittable:
$$p(\hat\theta_t) = \pi_t\,\mathrm{VM}(\hat\theta_t;\mu_t,\kappa_r) + (1-\pi_t)\,\mathrm{VM}(\hat\theta_t;\theta_t,\kappa_s(c_t)).$$

**A13 (perception = report)** is the modeling stance that makes all of the above legal: no separate decision stage, so estimate-distribution *shape* (unimodal vs bimodal) is the observer's computation, not a downstream choice. Under A13, R-int gives unimodal, R-switch gives bimodal — the shape is the test.

---

## 3. Overlay parameters (condition-dependence & transitions)

These modulate a core; they don't create new cores.

**Condition-dependent learning rate (A15 / A18 / A19).** One logistic link:
$$\alpha_t = \sigma\!\big(a_0 + a_\sigma\,\tilde\sigma_b + a_c\,\tilde c_t + a_{\sigma c}\,\tilde\sigma_b\tilde c_t + \lambda\,|\delta_t|\big),\qquad \tilde\cdot = \text{standardized}.$$
Directly testable claims:
- **A18** narrow → faster: $\;a_\sigma < 0$.
- **A19** evidence disturbs rate more in wide prior: $\;a_{\sigma c}\neq 0$ (interaction).
- **A15** same mechanism, different params: same functional form, refit per condition → test whether $\{a_\bullet\}$ are stable.

**Block-transition carryover (A16).** At each new block $b$:
$$\mu_{t_0(b)} = \eta\,\mu^{\text{end}}_{b-1} \,\oplus\, (1-\eta)\,\mu_0,\qquad \eta\in[0,1].$$
$\eta=0$ full reset, $\eta=1$ full carry.

**Timing / slow bias (A17).** Split into fast belief $\mu_t$ (updates at feedback) and a slow bias $b_t$ that only accrues with extended exposure and enters readout:
$$b_{t+1} = b_t + \alpha_b(\mu_t \ominus b_t),\quad \alpha_b \ll \alpha_t;\qquad \text{readout centered on } \mu^*_t \text{ pulled toward } b_t.$$

**Hierarchical / volatility core (A5, A12) — C3.** Two flavors:
- **A5 prior-identity:** latent $s_t\in\{\text{uniform},\text{peaked}\}$; infer $p(s_t\mid\text{data})$, integrate under the inferred prior. Mixture-of-priors.
- **A12 volatility:** hyperprior on how fast $\alpha$ may change (Behrens-style) — learns the learning rate. C2's SPE is the reduced, single-level version of this.

---

## 4. The consolidated model space (what to actually fit)

A **2-factor grid**: prior-dynamics core × readout. 19 assumptions → this table.

| | R-int-mean (PPC) | R-int-sample (sampling) | R-switch (bimodal) |
|---|---|---|---|
| **C0 fixed** (A8) | **M0** null Bayes, oracle prior | M0s | M0-sw |
| **C1 leaky-delta** (A1/A6/A7/A11) | **M1** adaptive-prior Bayes | M1s | M1-sw |
| **C2 SPE+width** (A3/A14) | **M2** | M2s | M2-sw |
| **C3 hierarchical** (A5/A12) | M3 | M3s | **M3-sw** |

Overlays (A15/18/19 condition-$\alpha$; A16 carryover $\eta$; A17 slow bias) switch on/off on top of any cell. RT (A10) is a **separate observation channel**, fit jointly or post-hoc:
$$\mathrm{RT}_t = r_0 - r_1\,\mathrm{Rel}_t + \varepsilon,\qquad \mathrm{Rel}_t = \kappa_s(c_t) + \kappa_t \ (\text{total reliability}).$$
A10's specific claim (RT slope over last 5 predicts next $|\delta|$): regress $|\delta_{t+1}|$ on $\text{slope}\big(\mathrm{RT}_{t-4:t}\big)$; sign/significance test.

### Parameter inventory (per subject)
- Sensory: $\kappa_s^{(1)},\kappa_s^{(2)},\kappa_s^{(3)}$ (one per coherence) — or $\kappa_s(c)=\kappa_0 c^{p}$ (2 params).
- Prior dynamics: $\alpha$ (C1) or $a_0,\lambda$ (C2) or $+\,a_\sigma,a_c,a_{\sigma c}$ (overlay); $\alpha_\sigma$ (width); $N$ (A2); $\eta$ (A16).
- Readout: $\kappa_r$ (report noise); mixture handled by $\pi_t$ (no free param — reliability-set).

### Trial likelihoods (for MLE/MAP)
- **R-int-mean:** $\hat\theta_t \sim \mathrm{VM}(\mu^*_t,\ \kappa_r)$.
- **R-int-sample:** $\hat\theta_t \sim \mathrm{VM}\big(\mu^*_t,\ (\,\kappa^{*-1}_t+\kappa_r^{-1}\,)^{-1}\big)$ (posterior draw ⊕ report noise).
- **R-switch:** the two-component mixture in §2.

---

## 5. Fitting, identifiability, and what each question gets answered

**Fit:** per-subject MAP over trials (block-aware; carry or reset $\mu$ at block edges per $\eta$). Optimizer: circular-aware gradient or CMA-ES; multi-start. Pool with hierarchical priors across subjects if needed for stability.

**Model comparison:** per-subject cross-validated log-likelihood (leave-blocks-out) + BIC; report win-frequency across the 12 subjects.

**Identifiability guards:**
- $\kappa_s$ vs $\kappa_r$ trade off → **anchor $\kappa_s$** on high-coherence, narrow-prior trials (near-veridical, prior-weight ≈ 0).
- Learning rate identifiable only from post-feedback sequential structure → weight fit toward **block-onset transients** (first ~N trials after a prior change).
- R-int-sample vs R-int-mean separated by **variance scaling with coherence**, not by mean bias (means coincide).

**Question → deliverable:**
- **Q9 (PPC vs sampling)** = R-int-mean vs R-int-sample within the winning core.
- **Q11 (switching)** = R-switch vs R-int (bimodality test) + estimate of $\pi_t$ dynamics.
- **Q14 (SPE fits learning)** = C2 vs C0/C1 fit to real learning curves.
- **Q15 (gradual vs abrupt)** = C1/C2 (smooth $\alpha$) vs a change-point core (step in $\mu_t$).
- **Q16/Q17 (source of overgeneralization / bimodality)** = does bias come from the **core** (prior dynamics, C*) or the **readout** (R-switch)? The 2-factor grid *is* the attribution test.
- **Q18, Q1b (serial / streak effects)** = sign and magnitude of $\alpha_t$ and its coherence dependence ($a_c$).
- **Q3b, Q4 (RT)** = the RT channel coefficients $r_1$, and the A10 slope test.

---

## 6. Minimal build order (fits the daily-doc / notebook workflow)

1. **M0** (fixed oracle prior + Bayes, R-int-mean) — sanity baseline; reuses circular-stats already in `laquitaine_human_errors.ipynb`.
2. **M1** (add leaky-delta $\alpha$) — first real learning model; directly extends the SPE cells in `laquitaine_motion_prior_learning.ipynb`.
3. **M1-sw** (swap readout to switching) — first bimodality test → Q11.
4. **M2** (SPE + width learning + condition-$\alpha$ overlay) → Q14/Q18/Q19.
5. **R-int-sample** toggle across the above → Q9.
6. **C3 / carryover / RT channel** last (highest lift) → Q5/Q16/Q17, Q3b/Q4.

Each step is one nested model added to the same fitting harness; comparison at every step answers one question.
