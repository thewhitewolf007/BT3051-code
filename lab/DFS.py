from stack import stack
from random import randint
import matplotlib.pyplot as plt 
import networkx as nx

# G=nx.gnm_random_graph(randint(5,10),randint(10,20))
# nx.draw(G,with_labels=True)
# plt.show(G)
G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
e=[(1,2),(1,3),(1,4),(2,6),(3,5),(2,4),(6,7)]
G.add_edges_from(e)
def DFS(G,start):
	nodes=G.nodes()
	neighbors={}
	status={}
	to_do=stack()
	processed=[]
	for i in nodes:
		neighbors[i]=G.neighbors(i)
		status[i]="u"
	to_do.push(start)
	status[to_do.top()]="d"
	while to_do.isEmpty()==False:
		on=to_do.top()
		status[to_do.top()]="p"
		processed.append(to_do.top())
		to_do.pop()
		for inode in neighbors[on]:
			if(status[inode]=="u"):
				status[inode]="d"
				to_do.push(inode)
	return processed

print(DFS(G,2))
