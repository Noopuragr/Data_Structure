#Suppose you have a stack S containing n elements and a queue Q 
#that is initially empty. Write function that use Q to scan S 
#to see if it contains a certain element x, with the additional 
#constraint that your algorithm must return the elements back to S 
#in their original order. You may use S, Q and a constant number of 
#other variables.

import Limited_stacks
import queue
s=Limited_stacks.Stack()
q=queue.FlexiQueue()
def Scan(S,x):
	while not s.is_empty():
		ele=s.stack_pop()
		if ele!=x:
			q.enqueue(ele)
			#restore(s,q)
		elif ele==x:
			#s.stack_push(ele)
			#print(s.stack_pop())
			q.enqueue(ele)
			#s.stack_push(ele)
			#restore(s,q)
			print("Element found")
	while not q.isEmpty():
		i=1
		while i< q.length():
			i+=1
			q.enqueue(q.dequeue())
		s.stack_push(q.dequeue())
	#print(s.stack_pop())
#	print(s.stack_pop())

#	restore(s,q)
#			break

'''def restore(S,Q):
#	i=1
	while not q.isEmpty():
#		print("hii")
		i=0
		for i in range(q.length()-1):
			while (q.length()-1):
				q.enqueue(q.dequeue())
				i+=1
			s.stack_push(q.dequeue())
	print(s.stack_pop())
	print(s.stack_pop())


#	while not q.isEmpty():
#		for i in range(q.length()-1):
#			q.enqueue(q.dequeue())
#	print(s.stack_push(q.dequeue()))'''

s.stack_push(1)
s.stack_push(2)
s.stack_push(3)
Scan(s,1)
s.printStack()
#restore(s,q)