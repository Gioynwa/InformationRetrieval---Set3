import networkx as nx
import matplotlib.pyplot as plot

graph = nx.DiGraph()

graph.add_edges_from([('5', '11'), ('11', '2'), ('11', '10'), ('11', '9'), 
                  ('7', '11'), ('7', '8'), ('8', '9'), ('3', '10'), 
                  ('3', '8')])

plot.figure(figsize = (7, 4))
nx.draw_networkx(graph, with_labels = True)

hubs, authorities = nx.hits(graph, max_iter = 55, normalized = True)

print("Hub Scores: ", hubs) 
print("Authority Scores: ", authorities)