import matplotlib.pyplot as plt 
import networkx as nx
import time
def binary(x,n):
	a=bin(x)
	sp=list(a)[2:]
	l=len(sp)
	for i in range(0,n-l):
		sp.insert(0,'0')
	return sp

def switch(x):
	if(x=='0'):
		return '1'
	else:
		return '0'
		
def hypercube(n):
	G=nx.Graph()
	edge_list=[]
	for i in range(0,2**n):
		rep=binary(i,n)
		for j in range(0,n):
			add=rep[:]
			add[j]=switch(add[j])
			add.insert(0,'0b')
			add="".join(add)
			add=int(add,2)
			if(add>i):
				edge_list.append((i,add))
	G.add_edges_from(edge_list)
	return(G)

if __name__=='__main__':
	t1=time.perf_counter()	
	G=hypercube(3)
	t2=time.perf_counter()	
	nx.draw(G,with_labels=True)
	plt.show(G)
	print("The time taken is ",t2-t1)
