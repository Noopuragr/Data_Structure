#1.	Build maximum heap with required methods. It should support the 
#behaviors like adding element, getting maximum element, 
#extracting maximum element, count number of elements and 
#to check the method to test the heap order property.

class MaxHeap():
	def __init__(self,mylist=[]):
		self.data=mylist
		self._buildheap()
		self.count=0
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
		if j>0 and self.data[j]>self.data[parent]:
			self._swap(j,parent)
			self._upheap(parent)
#			print("data",self.data)
	def _downheap(self,j,size):
		if self.left_child(j)<size:
			left=self.left_child(j)
			bigchild=left
			if self.right_child(j)<size:
				right=self.right_child(j)
				if self.data[right]>self.data[left]:
					bigchild=right
			if self.data[bigchild]>self.data[j]:
				self._swap(bigchild,j)
				self._downheap(bigchild,size)
	def _buildheap(self):
		start=(self.length()-2)//2
		for i in range(start,-1,-1):
			self._downheap(i,self.length())

	def heap_add(self,ele):
		self.data.append(ele)
		self._upheap(self.length()-1)
		self.count+=1

	def remove_max(self):
		if self.is_Empty():
			print("Priority queue is empty")
		self._swap(0,self.length()-1)
		item=self.data.pop()
		self._downheap(0,self.length()-1)
#		return item

	def getMax(self):
		if self.length()==0:
			return -1
		return self.data[0]
		
#		self._downheap(self.length()-1)
#		print("data",self.data)

#2.	Modify Q2 to sort the input in ascending order.

	def ascending(self):
		length=self.length()
		for i in range(self.length()-1,-1,-1):
			self._swap(0,i)
			self._downheap(0,i)
	def view_heap(self):
		print(self.data)

	def checkHeapOrder(self,position):
		if self._parent(position)>self.data[position]:
			self.checkHeapOrder(position-1)
		else:
			return False




l1=[10,45,32,34,60,17]

m=MaxHeap(l1)

print("before remove_max")
m.view_heap()
m.remove_max()
print("after remove_max")
m.view_heap()
m.checkHeapOrder(4)
m.ascending()

print("After ascending")
m.view_heap()
