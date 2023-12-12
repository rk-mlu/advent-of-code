# Day 12

For part II, it is important to use a cache for the function calls.
The function calls are recursive and, thus, expensive.

I have written the look-up tables myself, but it is perhaps easier to just use
the `cache` decorator from `functools`.

See also
- https://docs.python.org/3/library/functools.html
- https://en.wikipedia.org/wiki/Memoization
