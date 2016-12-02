#BT3051 Assignment 0a
#Roll number: BE14B002
#Collaborators: None
#Time: 0:10
n=input('Enter a number> ')
try:
	n=int(n)
except ValueError:
	print("Entered  number is not an integer")
	exit()
else:
	while(n!=1):
		print(int(n))
		if(n%2==0):
			n/=2
		else: 
			n=3*n+1
print(1)