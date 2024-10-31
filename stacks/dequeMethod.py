from collections import deque

# Create a stack
stack = deque()

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Display the stack
print("Stack:", stack)

# Pop an element from the stack
top_element = stack.pop()
print("Popped element:", top_element)

# Display the stack after popping
print("Stack after popping:", stack)

# Peek at the top element without removing it
top_element = stack[-1] if stack else None  #[-1] in python refers to top of stack, if stack else none is a safety check to ensure the stack isnt empty
print("Top element:", top_element)
