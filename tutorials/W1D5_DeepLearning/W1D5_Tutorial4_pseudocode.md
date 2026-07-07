# W1D5 · Tutorial 4 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **4** code exercise(s).

---

## Exercise 4.1 — `__init__`

Blanked skeleton (fill the `____`):

```text
class ConvFC(nn.Module):
  """Deep network with one convolutional layer + one fully connected layer

  Attributes:
    conv (nn.Conv1d): convolutional layer
    dims (tuple): shape of convolutional layer output
    out_layer (nn.Linear): linear layer

  """

  def __init__(self, n_neurons, c_in=1, c_out=6, K=7, b=12*16,
               filters=None):
    """ initialize layer
    Args:
        c_in: number of input stimulus channels
        c_out: number of convolutional channels
        K: size of each convolutional filter
        h: number of stimulus bins, n_bins
    """
    super().__init__()
    self.conv = nn.Conv2d(c_in, c_out, kernel_size=K, padding=K//2, stride=1)
    self.dims = (c_out, b)  # dimensions of conv layer output
    M = np.prod(self.dims)  # number of hidden units

    self.out_layer = nn.Linear(M, n_neurons)

    # initialize weights
    if filters is not None:
      self.conv.weight = nn.Parameter(filters)
      self.conv.bias = nn.Parameter(torch.zeros((c_out,), dtype=torch.float32))

    nn.init.normal_(self.out_layer.weight, std=0.01)  # initialize weights to be small

  def forward(self, s):
    """ Predict neural responses to stimuli s

    Args:
        s (torch.Tensor): n_stimuli x c_in x h x w tensor with stimuli

    Returns:
        y (torch.Tensor): n_stimuli x n_neurons tensor with predicted neural responses

    """
    a = self.conv(s)  # output of convolutional layer
    a = a.view(-1, np.prod(self.dims))  # flatten each convolutional layer output into a vector
    y = ____
    return y


# Initialize network
n_neurons = resp_train.shape[1]
## Initialize with filters from Tutorial 2
example_filters = filters(out_channels=6, K=7)

net = ConvFC(n_neurons, filters = example_filters).to(device)

# Run GD on training set data
# ** this time we are also providing the test data to estimate the test loss
train_loss, test_loss = train(net, regularized_MSE_loss,
                              train_data=grating_stimuli.to(device), train_labels=resp_train.to(device),
                              test_data=grating_stimuli.to(device), test_labels=resp_test.to(device),
                              n_iter=200, learning_rate=2,
                              L2_penalty=5e-4, L1_penalty=1e-6)

# Visualize
with plt.xkcd():
  plot_training_curves(train_loss, test_loss)
```

**Blanks:** `y` (fill in)

→ twin `pseudocode/W1D5_Tutorial4_Pseudocode_5dffefa9.md` · answer `solutions/W1D5_Tutorial4_Solution_5dffefa9.py`

---

## Exercise 4.2 — `regularized_loss`

Blanked skeleton (fill the `____`):

```text
def regularized_loss(output, target, weights, L2_penalty=0, L1_penalty=0,
                     device='cpu'):
  """loss function with L2 and L1 regularization

  Args:
    output (torch.Tensor): output of network
    target (torch.Tensor): neural response network is trying to predict
    weights (torch.Tensor): linear layer weights from neurons to hidden units (net.in_layer.weight)
    L2_penalty : scaling factor of sum of squared weights
    L1_penalty : scaling factor for sum of absolute weights

  Returns:
    (torch.Tensor) mean-squared error with L1 and L2 penalties added

  """

  loss_fn = nn.NLLLoss()
  loss = loss_fn(output, target)

  L2 = L2_penalty * torch.square(weights).sum()
  L1 = L1_penalty * torch.abs(weights).sum()
  loss += L1 + L2

  return loss.to(device)


# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

n_classes = 20

# Initialize network
net = DeepNetSoftmax(n_neurons, 20, n_classes)  # use M=20 hidden units

# Here you can play with L2_penalty > 0, L1_penalty > 0
train_loss, test_loss, predicted_test_labels = decode_orientation(net, n_classes,
                                                                  regularized_loss,
                                                                  resp_train, stimuli_train,
                                                                  resp_test, stimuli_test,
                                                                  n_iter=1000,
                                                                  L2_penalty=1e-2,
                                                                  L1_penalty=5e-4,
                                                                  device=device)

# Plot results
with plt.xkcd():
  plot_decoded_results(train_loss, test_loss, stimuli_test, predicted_test_labels, n_classes)
```

→ twin `pseudocode/W1D5_Tutorial4_Pseudocode_9e7e87e5.md` · answer `solutions/W1D5_Tutorial4_Solution_9e7e87e5.py`

---

## Exercise 4.3 — `decode_orientation`

Blanked skeleton (fill the `____`):

```text
def decode_orientation(net, n_classes, loss_fn,
                       train_data, train_labels, test_data, test_labels,
                       n_iter=1000, L2_penalty=0, L1_penalty=0, device='cpu'):
  """ Initialize, train, and test deep network to decode binned orientation from neural responses

  Args:
    net (nn.Module): deep network to run
    n_classes (scalar): number of classes in which to bin orientation
    loss_fn (function): loss function to run
    train_data (torch.Tensor): n_train x n_neurons tensor with neural
      responses to train on
    train_labels (torch.Tensor): n_train x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians
    test_data (torch.Tensor): n_test x n_neurons tensor with neural
      responses to train on
    test_labels (torch.Tensor): n_test x 1 tensor with orientations of the
      stimuli corresponding to each row of train_data, in radians
    n_iter (int, optional): number of iterations to run optimization
    L2_penalty (float, optional): l2 penalty regularizer coefficient
    L1_penalty (float, optional): l1 penalty regularizer coefficient

  Returns:
    (list, torch.Tensor): training loss over iterations, n_test x 1 tensor with predicted orientations of the
      stimuli from decoding neural network
  """

  # Bin stimulus orientations in training set
  train_binned_labels = stimulus_class(train_labels, n_classes).to(device)
  test_binned_labels = stimulus_class(test_labels, n_classes).to(device)
  train_data = train_data.to(device)
  test_data = test_data.to(device)

  # Run GD on training set data, using learning rate of 0.1
  # (add optional arguments test_data and test_binned_labels!)
  train_loss, test_loss = train(net.to(device), loss_fn, train_data, train_binned_labels,
                                learning_rate=0.1, test_data=test_data,
                                test_labels=test_binned_labels, n_iter=n_iter,
                                L2_penalty=L2_penalty, L1_penalty=L1_penalty)

  # Decode neural responses in testing set data
  out = net(test_data).to(device)
  out_labels = np.argmax(out.detach().cpu(), axis=1)  # predicted classes

  frac_correct = (out_labels == test_binned_labels.cpu()).sum() / len(test_binned_labels)
  print(f'>>> fraction correct = {frac_correct:.3f}')

  return train_loss, test_loss, out_labels


# Set random seeds for reproducibility
np.random.seed(1)
torch.manual_seed(1)

n_classes = 20

# Initialize network
net = ____  # use M=20 hidden units

# Initialize built-in PyTorch negative log likelihood loss function
loss_fn = ____

# Train network and run it on test images
# this function uses the train function you wrote before
train_loss, test_loss, predicted_test_labels = decode_orientation(net, n_classes, loss_fn.to(device),
                                                                  resp_train, stimuli_train,
                                                                  resp_test, stimuli_test,
                                                                  device=device)

# Plot results
with plt.xkcd():
  plot_decoded_results(train_loss, test_loss, stimuli_test, predicted_test_labels, n_classes)
```

**Blanks:** `net` (Initialize network); `loss_fn` (Initialize built-in PyTorch negative log likelihood loss function)

→ twin `pseudocode/W1D5_Tutorial4_Pseudocode_e924146b.md` · answer `solutions/W1D5_Tutorial4_Solution_e924146b.py`

---

## Exercise 4.4 — first let's smooth the tuning curves resp_all to make sure w

Blanked skeleton (fill the `____`):

```text
from scipy.ndimage import gaussian_filter1d

# first let's smooth the tuning curves resp_all to make sure we get
# an accurate peak that isn't just noise
# resp_all is size (n_stimuli, n_neurons)
resp_smoothed = gaussian_filter1d(resp_all, 5, axis=0)
# resp_smoothed is size (n_stimuli, n_neurons)

# find position of max response for each neuron
# aka preferred orientation for each neuron
preferred_orientation = ____

# Resort W_in matrix by preferred orientation
isort = preferred_orientation.argsort()
W_in_sorted = W_in[:, isort]

# plot resorted W_in matrix
with plt.xkcd():
  visualize_weights(W_in_sorted, W_out)
```

**Blanks:** `preferred_orientation` (aka preferred orientation for each neuron)

→ twin `pseudocode/W1D5_Tutorial4_Pseudocode_f0b29255.md` · answer `solutions/W1D5_Tutorial4_Solution_f0b29255.py`

---
