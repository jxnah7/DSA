When a thing is defined in terms of itself

A recurisve method is one that calls itself, could be used
instead of iteration

easier to read and write
easier to debug

sometimes slower
uses more memory


We always need a base case, otherwise infinite recursion is a thing


***
Recursion relies on the call stack, which means each recursive call adds a new frame to the stack. This takes memory, so if you have too many recursive calls without reaching the base case, you can run into a stack overflow (too much memory usage) and crash the program. It’s generally better to use recursion only for problems that can be solved with a relatively small number of recursive calls.
***