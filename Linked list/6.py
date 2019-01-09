# Create two separate single lists. Check two list are same. If the two lists have the same number of elements in the same order,
# If the two lists have the same number of elements in the same order,then they are treated as same.

import linked_list
class compare:
#	def __init__(self):
#		self.l1=linked_list.slist()
#		self.l2=linked_list.slist()
	def comp(self,l1,l2):
		node1=l1.head
		node2=l2.head
		while node1!=None and node2!=None:
			if node1.data==node2.data:
				node1=node1.next
				node2=node2.next
			else:
				print("Both liist are not same")
				break
		print("both list are same ignore if not same")
l1=linked_list.slist()
l2=linked_list.slist()
l1.addFirst(1)
l1.addFirst(3)
l2.addFirst(1)
l2.addFirst(2)
c=compare()
c.comp(l1,l2)
l1.printList()
l2.printList()



