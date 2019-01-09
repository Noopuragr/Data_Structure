#Design an ADT for a two-color, double-stack ADT that consists of two stacks – one “red” and one “blue” –
#and has as its operations color-coded versions of the regular stack ADT operations.
#For example, this ADT should support both a red push operation and a blue push operation.
#Give an efficient implementation of this ADT using single array whose capacity is set at some value N that is assumed to always be larger 
#than the sizes of the red and blue stacks combined.

class doubleStack():
	capacity=50
	def __init__(self):
		self.blue_count=0
		self.blue_max=20
		self.red_max=20
		self.red_count=0
		self.data=[None]*doubleStack.capacity
#		self.data=[]
#		print(self.size)
	def is_blue_empty(self):
		return self.blue_count==0
	def is_red_empty(self):
		return self.red_count==0
	def is_blue_full(self):
		return self.blue_count==self.blue_max
	def is_red_full(self):
		return self.red_count==self.red_max
	def stack_blue_peek(self):
		if not self.blue_count==0:
			return self.data[(self.blue_count)-1]
	def stack_red_peek(self):
		print("hi")
		if not self.red_count==0:
			return self.data[(self.red_count)]
	def stack_blue_push(self,ele):
		if not self.is_blue_full():
			self.data[self.blue_count]=ele
			self.blue_count+=1
	def stack_blue_pop(self):
		if not self.is_blue_empty():
			self.blue_count-=1
			return self.data[self.blue_count]

	def stack_red_push(self,ele):
		if not self.is_red_full():
			self.data[self.red_count-1]=ele
			self.red_count-=1
#		print(self.data)
	def stack_red_pop(self):
		x=0
		if not self.is_red_empty():
#			self.red_count+=1
			x= self.data[self.red_count]
		self.red_count+=1
		return x
	def printStack(self):
		print(self.data)
		print(self.red_count)
d=doubleStack()
d.is_blue_empty()
d.is_blue_full()
d.stack_blue_push(3)
d.stack_blue_push(8)
d.stack_blue_push(1)
d.stack_red_push(5)
d.stack_red_push(4)
d.stack_red_push(9)
#print(d.stack_blue_pop())
#print(d.stack_blue_pop())
#print(d.stack_blue_pop())
d.printStack()
#print(d.stack_red_pop())
#sprint(d.stack_red_pop())
print("The peek element from blue stack is",d.stack_blue_peek())
print("The peek element form red stack is",d.stack_red_peek())
