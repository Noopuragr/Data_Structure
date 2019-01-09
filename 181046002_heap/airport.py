#4.	An airport is developing a computer simulation of air-traffic control that handles events such as landings and takeoffs. 
#Each event has a time stamp that denotes the time when the event will occur with additional information like, plane number, takeoff or landing.
#The simulation program needs to efficiently perform the following two fundamental operations: 1. Insert an event with a given time stamp, aircraft number, takeoff / landing (add a future event).  
#2.Extract the event with smallest time stamp (that is, determine the next event to process). 
#Design and implement suitable data structures that work efficiently in terms of time.

class airport:
	def __init__(self,mylist=[]):
		self.data=[]
		self.data.append(mylist)
		self._buildheap()

	def length(self):
		return len(self.data)
	def is_Empty(self):
		return self.length()==0
	def _parent(self,j):
		return (j-1)//2
	def countEle(self):
		return self.count

	def left_child(self,j):
		return 2*j+1
	def right_child(self,j):
		return (2*j+2)
	def _swap(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
	def _upheap(self,j):
		parent=self._parent(j)
		if j>0 and self.data[j][0]<self.data[parent][0]:
			self._swap(j,parent)
			self._upheap(parent)
#			print("data",self.data)
	def _downheap(self,j,size):
		if self.left_child(j)<size:
			left=self.left_child(j)
			bigchild=left
			if self.right_child(j)<size:
				right=self.right_child(j)
				if self.data[right][0]<self.data[left][0]:
					bigchild=right
			if self.data[bigchild][0]<self.data[j][0]:
				self._swap(bigchild,j)
				self._downheap(bigchild,size)
	def _buildheap(self):
		start=(self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())

	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)

	def remove_min(self):
		if self.is_Empty():
			print("Priority queue is empty")
		self._swap(0,self.length()-1)
		item=self.data.pop()
		self._downheap(0,self.length()-1)
		return item
l1 = [2040, 101, 'takeoff']
a=airport(l1)
a.heap_add([2045,102,'landing'])
a.heap_add([2100,103,'takeoff'])
item=a.remove_min()
print("The aircraft with id ", item[1] ," has an event of " + item[2] + " at " , item[0])