#In certain applications of the queue, it is common to repeatedly dequeue 
#an element, process it in some way, and then immediately enqueuer 
#the same element. Modify ArrayQueue implementation to include a 
#rotate( ) method that has semantics identical to the combination, 
#Q.enqueue (Q.dequeue()). However, your implementation should be more efficient than making two separate calls.

import queue
q=queue.FlexiQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.rotate()
#print(q.dequeue())
#print(q.dequeue())
#print(q.dequeue())
#print(q.dequeue())
q.viewQue()