# Implement LeakyStack. This stack should be of fixed size. 
#When push is invoked with the stack at full capacity, rather than 
#throwing a Full exception, accept the pushed element at the top while “leaking” the oldest element from the bottom of the stack to make a room.

class LeakyStack:
	capacity=3
	l=[]
	def __init__(self):
		self.data=[]
		self.count=0
		self.list=[]
	def is_empty(self):
		return self.count==0
	def is_full(self):
		return self.count==LeakyStack.capacity
	def stack_Len(self):
		return self.count
	def stack_push(self,val):
		l=[]
		if not self.is_full():
			self.data.append(val)
			self.count+=1
			#print(self.data)
		else:
			self.remove(val) 
	def stack_pop(self):
		if not self.is_empty():
			self.count-=1
			return self.data.pop()
	def printStack(self):
		if not self.is_empty():
			print(self.data)
	def remove(self,val):
		del self.data[0]
		self.count-=1
		self.stack_push(val)




s=LeakyStack()
s.stack_push(1)
s.stack_push(2)
s.stack_push(3)
s.stack_push(4)
#s.printStack()
print(s.stack_pop())
print(s.stack_pop())
print(s.stack_pop())
print(s.stack_pop())
'''print(s.stack_pop())
print(s.stack_pop())
print(s.stack_pop())'''
#print(s.stack_pop())