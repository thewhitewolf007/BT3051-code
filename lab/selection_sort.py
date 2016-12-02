def selection_sort(arr):
	n=len(arr)
	for i in range(n):
		k=i
		for j in range(i,n):
			if(arr[j]<arr[k]):
				k=j
		arr[k],arr[i]=arr[i],arr[k]
	return arr
import time


if __name__=='__main__':
	ar=list(reversed(list(range(10000))))
	t1=time.perf_counter()	
	selection_sort(ar)
	t2=time.perf_counter()	
	print("The time taken is ",t2-t1)
