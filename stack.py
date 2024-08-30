# deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 
from collections import deque

my_stack = deque()
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)
my_stack.append(6)
print(my_stack)
my_stack.pop()
print(my_stack)
print(my_stack[0])

# Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements in the stack
print(stack.qsize())

# put() function to push element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop element from stack in LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())