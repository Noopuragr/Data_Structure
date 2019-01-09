#Design a stack using a single queue as an instance variable, 
#and only constant additional local memory within the method bodies.


import queue

class stack:
	def __init__(self):
#		self.data=[]
		self.q=queue.FlexiQueue()
	def is_empty(self):
		return self.q.is_empty()
	def push(self,data):
		self.q.enqueue(data)
	def pop(self):
		for i in range(self.q.length()-1):
			#dequeued=self.q.dequeue()
			self.q.enqueue(self.q.dequeue())
		return self.q.dequeue()
	def printQueue(self):
		return self.data

s=stack()
list1=[x for x in input("enter elements").split(',')]
for i in list1:
	s.push(i)
#	print(s.pop)

#print(s.pop())
#print(s.pop())
print(s.printQueue())
'''s.push()
s.push(11)
s.push(21)
#list2=[20,40,50]
s.push(20)
s.push(80)
#print(s.pop())
#Doubt only popping first element, second pop() is not workingss20,None'''

