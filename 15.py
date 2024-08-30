class MinStack(object):

    def __init__(self):
          self.l = []  
          self.s = sorted(self.l)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.l.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.l[-1]:
          del self.l[-1]

    def top(self):
        """
        :rtype: int
        """
        if self.l:    
          x = []
          x = sorted(self.l)  
          return x[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.l:  
          x = []
          x = sorted(self.l)  
          return x[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(f"object = {obj.l}")
obj.push(2)
obj.push(3)
obj.push(-2)
obj.push(0)
obj.push(2)
obj.pop()
print(f"object = {obj.l}")
param_3 = obj.top()
print(f"object = {obj.l[-1]}")
param_4 = obj.getMin()
print(f"object = {obj.l[0]}")
print(f"object = {obj.l[-2]}")
print(param_3, param_4)