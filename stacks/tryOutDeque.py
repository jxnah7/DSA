from collections import deque

#this is a stack but faster
stack = deque()

stack.append('yellow truck')
stack.append('black car')
stack.append('blue van')
stack.append('green machine')
stack.append('purple lawn mower')

#in terminal it will show a deque object which is actually good
#helps readability and knwoing the intent
print(stack)

favorite = stack.pop()

print(f"Hmm my favorite would be: {favorite}")

print("since I already chose that one what about you? Heres your options btw")
print(stack)
print("\n\n\n")

for i in range(1000000):
  stack.append('teehee')
  i = i + 1
print(stack)