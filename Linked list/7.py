#Write a method which creates the union of elements from two lists.

import linked_list
class union:
#	def __init__(self):
#		self.l1=linked_list.slist()
#		self.l2=linked_list.slist()
	def union(self,l1,l2,l3):
		node1=l1.head
		node2=l2.head
		while not node1==None:
			l3.addLast(node1.data)
			node1=node1.next
		while not node2==None:
			if not l3.chkEle(node2.data):
				l3.addLast(node2.data)
#				print(node2.data)
				node2=node2.next
			else:
				node2=node2.next
		print("The union of list is :")
		l3.printList()
#		list3=l3.head

#		print(list1.data)
#		print(list2.data)
'''		while not node1==None:
			l3.addLast(list1.data)
#			list3=list3.next
			list1=list1.next
		list3=l3.head'''
'''		while not list2==None:
			if list2.data!=list3.data:
				l3.addLast(list2.data)
				list3=list3.next
				list2=list2.next'''
'''		while not list3==None:
			
			list3=list3.next'''

			


'''			if list1.data == list2.data:
				l1.addLast(list2.data)
				list1=list1.next
				list2=list2.next'''			

l1=linked_list.slist()
l2=linked_list.slist()
l3=linked_list.slist()
l1.addFirst(1)
l1.addFirst(2)
l2.addFirst(1)
l2.addFirst(3)
l2.addFirst(4)
l2.addFirst(5)
u=union()
u.union(l1,l2,l3)
#print("The union of list is",l3.printList())