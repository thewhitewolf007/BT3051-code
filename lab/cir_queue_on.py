import time
class circular_queue():
	def __init__(self):
		
		self.items= [None]*(10)
		self.size=0
		self.front=0
		
		
	
	def enqueue(self,element):
		if self.size == len(self.items):
			self._resize(2*len(self.items))
		self.items[(self.front+self.size)%len(self.items)] = element
		self.size+=1
		# print(self.items)
			# self.items[self.back] = element
			# self.back = (self.back + 1) % (self.max_size)
			# self.count+=1
		
	def dequeue(self):
		if self.size == 0:
			print("The queue is empty")

		else:
			item = self.items[self.front]
			self.front = (self.front+1)% (len(self.items))
			self.size-=1
			# print(self.items)
			return item
	def top(self):
		return(self.items[self.front])

	def _resize(self,cap):
		old = self.items
		self.items = [None]*cap
		# print(self.items)
		for k in range(len(old)):
			# print(old[k])
			self.items[k] = old[self.front]
			self.front = (self.front+1)%len(old)
		self.front = 0



time1=time.perf_counter()
a=circular_queue()
for i in range(0,10):
	a.enqueue(i)
# print(a.dequeue())
for i in range (5):
	a.dequeue()
for i in range(0,10):
	a.enqueue(i)
time2=time.perf_counter()
print(time2-time1)

print(a.items)