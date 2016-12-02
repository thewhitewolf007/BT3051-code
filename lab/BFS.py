from queue import queue
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
def BFS(G,start):
	nodes=G.nodes()
	neighbors={}
	status={}
	to_do=queue()
	processed=[]
	for i in nodes:
		neighbors[i]=G.neighbors(i)
		status[i]="u"
	to_do.nqueue(start)
	status[to_do.front()]="d"
	while to_do.isEmpty()==False:
		for inode in neighbors[to_do.front()]:
			if(status[inode]=="u"):
				status[inode]="d"
				to_do.nqueue(inode)
		status[to_do.front()]="p"
		processed.append(to_do.front())
		to_do.dqueue()
	return processed


print(BFS(G,1))
