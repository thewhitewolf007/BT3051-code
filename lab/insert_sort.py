def insert_sort(arr):
	n=len(arr)
	for i in range(1,n):
		curr=arr[i]
		pos=i
		for j in range(i-1,0,-1):
 			if arr[j]>curr:
 				arr[j+1]=arr[j]
 				pos=j
 			else:
 				break
		arr[pos]=curr
	return(arr)
 

import time
if __name__=='__main__':
	ar=list(reversed(range(1000))) 
	t1=time.perf_counter()	
	print(insert_sort(ar))
	t2=time.perf_counter()	
	print("The time taken by insertion sort is ",t2-t1)
