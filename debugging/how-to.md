The [trace](https://docs.python.org/3/library/trace.html#module-trace) module allows
you to trace program execution,
generate annotated statement coverage listings, print caller/callee relationships
and list functions executed during a program run.
It can be used in another program or from the command line.

Just run: `python -m trace --count --trace debugging/main.py`

To run pdb debugger call from source code the `breakpoint()` built-in Python function.
