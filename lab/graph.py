import matplotlib.pyplot as plt 
import networkx as nx

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
nx.draw(G,with_labels=True)
plt.show(G)
