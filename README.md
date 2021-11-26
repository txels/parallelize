# Parallelize

A simple tool for a common problem: run a function against a set of data,
in parallel, with minimum coding fuss.

Adding the decorator to a function keeps it backwards compatible, but it
adds a superpower: if you now call the function with a single iterable,
it will run the function for the whole iterable, parallelize execution
(based on configuration) and return a tuple with the results.

Usage example:

```python
from parallelize import parallelize

@parallelize
def addition(x, y):
    return x + y

assert addition(1, 5) == 6
assert addition([(1, 2), (3, 5), (12, 16)]) == ( 3, 8, 28 )
```
