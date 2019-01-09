#Design a queue using two stacks as instance variables, 
#such that all queue operations execute in amortized O(1) time.

import Limited_stacks
class StkQue():
	def __init__(self):
		self.s1=Limited_stacks.Stack()
		self.s2=Limited_stacks.Stack()
	def isEmpty(self):
		return self.s1.is_empty()
	def qLength(self):
		return self.s1.stack_Len()
	def enque(self,ele):
		self.s1.stack_push(ele)
		#print(ele)
		#print(self.s1.stack_pop())
	def deque(self):
		for i in range(self.s1.stack_Len()):
			self.s2.stack_push(self.s1.stack_pop())
		return self.s2.stack_pop()




q=StkQue()
q.enque(1)
q.enque(2)
q.enque(3)
print(q.deque())
print(q.deque())

