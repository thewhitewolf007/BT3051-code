import time
x=list(range(0,100000))
print("Enter the number to be searched:")

num=1

def linear_search(array,num):
	for isearch in range(0,len(array)):
		if(num==array[isearch]):
			print("The number is present at location",isearch+1)
			return 0
	print("The number is not found!")
	return 0
t1=time.perf_counter()	
linear_search(x,num)
t2=time.perf_counter()
print("The time taken is ",t2-t1)