# Uncertainty

Information that we have might not be entirely certain all the time. We study this topic to understand how a robot / autonomous agent can use such information.

### Probability

Denotes the possible states / worlds, w.
Probability is denoted by P(w).

Probability ranges from 0 to 1, inclusive. <b>0<=P(w)<=1</b>

Sum of individual probabilities = 1

Dice example,

P(1) = 1/6
P(2) = 1/6
P(3) = 1/6
P(4) = 1/6
P(5) = 1/6
P(6) = 1/6


Sum(P) = 1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 1

When you roll two die, the probabilites would become - 

<table>
    <tr>
        <td>Sum</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
    </tr>
    <tr>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
    <tr>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>
    </tr>
    <tr>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>
        <td>11</td>
    </tr>
    <tr>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>
        <td>11</td>
        <td>12</td>
    </tr>
</table>

We can see from the above table, that the probability of getting a 1 and 12 are very low (1 in 36) and the chances of getting a 7 are the highest (1 in 6).


We can observe that the P(sum) follows a normal distribution.

### Conditional Probability 

Degree of belief in a proposition, given some evidence about something that has been revealed.


### Independence

The knowledge that one events occurring does not affect the probability of the next event.

P(a^b) = P(a)P(b|a)

Intuition - What is probability of a and b happening ?, it is the likelihood of a happening, and GIVEN a happens, multiply it by likelihood of b happening.

But we know that a does not influence b as they are independent. Hence, it is just really

P(a^b) = P(a)P(b)

Given clouds in the morning, what is the probability of rain in the afternoon?

* 80% of rainy afternoons start with cloudy mornings.
* 40% of days have cloudy mornings
* 10% of days have rainy afternoons.

P(rain|clouds) = P(clouds|rain)P(rain) / P(clouds)
               = (0.8*0.1)/0.4
               =  0.08/0.4
               = <b>0.2</b>

### Inference

* Query x: Variable for which to compute distribution
* Evidence variables E: observed variables for event e
* Hidden variables Y: non-evidence, non-query variable.

Goal - Calculate P(X|e).

Nodes - 
Rain = {none, light, heavy}
Maintenance = {yes,no}
Train = {on_time, delayed}
Appointment = {attend,miss}

Calculate P(Appointment|light, no)


=aP(Appointment, light, no)
=a(P(Appointment, light, no, on_time) +P(Appointment, light, no, delayed))


### Markov Assumption

The assumption that the current state only depends on a finite fixed number of previous states.

<table>
    <tr>
        <td><b>Hidden State</b></td>
        <td><b>Observation</b></td>
    </tr>
    <tr>
        <td>Robot's position</td>
        <td>Robot's sensor data</td>
    </tr>
    <tr>
        <td>Words spoken</td>
        <td>Audio waveforms</td>
    </tr>
    <tr>
        <td>User engagement</td>
        <td>Website / <br>App analytics</td>
    </tr><tr>
        <td>Weather</td>
        <td>Umbrella</td>
    </tr>
</table>

### Hidden Markov Model

A Markov model for a system with hidden states that generate some observed event.

### Sensor Markov Assumption

the assumption that the evidence variable depends only on the corresponding state.

<table>
    <tr>
        <td><b>Task</b></td>
        <td><b>Definition</b></td>
    </tr>
    <tr>
        <td>Filtering</td>
        <td>
            Given observations from start till now, calculate the distribution for current state
        </td>
    </tr>
    <tr>
        <td>Prediction</td>
        <td>Given observations from start till now, calculate the distribution for a future state</td>
    </tr>
    <tr>
        <td>Smoothing</td>
        <td>Given observations from start till now, calculate the distribution for past state</td>
    </tr>
</table>

<hr>
