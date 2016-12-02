import random
count_in=0
total_count=1000000
for i in range(total_count):
	x=random.random()
	y=random.random()
	if(x*x+y*y<1):
		count_in+=1
pi=count_in/total_count*4
print(pi)