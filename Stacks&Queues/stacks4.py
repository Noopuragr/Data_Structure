#Implement a transfer function and two temporary stacks, 
#to replace the contents of a given stack S with those same elements, 
#but in reverse order.

import Limited_stacks

def revStack():
	s=Limited_stacks.Stack()
	temp_stk1=Limited_stacks.Stack()
	temp_stk2=Limited_stacks.Stack()
	for i in range(10):
		s.stack_push(i)
	print("The content of stack is ")
	s.printStack()
	for j in range(s.stack_Len()):
		temp_stk1.stack_push(s.stack_pop())
	for k in range(temp_stk1.stack_Len()):
		temp_stk2.stack_push(temp_stk1.stack_pop())
	for m in range(temp_stk2.stack_Len()):
		s.stack_push(temp_stk2.stack_pop())
	print("The reverse of stack is")
	s.printStack()


revStack()

