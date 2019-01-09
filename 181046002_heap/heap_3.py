#3.	Build priority queue to handle real time tasks. Tasks can arrive at time. The attributes of tasks are 
#task-id, priority, arrival time, execution time and deadline. 
#Compute waiting time, turnaround time for each job.
# Check whether jobs are completed within the deadline specified. 
# It is treated that 10 is maximum priority and 1 is least priority.



class minheap():
	def __init__(self,mylist=[]):
		self.data=[]
		self.data.append(mylist)
		self._buildheap()
	def length(self):
		return len(self.data)
	def is_Empty(self):
		return self.length()==0
	def _parent(self,j):
		return (j-1)//2
	def countEle(self):
		return self.count

	def left_child(self,j):
		return 2*j+1
	def right_child(self,j):
		return (2*j+2)
	def _swap(self,i,j):
		self.data[i],self.data[j]=self.data[j],self.data[i]
	def upheap(self,j):
		parent=self._parent(j)
		if j>0 and self.data[j][2]>self.data[parent][2]:
			self._swap(j,parent)
			self.upheap(parent)
		elif j>0 and self.data[j][2]==self.data[parent][2]:
			if self.data[j][1]<self.data[parent][1]:
				self._swap(j,parent)
				self.upheap(parent)

	def downheap(self,j,size):
		if self.left_child(j)<size:
			left=self.left_child(j)
			smallchild=left
			if self.right_child(j)<size:
				right=self.right_child(j)
				if self.data[right][2]>self.data[left][2]:
					smallchild=right
				elif self.data[right][2]==self.data[left][2]:
					if self.data[right][1]<self.data[left][1]:
						smallchild=right
			if self.data[smallchild][2]>self.data[j][2]:
				self._swap(smallchild,j)
				self.downheap(smallchild,size)
			elif self.data[smallchild][2]==self.data[j][2]:
				if self.data[smallchild][1]<self.data[j][1]:
					self._swap(smallchild,j)
					self.downheap(smallchild,size)

	def _buildheap(self):
		start=(self.length()-2)//2
		for i in range(start,-1,-1):
			self.downheap(i,self.length())

	def heap_add(self,ele):
		self.data.append(ele)
		self.upheap(self.length()-1)

	def waitingTime(self):
		waitingTime=[]
		turnaroundTime=[]
		for i in range(0,self.length()):
			if i is 0:
				wTime=0
				waitingTime.append(wTime)
				taTime=self.data[i][3]
				turnaroundTime.append(taTime)
			else:
				wTime=turnaroundTime[i-1]-self.data[i][2]+1
				waitingTime.append(wTime)
				taTime=waitingTime[i]+self.data[i][3]
				turnaroundTime.append(taTime)
		return waitingTime,turnaroundTime
#Turn Around Time = waiting time+executiontime
#Waiting Time = Turn Around Time of previous – Execution Time +1(due to process)
	def chkDeadline(self,taTime):
		print(taTime)
		notDeadline=[]
		for i in range(0,self.length()):
			if self.data[i][4]<taTime[i]:
				notDeadline.append(self.data[i][0])
		return notDeadline

	def descOrder(self):
		length=self.length()
		for i in range(0,self.length()-1,-1,-1):
			self._swap(0,i)
			self.downheap(0,i)



l1=[100,1,1,5,10]
q=minheap(l1)
q.heap_add([201,3,1,5,10])
q.heap_add([202,4,1,5,10])
q.heap_add([204,4,3,5,10])
q.heap_add([204,5,3,5,10])
wTime, taTime = q.waitingTime()
notDeadline = q.chkDeadline(taTime)
print(notDeadline)
