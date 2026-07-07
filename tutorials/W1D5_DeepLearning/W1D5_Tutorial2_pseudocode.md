# W1D5 · Tutorial 2 · pseudocode companion

Reading view: each code exercise as a fill-in-the-blank skeleton. Twins in `pseudocode/`, answers in `solutions/`.

This tutorial: **2** code exercise(s).

---

## Exercise 2.1 — Stimulus parameters

Blanked skeleton (fill the `____`):

```text
# Stimulus parameters
in_channels = 1  # how many input channels in our images
h = 48  # height of images
w = 64  # width of images

# Convolution layer parameters
K = 7  # filter size
out_channels = 6  # how many convolutional channels to have in our layer
example_filters = filters(out_channels, K)  # create filters to use

convout = np.zeros(0)  # assign convolutional activations to convout

# Initialize conv layer and add weights from function filters
# you need to specify :
# * the number of input channels c_in
# * the number of output channels c_out
# * the filter size K
convLayer = ConvolutionalLayer(c_in=in_channels, c_out=out_channels, K=K, filters=example_filters)

# Create stimuli (H_in, W_in)
orientations = [-90, -45, 0, 45, 90]
stimuli = torch.zeros((len(orientations), in_channels, h, w), dtype=torch.float32)
for i,ori in enumerate(orientations):
  stimuli[i, 0] = grating(ori)

convout = convLayer(stimuli)
convout = convout.detach()  # detach gradients

with plt.xkcd():
  plot_example_activations(stimuli, convout, channels=np.arange(0, out_channels))
```

→ twin `pseudocode/W1D5_Tutorial2_Pseudocode_41665ca7.md` · answer `solutions/W1D5_Tutorial2_Solution_41665ca7.py`

---

## Exercise 2.2 — Complete and uncomment

Blanked skeleton (fill the `____`):

```text
# get weights of conv layer in convLayer
weights = ____
print(weights.shape)  # can you identify what each of the dimensions are?

with plt.xkcd():
  plot_weights(weights, channels=np.arange(0, out_channels))
```

**Blanks:** `weights` (get weights of conv layer in convLayer)

→ twin `pseudocode/W1D5_Tutorial2_Pseudocode_8bc67a81.md` · answer `solutions/W1D5_Tutorial2_Solution_8bc67a81.py`

---
