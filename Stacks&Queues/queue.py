#Queue Implementation
class FlexiQueue:
	default_capacity=1
	def __init__(self):
		self.data=[None]*FlexiQueue.default_capacity
		self.front=0
		self.size=0
	def isEmpty(self):
		return self.size==0		
	def length(self):
		return self.size
	def capacity(self):
		return(len(self.data))
	def first(self):
		if not self.isEmpty():
			return self.data[self.front]
	def last(self):
		return self.data[self.size]
	def enqueue(self,ele):
		#print(self.size)
		#print(len(self.data))
		if self.size==len(self.data):
			self.resize(2*len(self.data))
			#print(self.size)
			#print(len(self.data))
		new_pos=(self.front+self.size)%len(self.data)
		#print(new_pos)
		self.data[new_pos]=ele
		#print(ele)
		self.size+=1
		#return self.data

#	def printQueue(self):
#		return self.data

	def dequeue(self):
		if not self.isEmpty():
			element=self.data[self.front]
			#print(element)
			self.data[self.front]=None
			self.front=(self.front+1)#%len(self.data)
			#print("inside dequeue",self.front)
			self.size-=1
			'''if 0<self.size<len(self.data)//4:
				self.resize(len(self.data)//2)'''
			return element
		else:
			return None

	def resize(self,cap):
		#print(self.data)
		old=self.data
		#print(old)
		#print(cap)
		walk=self.front
		#print(walk)
		self.data=[None]*cap
		for k in range(len(old)):
			self.data[k]=old[walk]
			#print(self.data[k])
			walk=(walk+1)%len(old)
			#print old[walk]
			#print(self.data)
		self.front=0
		#print(old)
	def rotate(self):
		new=self.data[self.front]
		self.data[self.front]=None
		new_pos=(self.front+self.size)%len(self.data)
		self.data[new_pos]=new
		self.front=(self.front+1)%len(self.data)
	def viewQue(self):
		print(self.data)



'''list1=[1,2,3]
q=FlexiQueue()
print(q.enqueue(list1))

list2=[4,5,6]
print(q.enqueue(list2))
print(q.dequeue())
print(q.dequeue())'''
#print(q.printQueue())
'''q.enqueue(list2)
list3=[7,8,9]
q.enqueue(list3)'''

#print(q.dequeue())'''

#Doubt one extra none value is coming in output