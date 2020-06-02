import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kendalltau 


graph = nx.DiGraph()

graph.add_edges_from([('0', '1'), ('0', '7'), ('0', '6'), ('1', '7'), 
                  ('1', '2'), ('2', '1'), ('2', '7'), ('3', '7'), 
                  ('3', '5'), ('4', '5'), ('5', '6'), ('6', '5'), ('7', '6')])

plt.figure(figsize = (7, 4))
nx.draw_networkx(graph, with_labels = True)

d_array = np.array([0.55, 0.65, 0.75, 0.85, 0.95])

pr = []
for i in range(5):
  pr.append(nx.pagerank(graph, d_array[i], max_iter = 500))

x = d_array
lis = []

for i in range(8):
  lis2 = []
  for j in range(5):
    lis2.append(pr[j].get(str(i)))
  lis2 = np.array(lis2)
  lis.append(lis2)

lis = np.array(lis)
print(lis)

plt.figure(figsize = (10, 10))
plt.plot(x, lis[0], color="blue", label="0")
plt.plot(x, lis[1], color="yellow", label="1")
plt.plot(x, lis[2], color="green", label="2")
plt.plot(x, lis[3], color="red", label="3")
plt.plot(x, lis[4], color="black", label="4")
plt.plot(x, lis[5], color="orange", label="5")
plt.plot(x, lis[6], color="purple", label="6")
plt.plot(x, lis[7], color="pink", label="7")

# o komvos 3 peftei akrivos mazi me ton komvo 4
plt.legend(loc='upper left')
plt.show()

corr, _ = kendalltau(lis[0], lis[1])
print('Kendall Rank correlation between 0-1: %.5f' % corr)

corr, _ = kendalltau(lis[0], lis[7])
print('Kendall Rank correlation between 0-7: %.5f' % corr)

corr, _ = kendalltau(lis[0], lis[6])
print('Kendall Rank correlation between 0-6: %.5f' % corr)

corr, _ = kendalltau(lis[1], lis[2])
print('Kendall Rank correlation between 1-2: %.5f' % corr)

corr, _ = kendalltau(lis[1], lis[7])
print('Kendall Rank correlation between 1-7: %.5f' % corr)

corr, _ = kendalltau(lis[2], lis[7])
print('Kendall Rank correlation between 2-7: %.5f' % corr)

corr, _ = kendalltau(lis[3], lis[7])
print('Kendall Rank correlation between 3-7: %.5f' % corr)

corr, _ = kendalltau(lis[3], lis[5])
print('Kendall Rank correlation between 3-5: %.5f' % corr)

corr, _ = kendalltau(lis[4], lis[5])
print('Kendall Rank correlation between 4-5: %.5f' % corr)

corr, _ = kendalltau(lis[5], lis[6])
print('Kendall Rank correlation between 5-6: %.5f' % corr)

corr, _ = kendalltau(lis[6], lis[7])
print('Kendall Rank correlation between 6-7: %.5f' % corr)

corr, _ = kendalltau(lis[3], lis[4])
print('Kendall Rank correlation between 3-4: %.5f' % corr)