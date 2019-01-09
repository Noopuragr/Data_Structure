#Add method the check whether two BSTs are same. Provide test cases.

import tree
b=tree.BST()
a=tree.BST()
#b.add_node(11)
assert(b.add_node(40)==True)
assert(b.add_node(50)==True)
assert(b.add_node(25)==True)
assert(b.add_node(100)==True)
assert(b.add_node(35)==True)
assert(b.add_node(6)==True)
assert(b.add_node(8)==True)
assert(b.add_node(2)==True)
assert(b.add_node(11)==True)
assert(b.NumEle()==9)
assert(b.lookup(40)==True)
assert(b.lookup(60)==False)
assert(b.height()==5)
#assert(b.delete_node(2)==None)#change the value of node 2 to None
assert(b.terminal()==4)
assert(b.findMin()==2)
assert(b.findMax()==100)
assert(b.leftsubtree()==6)
assert(b.rightsubtree()==2)
#######################################################################
assert(a.add_node(40)==True)
assert(a.add_node(50)==True)
assert(a.add_node(25)==True)
assert(a.add_node(100)==True)
assert(a.add_node(35)==True)
assert(a.add_node(6)==True)
assert(a.add_node(8)==True)
assert(a.add_node(2)==True)
assert(a.add_node(11)==True)

def compare(node1,node2):
	if node1 is None and node2 is None:
		return True
	if node1 is not None and node2 is not None:
		return node1.data==node2.data and compare(node1.left,node2.left) and compare(node1.right,node2.right)
	return False

assert(compare(a.root,b.root)==True)