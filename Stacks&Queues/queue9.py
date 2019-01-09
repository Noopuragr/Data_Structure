#Design a double-ended queue using two stacks as instance variables.


import Limited_stacks
class DQue():
	def __init__(self):
		self.front_q=Limited_stacks.Stack()
		self.back_q=Limited_stacks.Stack()
	def isEmpty():
		return self.front_q.isEmpty() and self.back_q.isEmpty()
	def q_length():
		return self.front_q.length()+self.back_q.length()
	def enqueFront(self,val):
		self.front_q.stack_push(val)
	def enqueBack(self,val):
		self.back_q.stack_push(val)
	def dequeFront(self):
		if not self.front_q.is_empty():
			return self.front_q.stack_pop()
		elif not self.back_q.is_empty():
			self.front_q.stack_push(self.back_q.pop())
			ele=self.front_q.stack_pop()
			return ele
	def dequeBack(self):
		if not self.back_q.is_empty():
			return self.back_q.stack_pop()
		elif not self.front_q.is_empty():
			self.back_q.stack_pop(self.front_q.pop())
			ele=self.back_q.stack_pop()
			return ele
d=DQue()
d.enqueFront(5)
d.enqueFront(4)
d.enqueFront(3)
d.enqueBack(6)
d.enqueBack(7)
print(d.dequeFront())
print(d.dequeBack())
		

