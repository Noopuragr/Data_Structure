#Implementation of linked list

class slist:
	class _Node:
		def __init__(self,ele):
			self.data=ele
			self.next=None
	def __init__(self):
		self.head=None
		self.tail=None
		self.count=0
	def is_empty(self):
		return self.count==0
	def addFirst(self,val):
		new_node=self._Node(val)
		if not self.is_empty():
			#print(self.head) #Print None
			#print(new_node)#Print address i.e.  0x000002B11B196B38
			new_node.next=self.head # we are assigning None to new_node.next 
			self.head=new_node#updating the value of current self.head
			#print(self.head)# Print address i.e.  0x000002B11B196B38
			#print(new_node)# Print address i.e.  0x000002B11B196B38
			#print(new_node.next)#Print None
		else:
			self.head=self.tail=new_node
#			print("Inside else")
		self.count+=1
	def addLast(self,val):
		new_node=self._Node(val)
		if not self.is_empty():
			self.tail.next=new_node
			self.tail=new_node
#			print("adding last")
		else:
			self.head=self.tail=new_node
		self.count+=1
	def delFirst(self):
		if not self.is_empty():
			if self.count>1:
				self.head=self.head.next
				print("deleting first")
			else: 
				self.head==None
				print("deleting first")
				self.tail=None
			self.count-=1
			#return self.head
	def delLast(self):
		if not self.is_empty():
			if self.head==self.tail:
				self.head=self.tail=None
			else:
				tail=self.tail
				cur=self.head
				print("deleting last")
				while(cur.next!=tail):
					cur=cur.next
				self.tail=cur
				cur.next=None
			self.count-=1
	def eleCount(self):
		return self.count
	def chkEle(self,val):
		temp=self.head
		while temp:
			if val==temp.data:
#				print("present")
				return True
#				break
			temp=temp.next
	def maXEle(self):
		max=0
		temp=self.head
		while temp:
			if max<temp.data:
				max=temp.data
			temp=temp.next
		return max
	def minEle(self):
		min=self.maXEle()
		temp=self.head
		while temp:
			if min>temp.data:
				min=temp.data
			temp=temp.next
		return min
	def addAny(self,val,addaftr):
		new_node=self._Node(val)#created object of _Node class, it will have data and next
		if not self.is_empty():
			#print(self.head)
			temp=self.head
			while(temp.data!=addaftr and not temp.next is None):
				temp=temp.next
				#print(temp)
			new_node.next=temp.next
			temp.next=new_node
		else:
			print("mentioned key is not present")
			self.addLast(new_node.data)
		self.count+=1
	def printList(self):
		node=self.head
		while node is not None:
			print(node.data)
			node=node.next
#		return 
		#print
	def delAny(self,val):
		temp1=self.head
		while(temp1.data!=val and not temp1.next is None):
			temp1=temp1.next
		temp2=temp1.next
		temp1.next=temp2.next
		temp2.next=None
		self.count-=1
'''	def reverse(self):
		prev=None
		current=self.head
		while(current is not None):
			next=current.next
			current.next=prev
			prev=current
 			current=next
		self.head=prev'''
#		



l=slist()
l.addFirst(3)
l.addLast(2)
l.addFirst(5)
l.addFirst(1)
l.addLast(0)
#l.addAny(8,3)
l.delAny(3)
#print("maximum element is",l.maXEle())
#print("minimum element is",l.minEle())
#l.delFirst()
#l.delLast()
#print("total number of element is:",l.eleCount())
#l.chkEle(4)
l.printList()
#l.reverse()
#l.printList()

