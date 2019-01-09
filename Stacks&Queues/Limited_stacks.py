#Implementation stacks
class Stack:
	capacity=10
	def __init__(self):
		self.data=[]
		self.count=0
	def is_empty(self):
		return self.count==0
	def is_full(self):
		return self.count==Stack.capacity
	def stack_Len(self):
		return self.count
	def stack_peek(self):
		if not self.is_empty():
			return self.data[-1]
	def stack_push(self,ele):
		if not self.is_full():
			self.data.append(ele)
			self.count+=1
			#print(self.data)
		else:
			raise Exception("stack is full")
	def stack_pop(self):
		if not self.is_empty():
			self.count-=1
			return self.data.pop()
	def printStack(self):
		if not self.is_empty():
			print(self.data)
			

#class Exceptn(Exception):
#	print("Stack is full")
#	
s=Stack()
#s.stack_push(3)
#s.printStack()
 

