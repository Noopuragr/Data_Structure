# Implement a function with signature transfer(S,T) 
#that transfers all elements from Stack S onto Stack T, 
#so that that elements that starts at the top of S is the first
#to be inserted into T, and element at the bottom of S ends up
# at the top of T.

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        return self.items.append(data)
 
    def pop(self):
        return self.items.pop()
list1=[10,20,30]
S=Stack()
T=Stack()
for i in list1:
	S.push(i)

def Transfer(S,T):
	for i in range(0,3):
		T.push(S.pop())
		print(T.pop())
#	print(T.pop())
transfer=Transfer(S,T)