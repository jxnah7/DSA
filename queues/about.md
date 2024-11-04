FIFO Data-Structure, First In First Out

enqueue- adding an object at the end of the queue
dequeue- removing an object at the beginning of the queue

Keep in mind a queue and stack are largely the same syntax, just how you use it will determine what is it

ex.

if you init a deque() function, and use append/pop, that is the behaviour of a stack

if you init a deque() function, and use append/popleft, that is the behaviour of a queue.

popleft() removes the element in the very front of the queue.

the syntax is basic, sometimes in larger programs wrappers might be used to make readability better

// WHEN ARE QUEUES USEFUL?

1. Keyboard buffer (letters should appear on the screen in the order theyre pressed)
2. Printer Queue (Print jobs should be completed in order)
3. Linkedlists, PriorityQueues, Breadth-first-search
