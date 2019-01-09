#Suppose you have three nonempty stacks R, S and T. 
#Describe a sequence of operations that results in S storing all 
#elements originally in T below of S’s original elements, 
#with both sets of those elements in their original configuration. 
#For example, if R = [1,2,3], S = [4, 5] and T = [6, 7, 8, 9], 
#the final configuration should have R = [1, 2, 3] and S = [6, 7, 8,  9, 4, 5].

import Limited_stacks
R=Limited_stacks.Stack()
S=Limited_stacks.Stack()
T=Limited_stacks.Stack()
l1=[1,2,3]
l2=[4,5]
l3=[6,7,8,9]
for i in l1:
	R.stack_push(i)
for i in l2:
	S.stack_push(i)
for i in l3:
	T.stack_push(i)
l4=[]
for i in range(0,2):
	l4.append(S.stack_pop())
for i in range(0,4):
	l4.append(T.stack_pop())
print(l4)


