Stacks are a fundamental data structure that follows the Last In First Out (LIFO) principle, meaning the last element added is the first one to be removed. In Python, you can implement a stack using a list or the collections.deque module. 

The deque (double-ended queue) from the collections module is more efficient for stack operations:

Push: Add an element to the top of the stack (using append).
Pop: Remove and return the top element (using pop).
Peek: Get the top element without removing it (access the last element).


Both methods are straightforward, but using deque is generally preferred for stacks because it provides O(1) time complexity for append and pop operations. Choose the method that best suits your needs!

remember:
  stack[0] is the bottom or first element
  stack[-1] is the top or last element


USE CASES:
  undo/redo features
  moving back/forward through browser history
  backtracking algorithms
  calling functions (call stack)