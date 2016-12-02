def bubble_sort(arr):
	n=len(arr)
	for i in range(n):
		swap=False
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				swap=True
				arr[j],arr[j+1]=arr[j+1],arr[j]
		if not swap:
			return arr
	return arr

import time
if __name__=='__main__':
	ar=list((range(5000)))+[10**8]+list(range(5000,10000))
	t1=time.perf_counter()	
	print(bubble_sort(ar))
	t2=time.perf_counter()	
	print("The time taken is ",t2-t1)
