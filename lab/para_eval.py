from stack import *


exp="( ( 1 + ( ( 2 * 3 ) ^ 5 ) * 6 ) )" 
operand=stack()
operator=stack()
exp=exp.split()

for ichar in exp:
	if ichar.isnumeric():
		operand.push(ichar)
	elif (not(ichar is ')' )) and (not(ichar is '(')):
		operator.push(ichar)
	elif ichar is ')':
		b=float(operand.top())
		operand.pop()
		a=float(operand.top())
		operand.pop()
		operand.push(evaluate(a,b,operator.top()))
		operator.pop()
		
res=operand.top()
operand.pop()
if operand.isEmpty() & operator.isEmpty():
	print(res)
else: print("An error occured")