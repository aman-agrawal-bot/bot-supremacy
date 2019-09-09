import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import graphviz as pgz
"""d = {(1,2,3): ([None]),
 (2,3,4): ([None,(1,2,3)]),
 'AAAD': (['BBDD', None, None, None, None, None, None]),
 'AAFF': (['AAAD', None, None, None, None, None, None]),
 'MMCC': (['AAAD', None, None, None, None, None, None]),
 'KKLL': (['AAFF', 'MMCC', 'AAAD', 'BBDD', None, None, None])}
#d={i:i+10 for i in range(10)}
#print(d)"""
d  =[(random.randint(0,4),random.randint(0,4),random.randint(0,4)) for i in range(10)]
g = nx.DiGraph()
g.add_nodes_from(d)
d.sort()
print(d)
#print(d.keys())
#print(d)
#pos={1:[1,2],3:[4,5],6:[7,8],9:[10,12],13:[14,21]}
"""
print(d)
for i in range(len(d)):
    for j in range(i+1,len(d)):
        print(d[j][0])
"""
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if(((d[i][0]-d[j][0])**2+(d[i][1]-d[j][1])**2+(d[i][2]-d[j][2])**2)<=8):
            g.add_edge(d[i],d[j],weight=d[i][0])

#pos=nx.get_node_attributes(g,'pos')
#nx.draw_networkx_edges(g,pos,width=i)
#labels = nx.get_edge_attributes(g,'weight')
#nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
#for k, v in d.items():
#    g.add_edges_from(([(k, t) for t in v]))
#pos=nx.spring_layout(g)
pos = nx.nx_agraph.graphviz_layout(g, prog='dot')
nx.draw(g,pos,with_labels="True")
plt.draw()
plt.show()


"""
gr = nx.DiGraph()
gr.add_nodes_from(d)
#print(d.keys())
#print(d)
#pos={1:[1,2],3:[4,5],6:[7,8],9:[10,12],13:[14,21]}

print(d)
for i in range(len(d)):
    for j in range(i+1,len(d)):
        print(d[j][0])

for i in range(len(d)-1):
    for j in range(i+1,len(d)-1):
#        if(((d[i][0]-d[j][0])**2+(d[i][1]-d[j][1])**2+(d[i][2]-d[j][2])**2)<=10):
        gr.add_edge(d[i],d[j],weight=d[i][0])

#pos=nx.get_node_attributes(g,'pos')
#nx.draw_networkx_edges(g,pos,width=i)
#labels = nx.get_edge_attributes(gr,'weight')
#nx.draw_networkx_edge_labels(gr,pos,edge_labels=labels)
#for k, v in d.items():
#    g.add_edges_from(([(k, t) for t in v]))
pos2=nx.shell_layout(gr)
nx.draw(gr,pos2,with_labels="True")
plt.draw()
plt.show()
"""
