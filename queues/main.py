from collections import deque

stack = deque() #create queue

stack.append("M")
stack.append("E")
stack.append("O")
stack.append("W")

print(stack)

stack.popleft() #pop first element beginning of queue

print('\n')
print(stack)

#this queue follows FIFO principles
#First in first out