# Director Of Photography

## Description

A photography set consists of N cells in a row, numbered from 1 to N in order, and can be represented by a string C of length N. Each cell $i$ is one of the following types (indicated by $C_i$, the $ith$ character of C).

- If $C_i$ = "P", it's allowed to contain a photographer.
- If $C_i$ = "A", it's allowed to contain an actor.
- If $C_i$ = "B", it's allowed to contain a backdrop.
- If $C_i$ = ".", it must be left empty.

A photograph consists of a photographer, an actor and a backdrop, such that each of them is placed in a valid cell, and such that actor is between the photographer and the backdrop [PAB]. Such a photograph is considered artistic if the distance between the photographer and the actor is between X and Y cells (inclusive), and the distance between the actor and the backdrop is also between X and Y cells (inclusive). The distance between cells $i$ and $j$ is $|i - j|$ (the absolute value of the difference between their indices).

**Determine the number of different artistic photographs which could potentially be taken at the set**. Two photographs are considered different if they involve a different photographer cell, actor celll, and/or backdrop cell.

### Conditions stated:
1. $distance(PA) >= X \hspace{1mm}and\hspace{1mm}distance(PA) <= Y$
2. $distance(AB) >= X \hspace{1mm}and\hspace{1mm}distance(AB) <= Y$
3. $distance(ij) = |i - j|$
4. $Photograph_i ≠ Photograph_j$ if any:
- $Photograph_i(Pcell) ≠ Photograph_j(Pcell)$ 
- $Photograph_i(Acell) ≠ Photograph_j(Acell)$ 
- $Photograph_i(Bcell) ≠ Photograph_j(Bcell)$ 
5. The order doesn't matter => $PA == AP$ and $AB == BA$

## Constraints

- 1 <= N <= 200
- 1 <= X <= Y <= N

## Sample test case # 1

- N = 5
- C = APABA
- X = 1
- Y = 2
- Expected return value = 1

### Explanation # 1

The absolute distances between photographer/actor and actor/backdrop must be between 1 and 2. The only possible photograph that can be taken is with the 3 middle cells, and it happens to be artistic. 

## Sample test case # 2

- N = 5
- C = APABA
- X = 2
- Y = 3
- Expected return value = 0

### Explanation # 2

In the second case, the only possible photograph is again taken with the 3 middle cells. However, as the distance requirement is between 2 and 3, it is not possible to take an artistic photograph.

## Sample test case # 3
- N = 8
- C = .PBAAP.B
- X = 1
- Y = 3
- Expected return value = 3

### Explanation # 3

The are 4 possible photographs, illustrated as follows:
- .P.A...B
- .P..A..B
- 