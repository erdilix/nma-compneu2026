# Pseudocode twin — W2D3 Tutorial 2: Initialize variables

- **Answer twin:** `../solutions/W2D3_Tutorial2_Solution_37abbdad.py`
- **Reading view:** `../W2D3_Tutorial2_pseudocode.md`

Fill each `____`. Comments above a blank are the hint; the completed answer is the sibling `.py`.

```text
"""
1) Whichever eigenvalue is 1 is the stable solution. There should be another
eigenvalue that is <1, which means it is decaying and goes away after the
transient period.

2) The eigenvector corresponding to this eigenvalue is the stable solution.

3) To see this, we need to normalize this eigenvector so that its 2 elements
sum to one, then we would see that the two numbers correspond to
[P(open), P(closed)] at equilibrium -- hopefully these are exactly the
equilibrium solutions observed in Section 2.
""";

# whichever eigenvalue is 1, the other one makes no sense
print(eigenvector1 / eigenvector1.sum())
print(eigenvector2 / eigenvector2.sum())
```
