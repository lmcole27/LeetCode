class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def newNode(key):
  return Node(key)
 
 
# driver code
#let us create two sorted linked lists to test the above
#function. Created lists shall be
#a: 5->10->15->40
#b: 2->3->20
a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)


v = []
while(a is not None):
    v.append(a.key)
    a = a.next
 
while(b is not None):
    v.append(b.key)
    b = b.next

v.sort()
print(v)
result = Node(-1)
# temp = result
for i in range(len(v)):
  result.next = Node(v[i])
  print(i, result.next.key, Node(v[i]).key)
  result = result.next
    
print(result.key)
