# Day 12

For part II, it is important to use a cache for the function calls.
The function calls are recursive and, thus, expensive.

In my solution, I have cooked up my own look-up table.
It is perhaps easier to just use the `cache` decorator from `functools`.

See also
- https://docs.python.org/3/library/functools.html
- https://en.wikipedia.org/wiki/Memoization
