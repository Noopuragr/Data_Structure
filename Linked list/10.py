#Create double linked list with methods to add, remove, 
#to check the existence of element.

class dlist:
	class _Node:
		def __init__(self,ele):
			self.data=ele
			self.next=None
			self.prev=None
	def __init__(self):
		self.head=None
		self.tail=None
		self.count=0
	def is_empty(self):
		return self.count==0

	def addLast(self,ele):
		new_node=self._Node(ele)
		if not self.is_empty():
			self.tail.next=new_node
			new_node.prev=self.tail
			self.tail=new_node
#			self.tail=new_node.prev
#			new_node=self.tail
		else:
			self.head=self.tail=new_node
			new_node.prev=None
			new_node.next=None
		self.count+=1
	def printList(self):
		node=self.head
		while node is not None:
			print(node.data)
			node=node.next
	def deleteNode(self,ele):
		temp=self.head
#		x=temp.next
##		print(ele)
		while temp is not None:
			prev=temp.prev
			next_node=temp.next
			if temp.data==ele:
				if prev is not None:
					prev.next=next_node
					if next_node is not None:
						next_node.prev=prev
				else:
					self.head=next_node
					if next_node is not None:
						next_node.prev=None
				return
			temp=next_node
			self.count-=1
		return
d=dlist()
d.addLast(3)
d.addLast(4)
d.addLast(5)
d.addLast(6)
d.deleteNode(6)
#d.addRight(4)
#d.addRight(2)
d.printList()

