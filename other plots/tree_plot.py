import networkx as nx
import matplotlib.pyplot as plt


# graph 1
#nodes = ['A','B','C','D','E','F','G']
#coordinates = [[1,1],[2,1.5],[1,2],[2,2],[3,1],[3,2],[4,1.5]]
#pos = {}
#G = nx.Graph()
#G.add_edge('A', 'B', weight=1901)
#G.add_edge('A', 'C', weight=19)
#G.add_edge('A', 'D', weight=22)
#G.add_edge('C', 'B', weight=1962)
#G.add_edge('C', 'D', weight=1885)
#G.add_edge('B', 'D', weight=1922)
#G.add_edge('B', 'E', weight=1205)
#G.add_edge('D', 'E', weight=1106)
#G.add_edge('D', 'F', weight=1007)
#G.add_edge('B', 'F', weight=1976)
#G.add_edge('E', 'F', weight=19)
#G.add_edge('E', 'G', weight=1941)
#G.add_edge('F', 'G', weight=41)
##pos = nx.circular_layout(G)  # positions for all nodes
#i=0
#for x in nodes:
#    pos[x] = coordinates[i]
#    i=i+1
    
# graph 2
nodes = ['A','B','C','D','E','F','G','H','I']
G = nx.Graph()
G.add_edge('A', 'B', weight=22)
G.add_edge('B', 'C', weight=24)
G.add_edge('C', 'D', weight=26)
G.add_edge('D', 'E', weight=32)
G.add_edge('E', 'F', weight=19)
G.add_edge('F', 'G', weight=20)
G.add_edge('G', 'H', weight=32)
G.add_edge('H', 'I', weight=22)
G.add_edge('I', 'A', weight=32)
G.add_edge('A', 'C', weight=41)
G.add_edge('C', 'H', weight=41)
G.add_edge('C', 'E', weight=41)
G.add_edge('E', 'G', weight=41)
G.add_edge('E', 'H', weight=41)

pos = nx.circular_layout(G)  # positions for all nodes



##################
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color = 'pink')

# edges
nx.draw_networkx_edges(G, pos, width=1, alpha=1, edge_color='b')

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

grafo_labels = nx.get_edge_attributes(G,'weight')
edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels = grafo_labels)
plt.axis('off')
plt.show()

