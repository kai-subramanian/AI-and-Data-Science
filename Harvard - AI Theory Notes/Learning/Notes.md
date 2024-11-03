# Learning

We don't give explicit instructions to the machine, we instead make the computer *learn* from patterns.

### Supervised Learning 

Given a dataset of input-output pairs, learn a function to map inputs to to outputs.

Subcategories - 
* Classification - Supervised learning task to function mapping output into discrete classes (examples - spam classification, fraud detection in bank notes, etc)

* Nearest neighbor classification - algorithm that, given an input, chooses the class of nearest data point to that input. k nearest neighbors considers k nearest neighbors to come to a conclusion (k can be arbitrary value, say 3 or 5)

* Linear Regression - Regression is the mappping of relation between an input and output variable.
Let x1=Humidity and x2=Pressure.
h(x1,h2) = Rain if w0 + w1x1 + w2x2 >=0, No rain otherwise.


Evaluate hypothesis - we need to minimize the loss function.
Loss function expresses how poorly our model performs.

### 0-1 loss function

L(actual, predicted) = 
&emsp; 0 if actual=predicted,
&emsp; 1 otherwise

### Maximum margin separator

A boundary that maximizes the distance between any of the data points.

### Reinforcement Learning

The agent receives a reward for good or desired action and receives a penalty for bad or undesirable action. Let the AI learn from the sequence of actions it makes.

The reward function can be mapped to maximize rewards and/or minimize the penalty.


### Markov decision process

Model for decision making, representing states, action and rewards.

Consists of - 
* Set of states S
* Set of actions ACTIONS(s)
* Transition Model
* Reward Function.


### Function Approximation

Approximating Q(s,a), often by a function that combines various features, rather than storing one value for every state-action pair.

### Unsupervised learning

Data without any additional feedback, we learn the patterns.

* Clustering - organizing objects into groups where similar objects are in same groups. Used in Genetics, Image recognition, etc.
* k-Means clutering - Used to cluster data based on repeatedly assining points to clusters and updating the cluster's centers.
* Unsupervised learning also includes dimensionality reduction.