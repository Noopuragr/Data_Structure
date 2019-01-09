#When a share of common stock of some company is sold, the capital gain (or, sometimes, loss) is the difference between 
#the share’s selling price and the price originally paid to buy it. This rule is easy to understand for a single share,
#but if we sell multiple shares of stock bought over a long period of time, then we must identify the shares actually being sold. 
#A standard accounting principle for identifying which share of stock were sold in such a case to use a FIFO protocol –
#the shares sold are the ones that have been held the longest period.
#For example, suppose we buy 100 shares at Rs 20 each on day 1, 20 shares at Rs 24 on day 2, 200 shares at Rs 36 on day3.
#And sell 150 shares on day 4 at Rs 30 each. Then applying FIFO principle means that of the 150 shares sold, 100 were bought on day1, 
#320 were bought on day2, and 30 were bought on day3. The capital gain in this case would therefore be 100*10 + 20*6 + 30 * (-6), or Rs 940. 
#Write a program that takes as input a sequence of transactions of the form “buy x share(s) at Rs y each” or “sell x share(s) at Rs y each” ,
#assuming that transactions occur on consecutive days and the values x and y are integers. 
#Given this input sequence output should be the total capital gain (loss) for the entire sequence, using the FIFO protocol to identify shares.

import queue
q=queue.FlexiQueue()
def buy(x,y):
	q.enqueue([x,y])
def sell(x,y):
	if not q.isEmpty():
		sum=0
		l=q.dequeue()
		if l[0]<x:
			while(x!=0):
				x=x-l[0]
				if x>0:
					sum=l[0]*(y-l[1])
					l=q.dequeue()
				else:
					x=l[0]+x
					sum=sum+x*(y-l[1])
					l[0]=l[0]-x
					q.enqueue(l)
		else:
			sum=sum+x*(y-l[1])
			l[0]=l[0]-x
			q.enqueue([l[0],l[1]])
		length=q.length()

		for i in range(length-1):
			q.enqueue(q.dequeue())	

	return sum

buy(3,8)
buy(5,4)
#sell(2,5)
print("Gain/Loss",sell(2,5))
