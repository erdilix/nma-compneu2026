# W3D3 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 2.1 — `markov_forward`

Blanked skeleton (fill the `____`):

```text
def markov_forward(p0, D):
  """Calculate the forward predictive distribution in a discrete Markov chain

  Args:
    p0 (numpy vector): a discrete probability vector
    D (numpy matrix): the transition matrix, D[i,j] means the prob. to
    switch FROM i TO j

  Returns:
    p1 (numpy vector): the predictive probabilities in next time step
  """

  # Calculate predictive probabilities (prior)
  p1 = ____

  return p1

def one_step_update(model, posterior_tm1, M_t):
  """Given a HMM model, calculate the one-time-step updates to the posterior.
  Args:
    model (GaussianHMM1D instance): the HMM
    posterior_tm1 (numpy vector): Posterior at `t-1`
    M_t (numpy array): measurements at `t`
    Returns:
    posterior_t (numpy array): Posterior at `t`
  """
  # Calculate predictive probabilities (prior)
  prediction = markov_forward(posterior_tm1, model.transmat)

  # Get the likelihood
  likelihood = compute_likelihood(model, M_t)

  # Calculate posterior
  posterior_t = ____

  # Normalize
  posterior_t /= np.sum(posterior_t)

  return prediction, likelihood, posterior_t


# Set random seed
np.random.seed(12)

# Set parameters
switch_prob = 0.4
noise_level = .4
t = 75

# Create and sample from model
model = create_HMM(switch_prob = switch_prob,
                    noise_level = noise_level,
                    startprob=[0.5, 0.5])

measurements, states = sample(model, nstep)

# Infer state sequence
predictive_probs, likelihoods, posterior_probs = simulate_forward_inference(model, nstep,
                                                            measurements)
states_inferred = np.asarray(posterior_probs[:,0] <= 0.5, dtype=int)

# Visualize
with plt.xkcd():
  plot_forward_inference(
        model, states, measurements, states_inferred,
        predictive_probs, likelihoods, posterior_probs,t=t, flag_m = 0
      )
```

**Blanks:** `p1` (Calculate predictive probabilities (prior)); `posterior_t` (Calculate posterior)

→ twin `pseudocode/W3D3_Tutorial2_Pseudocode_69ce2879.md` · answer `solutions/W3D3_Tutorial2_Solution_69ce2879.py`

---

## Exercise 2.2 — `create_HMM`

Blanked skeleton (fill the `____`):

```text
def create_HMM(switch_prob=0.1, noise_level=1e-1, startprob=[1.0, 0.0]):
  """Create an HMM with binary state variable and 1D Gaussian measurements
  The probability to switch to the other state is `switch_prob`. Two
  measurement models have mean 1.0 and -1.0 respectively. `noise_level`
  specifies the standard deviation of the measurement models.

  Args:
      switch_prob (float): probability to jump to the other state
      noise_level (float): standard deviation of measurement models. Same for
      two components

  Returns:
      model (GaussianHMM instance): the described HMM
  """

  n_components = 2

  startprob_vec = np.asarray(startprob)

  # STEP 1: Transition probabilities
  transmat_mat = ____ # # np.array([[...], [...]])

  # STEP 2: Measurement probabilities

  # Mean measurements for each state
  means_vec = ____

  # Noise for each state
  vars_vec = np.ones(2) * noise_level * noise_level

  # Initialize model
  model = GaussianHMM1D(
    startprob = startprob_vec,
    transmat = transmat_mat,
    means = means_vec,
    vars = vars_vec,
    n_components = n_components
  )

  return model


def sample(model, T):
  """Generate samples from the given HMM

  Args:
    model (GaussianHMM1D): the HMM with Gaussian measurement
    T (int): number of time steps to sample

  Returns:
    M (numpy vector): the series of measurements
    S (numpy vector): the series of latent states

  """
  # Initialize S and M
  S = np.zeros((T,),dtype=int)
  M = np.zeros((T,))

  # Calculate initial state
  S[0] = np.random.choice([0,1],p=model.startprob)

  # Latent state at time `t` depends on `t-1` and the corresponding transition probabilities to other states
  for t in range(1,T):

    # STEP 3: Get vector of probabilities for all possible `S[t]` given a particular `S[t-1]`
    transition_vector = ____

    # Calculate latent state at time `t`
    S[t] = np.random.choice([0,1],p=transition_vector)

  # Calculate measurements conditioned on the latent states
  # Since measurements are independent of each other given the latent states, we could calculate them as a batch
  means = model.means[S]
  scales = np.sqrt(model.vars[S])
  M = np.random.normal(loc=means, scale=scales, size=(T,))

  return M, S


# Set random seed
np.random.seed(101)

# Set parameters of HMM
T = 100
switch_prob = 0.1
noise_level = 2.0

# Create HMM
model = create_HMM(switch_prob=switch_prob, noise_level=noise_level)

# Sample from HMM
M, S = sample(model,T)
assert M.shape==(T,)
assert S.shape==(T,)

# Print values
print(M[:5])
print(S[:5])
```

**Blanks:** `transmat_mat` (STEP 1: Transition probabilities); `means_vec` (Mean measurements for each state); `transition_vector` (STEP 3: Get vector of probabilities for all possible `S[t]` given a particular `S[t-1]`)

→ twin `pseudocode/W3D3_Tutorial2_Pseudocode_9035e19a.md` · answer `solutions/W3D3_Tutorial2_Solution_9035e19a.py`

---
