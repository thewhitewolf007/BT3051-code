import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort	
from insert_sort import insert_sort
ar=list(reversed(range(100))) 
t1=time.perf_counter()	
selection_sort(ar)
t2=time.perf_counter()	
ar=list(reversed(range(100))) 
print("The time taken by selection sort is ",t2-t1)
t1=time.perf_counter()	
bubble_sort(ar)
t2=time.perf_counter()	
print("The time taken by bubble sort is ",t2-t1)
ar=list(reversed(range(100))) 
t1=time.perf_counter()	
insert_sort(ar)
t2=time.perf_counter()	
print("The time taken by insertion sort is ",t2-t1)
