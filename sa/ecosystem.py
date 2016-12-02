from random import randint
class Bear:
	def __init__(self):
		gen=randint(0,1)
		if gen==0:
			self._gen="Male"
		else:
			self._gen="Female"
		self._str=randint(1,101)
	def getStr(self):
		return self._str
	def getGen(self):
		return self._gen
	def __repr__(self):
		return "%s %s with strength %i"   %(self._gen,type(self).__name__,self._str)
	def __str__(self):
		return "blah"

class Fish:
	def __init__(self):
		gen=randint(0,1)
		if gen==0:
			self._gen="Male"
		else:
			self._gen="Female"
		self._str=randint(1,101)
	def getStr(self):
		return self._str
	def getGen(self):
		return self._gen
	def __repr__(self):
		return "%s %s with strength %i"   %(self._gen,type(self).__name__,self._str)


spots=10
ecosystem=[[]for ieco in range(spots)]

for i in range(spots):
	typ=randint(0,2)
	if typ==1:
		ecosystem[i].append(Fish())
	elif typ==2:
		ecosystem[i].append(Bear())

print(ecosystem)


for ilist in range(spots):
	for j in range(len(ecosystem[ilist])):
		if ilist==0:
			step=randint(0,1)
		elif ilist==spots-1:
			step=randint(-1,0)
		else:
			step=randint(-1,1)
		print(step)
		input()
		if step!=0:
			if len(ecosystem[ilist+step])==0:
				ecosystem[ilist+step].append(ecosystem[ilist][j])
				k=ecosystem[ilist].pop(j)
			# elif ecosystem

