class queue:
	def __init__(self):
		self._que=[]
	def isEmpty(self):
		if len(self._que)==0:
			return True
		else: 
			return False
	def front(self):
		return self._que[0]
	def dqueue(self):
		self._que.pop(0)
	def nqueue(self,var):
		self._que.append(var)


import time
a=queue()
t1=time.perf_counter()	
for i in range(0,100):
	a.nqueue(i)
for j in range(0,100):
	a.dqueue()
t2=time.perf_counter()	

print("The time taken is ",t2-t1)