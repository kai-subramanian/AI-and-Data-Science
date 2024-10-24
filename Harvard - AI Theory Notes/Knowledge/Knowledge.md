Knowledge - Representation of Information.

Lot of intelligence is based on knowledge. We reason about and conclude based on knowledge.

Knowledge based agents
- agents that reason by and operate on internal representation of knowledge.

An example - 
- If it didn't rain, Harry visited Hagrid today.
- Harry visited Hagrid or Dumbledore today, but not both.
- Harry visted Dumbledore today.

<b>Conclusion - Harry did not visit Hagrid today. It did rain today.</b>

Propositional logic - 

P Q R

How to connect ? We use logical connectors - not ~  , and &, or | .
implication -> and biconditional <->

<b>Truth tables - </b>

p - true false
~p - false true

p false false true true
q false true false true
AND 
r false false false true

p false false true true
q false true false true
OR
r false true true true

p false false true true
q false true false true
IMPLICATION
r true true false true

p false false true true
q false true false true
BICONDITIONAL
r true false false true

Example of a model - 
P - it is raining.
Q - it is a Tuesday.

{P=true, Q=false}

A knowledge base - a set of sentences known by a knowledge based agent to be true.

Entailment - a|= b

In every world where a is true, b is also true.

Inference - 

P - it is raining.
Q - it is a Tuesday.
R - Harry will go for a run.

KB - (P & ~Q)-> R.

<b>Inference - If it is a Tuesday and it is not raining, Harry will go for a run.</b>

Does KB|=a ?
To verify this, we use Model checking algorithms. 
 - Enumerate all possible models,
 - If every model where KB is true, a is also true, then <b>KB entails a.</b>

<hr>

KB for Harry example - 

P false false false false true true true true
Q false false true true false false true true
R false true false true false true false true
KB false false false false false <b>true</b> false false

Only one scenario.

De Morgan's Law 
- ~(a | b) = ~a & ~b
- ~(a & b) = ~a | ~b


Conjunctive normal form - CNF - 
logical sentence that is a conjunction of clauses.

example - (A | b | c) & (d | ~e) & (f | g)

Convert to CNF - 
 - Eliminate Biconditionals
 - Eliminate Implications
 - Move ~ inwards using De Morgan's laws.

<b>Inference by resolution - </b>

To determine if KB|=a, 
    - convert KB & ~a to CNF
    - Keep checking if we can use resolution to produce a new clause.
    - if we ever produce an empty clause, we have a contradiction.
    - else we can't add new clauses, no entailment.

<b>First Order Logic </b>

Person(A) - A is a person.
~Person(A) - A is not a person.
BelongsTo(A, x) - A belongs to x.

<b>Universal quantification - </b>

Vx.BelongsTo(x, A) -> ~ BelongsTo(x, B)
 - For all objects x, if x belongs to A, then x does not belong to B.
 - Anyone in A is not in B.

<b>Existential Quantification - </b>

Ex. House(x) & BelongsTo(A,x)
 - There exists an object x such that x is a house and A belongs to x.
 - A belongs to x.

Combined - Ax. Person(x) -> (Ey.House(y) & BelongsTo(x,y))
All this enables AI to represent knowledge based on what information
<hr>