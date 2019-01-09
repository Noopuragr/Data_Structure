#Modify ArrayStack implementation so that the stack’s capacity is 
#limited to maxlen elements. If push is called when the stack is at full 
#capacity, throw a Full exception.

import Limited_stacks
list1=[1,2,3,4]
list2=[4,5,6,7]
s=Limited_stacks.Stack()
'''for i in list1:
	s.stack_push(i)'''
s.stack_push(list1)
s.stack_push(list2)
print(s.stack_pop())


