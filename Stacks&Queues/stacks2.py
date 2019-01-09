#Implement a function that reverses a list of elements by pushing
# them onto a stack in one order, 
#and write them back to the list in reversed order.

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()

s=Stack()
list1=[1,2,3,4]
list2=[]
for i in list1:
    s.push(i)
for i in range(0,4):
    list2.append(s.pop())
print(list2)








