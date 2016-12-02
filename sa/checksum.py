num=str(input("Enter your 9 digit number>"))
if(len(num)!=9):
	print("Not a nine digit number")
	exit()
def find_ISBN(num):
	num=str(num)
	check=int(num[8])*2+int(num[7])*3+int(num[6])*4+int(num[5])*5+int(num[4])*6+int(num[3])*7+int(num[2])*8+int(num[1])*9+int(num[0])*10
	rem=check%11
	add=str(11-rem)
	if(add!=10):
		isbn="".join([add,num])
	else: isbn="".join(["x",num])
	return(isbn)

print(find_ISBN(num))