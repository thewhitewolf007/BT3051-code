import networkx as nx 
import matplotlib.pyplot as plt 
import time
t1=time.perf_counter()	
G=nx.hypercube_graph(10)
t2=time.perf_counter()	
# nx.draw(G,with_labels=True)
# plt.show(G)
print("The time taken is ",t2-t1)
