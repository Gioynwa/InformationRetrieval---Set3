import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kendalltau

def realPageRank(prGraph, prBlock, start, end):
  
  lis = []
  realLis = []
  trueSum = 0
  for i in range(start, end + 1):
    lis.append((prBlock.get(str(i))) / prBlock.get(str(start)))
    trueSum += (prBlock.get(str(i))) / prBlock.get(str(start))

  truePageRank = prGraph / trueSum
  j = 0
  for i in range(start, end + 1):
    realLis.append({str(i):truePageRank * lis[j]})
    j += 1
  
  return(realLis)

dampFactor = 0.85
graph = nx.DiGraph()
graph.add_edges_from([('RED', 'RED'), ('RED', 'GREEN'), ('RED', 'YELLOW'), ('GREEN', 'GREEN'), 
                  ('GREEN', 'YELLOW'), ('GREEN', 'RED'), ('GREEN', 'BLUE'), ('YELLOW', 'RED'), 
                  ('YELLOW', 'YELLOW'), ('YELLOW', 'GREEN'), ('YELLOW', 'BLUE'), ('BLUE', 'BLUE'), ('BLUE', 'YELLOW'), ('BLUE', 'GREEN')])

plt.figure(figsize = (10, 10))
nx.draw_networkx(graph, with_labels = True)

pr = nx.pagerank(graph, dampFactor)
print("BlockRank:", pr)
print("\n\n")

# red graph
graphRed = nx.DiGraph()
graphRed.add_edges_from([('0', '6'), ('0', '4'), ('1', '2'), ('1', '5'), 
                  ('1', '6'), ('1', '7'), ('2', '1'), ('2', '3'), 
                  ('2', '7'), ('3', '2'), ('3', '7'), ('3', '4'), ('4', '3'), ('4', '7'),
                  ('4', '6'), ('4', '0'), ('4', '5'), ('5', '4'), 
                  ('5', '6'), ('5', '1'), ('6', '0'), ('6', '1'), 
                  ('6', '7'), ('6', '4'), ('6', '5')])

prRed = nx.pagerank(graphRed, dampFactor)
print("Approximate pagerank of red Graph:", prRed)

truePrRed = realPageRank(pr.get('RED'), prRed, 0, 7)
print("Real pagerank of red Graph:", truePrRed)
print("\n\n")

# green graph
graphGreen = nx.DiGraph()
graphGreen.add_edges_from([('8', '9'), ('8', '14'), ('9', '8'), ('9', '10'), 
                  ('9', '11'), ('9', '13'), ('10', '9'), ('10', '14'), 
                  ('10', '13'), ('10', '11'), ('11', '10'), ('11', '9'), ('11', '12'), ('12', '11'),
                  ('12', '10'), ('12', '13'), ('13', '12'), ('13', '10'), 
                  ('13', '9'), ('13', '14'), ('14', '13'), ('14', '10'), 
                  ('14', '8')])

prGreen = nx.pagerank(graphGreen, dampFactor)
print("Approximate pagerank of green Graph:", prGreen)

truePrGreen = realPageRank(pr.get('GREEN'), prGreen, 8, 14)
print("Real pagerank of green Graph:", truePrGreen)
print("\n\n")

# yellow graph
graphYellow = nx.DiGraph()
graphYellow.add_edges_from([('15', '16'), ('15', '21'), ('15', '17'), ('15', '18'), 
                  ('16', '15'), ('16', '22'), ('16', '17'), ('17', '16'), 
                  ('17', '15'), ('17', '22'), ('18', '15'), ('18', '22'), ('18', '21'), ('19', '21'),
                  ('19', '22'), ('20', '21'), ('20', '22'), ('21', '20'), 
                  ('21', '19'), ('21', '18'), ('21', '15'), ('22', '16'), 
                  ('22', '17'), ('22', '18'), ('22', '19'), ('22', '20')])

prYellow = nx.pagerank(graphYellow, dampFactor)
print("Approximate pagerank of yellow Graph:", prYellow)

truePrYellow = realPageRank(pr.get('YELLOW'), prYellow, 15, 22)
print("Real pagerank of yellow Graph:", truePrYellow)
print("\n\n")

# blue graph
graphBlue = nx.DiGraph()
graphBlue.add_edges_from([('23', '24'), ('23', '27'), ('23', '30'), ('23', '31'), 
                  ('24', '23'), ('24', '25'), ('24', '26'), ('25', '24'), 
                  ('25', '29'), ('25', '31'), ('26', '24'), ('26', '28'), ('26', '25'), ('25', '26'),
                  ('27', '31'), ('27', '23'), ('27', '30'), ('27', '29'), 
                  ('27', '28'), ('28', '27'), ('28', '26'), ('28', '31'), 
                  ('28', '29'), ('29', '28'), ('29', '27'), ('29', '31'), ('29', '25'),
                  ('30', '27'), ('30', '23'), ('31', '25'), ('31', '23'), ('31', '29'), ('31', '28'), ('31', '27')])

prBlue = nx.pagerank(graphBlue, dampFactor)
print("Approximate pagerank of blue Graph:", prBlue)

truePrBlue = realPageRank(pr.get('BLUE'), prBlue, 23, 31)
print("Real pagerank of blue Graph:", truePrBlue)
print("\n\n")