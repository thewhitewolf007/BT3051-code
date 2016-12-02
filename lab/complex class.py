class complexno:
	def __init__(self,a=0,b=0):
		self._real=a
		self._img=b
	def __repr__(self):
		if(self.img>0):
			return "%g+%gj" % (self._real , self._img)
		else:
			return "%g%gj" % (self._real , self._img)
	def __add__(self,other):
		return(complexno(self._real+other.real,self._img+other.img))
	def __mul__(self,other):
		return(complexno(self._real*other.real+self._img*other.img,self._img*other.real+self._real*other.img))
	def __invert__(self):
		return(complexno(self.real,-self.img))
	@property
	def real(self):
		return self._real	
	@property
	def img(self):
		return self._img
	

a=complexno(1,2)
b=complexno(2,3)
c=a+b
d=a*b
e=~a
print(a)
print(a,b,c,d,e)
