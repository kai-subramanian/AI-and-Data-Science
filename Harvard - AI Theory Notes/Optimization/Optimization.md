# Optimization

Choosing the best option from a set of options.

### Local search 

Search algos that maintain a single node and searches by moving on to a neighbouring node.

### State - space landscape  

Used to either minimize or maximize a value - find global maximum or global minimum. **(Hill climbing algorithm)**

### Hill climbing variants

<table>
    <tr>
        <td>Variant</td>
        <td>Definition</td>
    </tr>
    <tr>
        <td>Steepest Ascent</td>
        <td>Choose highest valued neighbour</td>
    </tr>
    <tr>
        <td>Stochastic</td>
        <td>Choose randomly from higher-valued neighbours</td>
    </tr>
    <tr>
        <td>First choice</td>
        <td>Choose the first higher-valued neighbour</td>
    </tr>
    <tr>
        <td>Local beam search</td>
        <td>Choose the k highest-valued neighbours</td>
    </tr>
</table>


### Simulated Annealing 

* Early on, higher temperature : More likely to accept neighbours that are worse than the current state.

* Later on, lower temperature : Less likely likely to accept neighbours that are worse than the current state.

fn simulated(problem, max):
    current = initial state of problem
    for t=1 to max:
        T=TEMPERATURE(t)
        neighbour=random neighbour of current
        deltaE = how much better neighbour is than current
        if(deltaE>0):
            current=neighbour
        with probability e^(deltaE/t) set current=neighbour
    end for
end fn