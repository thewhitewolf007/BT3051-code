import time
x=list(range(1000))
print("enter the number to be searched:")
num=1
def binary_search(array,num):
	ipos=0
	epos=len(array)-1
	while(abs(ipos-epos)>1):
		check=int((ipos+epos)/2)
		if(num>array[check]):
			ipos=check
		elif(num<array[check]): 
			epos=check 
		else: 
			print("The number is found at position",check+1)
			return(0)
	if(array[epos]==num):
		print("The number is found at position",epos+1)
		return(0)
	print("The number is not found!")
t1=time.perf_counter()	
binary_search(x,num)
t2=time.perf_counter()
print("The time taken is ",t2-t1)