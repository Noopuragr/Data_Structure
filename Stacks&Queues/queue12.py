#Give an array based implementation of double-ended queue supporting 
#behaviors like len (), add_first(), add_last(), delete_first(), delete_last(), first() and last(). 
#Double-ended queue should be of fixed capacity. When queue is full, inserting element from one end should cause an element to be lost from the opposite side.

class Deque():
	default_capacity=5
	def __init__(self):
		self.data=[None]*Deque.default_capacity
		self.size=0
		self.front=0
		self.back=0
	def addLast(self,val):
		if self.size==0:
			self.data[self.front]=val
			self.size+=1
			self.back=self.front
		elif not self.isfull():
			new_pos=(self.back+1)%len(self.data)
			self.data[new_pos]=val
			self.back=(self.back+1)%len(self.data)
			self.size+=1
		else:
			self.data[self.front]=val
			self.back=self.front
			self.front=(self.front+1)%len(self.data)

#		if len(self.data)>self.size:
#			self.front=(self.front+1)%len(self.data)
	def isfull(self):
		return self.size==Deque.default_capacity
	def isempty(self):
		return self.size==0
	def delLast(self):
		if not self.isempty():
			temp=self.data[self.back]
			self.data[self.back]=None
			self.back=(self.back-1)%len(self.data)
			self.size-=1
			return tmp

	def delFirst(self):
		if not self.isempty():
			temp=self.data[self.front]
			self.data[self.front]=None
			self.front=(self.front+1)%len(self.data)
			self.size-=1
			return tmp
	def addFirst(self,new):
		if self.size==0:
			self.data[self.front]=new
			self.size+=1
			self.back=self.front
		elif not self.isfull():
			new_pos=(self.front-1)%len(self.data)
			self.data[new_pos]=new
			self.front=new_pos
			self.size+=1
		else:
			self.data[self.back]=new
			self.front=self.back
			self.back=(self.back-1)%len(self.data)

	def printQue(self):
		print(self.data)

d=Deque()

#d.addLast(4)
d.addFirst(3)
d.addFirst(4)
d.addFirst(5)
d.addLast(8)
d.printQue()
#d.delLast()
#d.delFirst()









