# Neural Networks

Developed since 1940's.
Modelled based on human brain - 
it is made of neurons that are connected, and the pathways get activated.

### Artificial Neural Networks

Model Mathematical Function, from inputs to outputs based on the structure and parameters of the network.

Allows for learning the network's parameters.


### Gradient Descent 
* To train a neural network, we start with a random choice of weights.
* Repeat - 
Calculate the gradient based on all data points: direction that will lead to decreasing loss.
Update the weights based on gradient.

* Really expensive part of it - figuring the gradient based on all data points. We need to be able to train it faster.

### Stochastic Gradient Descent

* We choose the gradient randomly, based on one data point.

Tradeoff - we choose all the data vs choose a single data point.

### An effective tradeoff - Mini-batch Gradient Descent

* Starts with a random choice of weights
* Repeat - 
Calculate the gradient based on **one small batch** : direction that will lead to decreasing loss.
Update the weights based on gradient.

We add multiple layers to the neural network. The outputs can be modelled based on a probability value, and we can choose the output node with highest probability.

This is also useful in **reinforcement learning**, where the agent takes the action choice based on node with highest probability.

### Overfitting