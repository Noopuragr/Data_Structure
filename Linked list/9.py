#Create single list such that it should always contain unique elements. 
#are should be taken that, if element is already present in the list, you should not add it again.

import linked_list
def unique(l1,ele):
	if not l1.is_empty():
		if not l1.chkEle(ele):
			l1.addLast(ele)
		else:
			print("Element already present",ele)
#			print(ele)
	else:
		l1.addLast(ele)
#		print("adding last")

l1=linked_list.slist()
unique(l1,1)
unique(l1,2)
unique(l1,1)
unique(l1,3)
unique(l1,4)
unique(l1,3)
l1.printList()


