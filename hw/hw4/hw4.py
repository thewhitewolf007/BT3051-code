# BT3051 Assignment 4
#Roll number : BE14B002
# Collaborators : None
#Time: 1:00
import numpy as np
import matplotlib.pyplot as plt 
import networkx as nx
def barabasi_albert_graph (G, nNodes , mLinks ):
	# G is an initial graph , which should be an nx.Graph type of object
	# nNodes is the number of nodes to add to G
	# mLinks is the number of links that get added from a new node to existingnodes in each iteration
	degree=[]
	total_edges=G.number_of_edges()
	initial_nodes=G.number_of_nodes()
	total_nodes=initial_nodes
	if initial_nodes<mLinks:
		return "Error in graph"
	for inode in range(1,initial_nodes+1):
		degree.append(G.degree(inode))
	for jnode in range(initial_nodes+1,initial_nodes+nNodes+1):
		G.add_node(jnode)
		divide=2*total_edges
		prob=[deg/divide for deg in degree]
		edge=list(np.random.choice(list(range(1,total_nodes+1)),size=mLinks,p=prob,replace=False))
		edge_list=[(jnode,x) for x in edge]
		total_nodes+=1
		total_edges+=mLinks
		degree.append(mLinks)
		for x in edge:
			degree[x-1]+=1
		G.add_edges_from(edge_list)
	G_new = G.copy ()
	### CODE FOR graph creation
	nx.draw(G_new)
	plt.savefig("Graph.png", format="PNG")
	plt.clf()
	return G_new

if __name__=='__main__':
	G = nx.Graph()
	G.add_edge(1,2)
	G_new = barabasi_albert_graph (G,98,1)	
	nx.draw(G_new)
	plt.show(G_new)
	
#plot G_new