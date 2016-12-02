def raman(n):
	num=[]
	for i in range(1,n):
		for j in range(i,n):
			for k in range(1,n):
				for l in range(k,n):
					if((i**3+j**3)==(k**3+l**3) and (i!=k) and (j!=l) and (i!=l) and (j!=k) and ((k**3+l**3)<10000)):	
						if ((i**3+j**3) not in num):
							num.append((i**3+j**3))
							num.append(i)
							num.append(j)
							num.append(k)
							num.append(l)
	return(num)

print(raman(25))