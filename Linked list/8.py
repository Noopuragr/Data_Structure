#Write a method which creates the union of elements from two lists.

import linked_list
class intersection:
	def intersect(self,l1,l2,l3):
		node1=l1.head
		node2=l2.head
		while not node1==None:
			if l2.chkEle(node1.data):
				l3.addFirst(node1.data)
				node1=node1.next
			else:
				node1=node1.next
		print("The intersection of list is")
		l3.printList()
l1=linked_list.slist()
l2=linked_list.slist()
l3=linked_list.slist()
l1.addFirst(1)
l1.addFirst(2)
l2.addFirst(1)
l2.addFirst(3)
l2.addFirst(4)
l2.addFirst(5)
l2.addFirst(2)
i=intersection()
i.intersect(l1,l2,l3)

