"""
1. Yes the output is scaled by exactly 3x due to linearity, and the shape is not changed.
2. The output is simply shifted: LTI means the system's response is always the same, just delayed by the same amount as the input shift.
3. Any system that has a nonlinear response. For example, a neuron accumulates synaptic input (approximately) linearly below threshold, but has a nonlinear response in the action potential when threshold is reached.
""";