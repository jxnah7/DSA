# Create a stack
stack = []

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
top_element = stack[-1] if stack else None
print("Top element:", top_element)
