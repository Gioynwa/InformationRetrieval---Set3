import networkx as nx
import matplotlib.pyplot as plot

# 14 nodes with ids from 0 to 13
# red node has id = 0

graph = nx.DiGraph()

graph.add_edges_from([('0', '1'), ('0', '2'), ('0', '3'), ('0', '4'), 
                  ('1', '0'), ('1', '2'), ('1', '4'), ('2', '0'), 
                  ('2', '1'), ('2', '3'), ('3', '0'), ('3', '2'), ('3', '4'), ('4', '0'), ('4', '1'), ('4', '3'), ('2', '5'), ('5', '2'),
                  ('5', '6'), ('5', '9'), ('5', '7'), ('6', '5'), ('6', '7'), ('6', '8'), ('6', '9'), ('7', '5'), ('7', '6'), ('7', '8'),
                  ('8', '6'), ('8', '7'), ('8', '9'), ('8', '11'), ('9', '8'), ('9', '5'), ('9', '6'), ('9', '10'), ('10', '9'), ('10', '11'),
                  ('10', '13'), ('11', '8'), ('11', '10'), ('11', '13'), ('11', '12'), ('12', '11'), 
                  ('12', '13'), ('13', '10'), ('13', '11'), ('13', '12')])

plot.figure(figsize = (10, 10))
nx.draw_networkx(graph, with_labels = True)

dampFactor = 0.85

# for red node probability = 0.5
# for other nodes probability = 0.5 / 13 = 0.038 each

ppr1 = nx.pagerank(graph, dampFactor, personalization={'0':0.5, '1':0.038, '2':0.038, '3':0.038, '4':0.038, '5':0.038, '6':0.038, '7':0.038, '8':0.038, '9':0.038, '10':0.038, '11':0.038, '12':0.038, '13':0.038})
print(ppr1)