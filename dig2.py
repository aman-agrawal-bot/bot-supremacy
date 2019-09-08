import networkx as nx
import matplotlib.pyplot as plt
import random
"""d = {(1,2,3): ([None]),
 (2,3,4): ([None,(1,2,3)]),
 'AAAD': (['BBDD', None, None, None, None, None, None]),
 'AAFF': (['AAAD', None, None, None, None, None, None]),
 'MMCC': (['AAAD', None, None, None, None, None, None]),
 'KKLL': (['AAFF', 'MMCC', 'AAAD', 'BBDD', None, None, None])}
#d={i:i+10 for i in range(10)}
#print(d)"""
d={(random.randint(0,4),random.randint(0,4),random.randint(0,4)):[(random.randint(0,4),random.randint(0,4),random.randint(0,4)),(random.randint(0,4),random.randint(0,4),random.randint(0,4))] for i in range(10)}
g = nx.DiGraph()
g.add_nodes_from(d.keys())
for k, v in d.items():
    g.add_edges_from(([(k, t) for t in v]))
nx.draw(g,with_labels="True")
plt.show()
