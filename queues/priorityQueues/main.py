from queue import PriorityQueue

queue = PriorityQueue()

#Add elements using put
queue.put(3.0)
queue.put(2.1)
queue.put(3.9)
queue.put(4.2)
queue.put(1.2)
queue.put(2.9)


#Cannot iterate over a PriorityQueue with a for-loop, doesnt
#support direct iteration like a list so we use while-loop

while not queue.empty():
  print(queue.get())

'''
the get() function removes the highest priority item
and then returns it so its the first element printed
'''