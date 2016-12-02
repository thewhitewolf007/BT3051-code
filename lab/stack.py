class stack:
	def __init__(self):
		self._sta=[]
	def pop(self):
		self._sta.pop()
	def push(self,var):
		self._sta.append(var)
	def top(self):
		return self._sta[-1]
	def isEmpty(self):
		if len(self._sta)==0:
			return True
		else: 
			return False


def evaluate(a,b,op):
	if(op=="+"):
		return a+b
	elif(op=="-"):
		return a-b
	elif(op=="/"):
		return a/b
	elif(op=="*"):
		return a*b
	elif(op=="**")|(op=="^"):
		return a**b