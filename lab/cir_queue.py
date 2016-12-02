class cir_queue:
	def __init__(self,size=10):
		self._size=size
		self._que=[None]*self._size
		self._ini=0
		self._size=DEF_SIZE
	def isEmpty(self):
		if len(self._que)==0:
			return True
		else: 
			return False
	def _resize(self,new):
		old=self._que
		self._que=[None]*new
		walk=self._ini
		for iwalk in range()
	def front(self):
		if len(self._que)!=0:
			return self._que[self._ini]
		else: 
			return "The queue is empty"
	def dqueue(self):
		if(self._ini==len(self._que)-1):
			self._ini=0
		elif(self._ini!=self._fin):
			self._ini+=1
		elif self._ini==self._fin: 
			self._que=[]
		else: 
			return "The queue is empty"
	def nqueue(self,var):
		if self._ini==0 or self._ini==self._fin+1:
			self._que.append(var)
			self._fin+=1
		elif self._fin==len(self._que)-1:
			self._fin=0
			self._que[0]=var
		else:
			self._fin+=1
			self._que[self._fin]=var

import time
a=cir_queue()
t1=time.perf_counter()	
for i in range(0,100000):
	a.nqueue(i)
for j in range(0,100000):
	a.dqueue()
t2=time.perf_counter()	

print("The time taken is ",t2-t1)