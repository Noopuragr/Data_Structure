#import queue
#Design a BST class with methods to add element, search element, number of elements 
#and delete requested element. Provide test cases.
class BST:
	class _TreeNode:
		def __init__(self,ele):
			self.data=ele
			self.left=None
			self.right=None
	def __init__(self):
		self.root=None
		self.count=0
		self.tcount=0

	def add_node(self,ele):
		current=parent=self.root
		while current is not None and current.data!=ele:
			parent=current
			if ele<current.data:
				current=current.left
			elif ele>current.data:
				current=current.right
		if current is None:
			new_node=self._TreeNode(ele)
			if parent is None:
				self.root=new_node
			elif ele <parent.data:
				parent.left=new_node
			elif ele>parent.data:
				parent.right=new_node
			self.count+=1
		return True
	def isEmpty(self):
		return self.count==0
	def lookup(self,key):
		if not self.isEmpty():
			current =self.root
			if current.data==key:
				return True
			else:
				while current!=None:
					if current.data>key:
						current=current.left
					elif current.data<key:
						current=current.right
					else:
						break
				return current!=None
	def inorder(self):#Increasing order#LPR
		if not self.isEmpty():
			self._inorder_(self.root)
	def _inorder_(self,node):#first tym it will refer to root node
		if not node is None:
			self._inorder_(node.left)##left of root node#recursive call
			print(node.data)
			self._inorder_(node.right)#recursive cll
	def pre_order(self):
		if not self.isEmpty():
			self._preorder(self.root)
#			print("root")
	def _preorder(self,node):
		if not node is None:
			print(node.data)
			self._preorder(node.left)
#			print("left")
			self._preorder(node.right)
#			print(right)
	def post_order(self):
		if not self.isEmpty():
			self._postorder(self.root)
	def _postorder(self,node):
		if not node is None:
			self._postorder(node.left)
			self._postorder(node.right)
			print(node.data)
	def delete_node(self,key):
		if not self.isEmpty():
			self.root=self._delete_(self.root,key)
	def _delete_(self,node,key):
		if node is None:
			return node
		elif key<node.data:
			node.left=self._delete_(node.left,key)
		elif key>node.data:
			node.right=self._delete_(node.right,key)
		elif(node.left and node.right):
			temp=self.findMin(node.right)
			node.data=temp.data
			node.right=self._delete(node.right,node.data)
		else:
			if node.left is None:
				node=node.right
			else:
				node=node.left
			self.count-=1
		return node

#Add methods to find max and min element in BST. Provide test cases.
		
	def findMin(self):
		if not self.isEmpty():
			return self._findMin(self.root).data
	def _findMin(self,node):
		if node.left is None:
			return node
		else:
			return self._findMin(node.left)
	def findMax(self):
		if not self.isEmpty():
			return self._findMax(self.root).data
	def _findMax(self,node):
		if node.right is None:
			return node
		else:
			return self._findMax(node.right)
#to return the number of element present in BST
	def NumEle(self):
		return self.count
#to find height of tree
	def height(self):
		return self._height(self.root)

	def _height(self,node):
		if node is None:
			return 0
		else:
			ldepth=self._height(node.left)
			rdepth=self._height(node.right)
		return (max(int(rdepth)+1,int(ldepth)+1))

# Add method to count the number of terminal nodes in BST. 
#Provide test cases.
	def terminal(self):
		if not self.isEmpty():
			return self._terminal(self.root)
	def _terminal(self,nn):
		if nn.left is not None and nn.right is not None:
			self._terminal(nn.left)
			self._terminal(nn.right)
		elif nn.right is not None:
			self._terminal(nn.right)
		elif nn.left is not None:
			self._terminal(nn.left)
		else:
			self.tcount+=1
		return self.tcount

	def level_order(self):
		l=[]
		current=self.root
		l.append(self.root)
		while len(l):
			current=l[0]
			if current.left is not None:
				l.append(current.left)
			if current.right is not None:
				l.append(current.right)
			print(current.data)#here we cant write print(current), it will print the address
			del l[0]

#Add method to count number of nodes in the left sub tree and 
#number of nodes in right sub tree. Provide test cases.

	def leftsubtree(self):
		current=self.root.left
		return self.count_leftsubtree(current)
	def count_leftsubtree(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.count_leftsubtree(node.left)+self.count_leftsubtree(node.right))
	def rightsubtree(self):
		current=self.root.right
		return self.count_rightsubtree(current)
	def count_rightsubtree(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.count_rightsubtree(node.left)+self.count_rightsubtree(node.right))

#Add methods to display the traversal in ascending and descending order.

	def ascending(self):
		print(self.inorder())
	def descending(self):
		if not self.isEmpty():
			self._descending(self.root)
	def _descending(self,node):
		if not node is None:
			self._descending(node.right)
			print(node.data)
			self._descending(node.left)
						
b=BST()
b.add_node(40)
b.add_node(50)
b.add_node(25)
b.add_node(100)
b.add_node(35)
b.add_node(6)
b.add_node(8)
b.add_node(2)