# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 07:57:49 2018

@author: Administrator
"""
import community
import numpy as np
import networkx as nw
from matplotlib import pyplot as plt
def sampleIBP(alpha, num_objects):  
    # Initializing storage for results
    result = np.zeros([num_objects, 1000]).astype(int)
    # Draw from the prior for alpha
    alpha_N=alpha/np.arange(1,num_objects+1)
    Knews = np.random.poisson(alpha_N)
#    print(alpha_N[0:40])
#    print(Knews[np.nonzero(Knews)[0][:]])
    # Filling in first row of result matrix
    if Knews[0]==0:
        Knews[0]=1
    t=Knews[0]
    result[0, 0:t] = np.ones(t) #changed form np.ones([1, t])
    # Initializing K+
    K_plus = t
    for i in range(1, num_objects):
#        ff=counter()
        for j in range(0, K_plus):
            mk=np.sum(result[0:i,j])
            nmk=i - mk
            logmk=1E-5
            lognmk=1E-5
            if mk!=0:
                logmk=np.log(mk)
            if nmk!=0:
                lognmk=np.log(nmk)            
            p = np.array([logmk - np.log(i+1), 
                          lognmk - np.log(i+1)])
            p = np.exp(p - max(p))
            if(np.random.uniform(0,1) < p[0]/np.sum(p)):
                result[i, j] = 1
#                ff()
            else:
                result[i, j] = 0
        t = Knews[i]
        x = K_plus + 1
        y = K_plus + t
        result[i, (x-1):y] = np.ones(t) #changed form np.ones([1, t])
        K_plus = K_plus+t
#        print("---ff is:",ff()-1)
    result = result[:, 0:K_plus]
#    for k in range(K_plus):
#        print(np.shape(np.nonzero(result[:,k])[0]))
    return list([result, K_plus,alpha_N,Knews])

def harmi(num_objects):
    HN = 0
    for i in range(0, num_objects):
        HN = HN + 1/(i+1)
    return HN    

def simulateNetwork(N):
    
    HN=harmi(N)
    alpha = np.random.gamma(3,1/(1+HN))
    [Z, K_plus,_,_] = sampleIBP(alpha, N)
#    print(Z)
    a=np.random.gamma(2,1,size=K_plus)
    b=np.random.gamma(1,1,size=K_plus)
    Rho = np.random.gamma(a,b)
    data=np.zeros((N,N)).astype(int)
    for i in range(N):
        for j in range(N):
            rho=sum(Z[i,:]*Z[j,:]*Rho)
#            print(rho)
            data[i,j]=np.random.poisson(rho)
#    print(Z)
#    str=input("origin Z is:")
    return data
N=20
data=simulateNetwork(N)
print(data)
edges=np.nonzero(data)
print(edges)
G=nw.DiGraph()
G.add_nodes_from(np.arange(20))
edge_num=np.shape(edges)[1]
weights=np.zeros(edge_num).astype(int)
for i in range(edge_num):
    weights[i]=data[edges[0][i],edges[1][i]]
#    edge.append(e)
#print(zip(edges[0],edges[1],weights))
G.add_weighted_edges_from(zip(edges[0],edges[1],weights))
nw.draw(G,with_labels=True,pos = nw.random_layout(G))
plt.show()
nw.draw(G,with_labels=True,pos = nw.circular_layout(G))
plt.show()
nw.draw(G,with_labels=True,pos = nw.shell_layout(G))
plt.show()
nw.draw(G,with_labels=True,pos = nw.spring_layout(G))
plt.show()
nw.draw(G,with_labels=True,pos = nw.spectral_layout(G), nodecolor='r', edge_color='b')
plt.show()
plt.savefig("yu.png")
#for n,nbrs in G.adjacency():
#    for nbr,eattr in nbrs.items():
#        weight=eattr['weight']
#        print('(%d,%d,%0.3f)' %(n,nbr,weight))
degree = nw.degree_histogram(G)          #返回图中所有节点的度分布序列
x = range(len(degree))                             #生成x轴序列，从1到最大度
y = [z / float(sum(degree)) for z in degree]
#将频次转换为频率，这用到Python的一个小技巧：列表内涵，Python的确很方便：）
plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线
plt.show()                                                          #显示图表
#G = nx.random_graphs.barabasi_albert_graph(1000,3)   #生成一个n=1000，m=3的BA无标度网络
#print(G.degree(0))                                   #返回某个节点的度
#print(G.degree())                                     #返回所有节点的度
#print(nw.degree_histogram(G))    #返回图中所有节点的度分布序列（从1至最大度的出现频次）
#Degree centrality measures.（点度中心性？）
dc=nw.degree_centrality(G)    # Compute the degree centrality for nodes.
idc=nw.in_degree_centrality(G)    # Compute the in-degree centrality for nodes.
odc=nw.out_degree_centrality(G)   #  Compute the out-degree centrality for nodes.
#print('dc is:',dc,'idc is:',idc,'odc is :',odc)
#Closeness centrality measures.（紧密中心性？）
cc=nw.closeness_centrality(G)    # Compute closeness centrality for nodes.
#print('cc is:',cc)
#Betweenness centrality measures.（介数中心性？）
bc=nw.betweenness_centrality(G)     #Compute betweenness centrality for nodes.
eb=nw.edge_betweenness_centrality(G)#     Compute betweenness centrality for edges.
#print('bc is:',bc,'eb is:',eb)
#Current-flow closeness centrality measures.（流紧密中心性？）
#cfc=nw.current_flow_closeness_centrality(G)    # Compute current-flow closeness centrality for nodes.
#Current-flow betweenness centrality measures.（流介数中心性？）
#cfbc=nw.current_flow_betweenness_centrality(G)   #  Compute current-flow betweenness centrality for nodes.
#ecfbc=nw.edge_current_flow_betweenness_centrality(G)    # Compute current-flow betweenness centrality for edges.
#print('cfbc is:',cfbc,'ecfbc is :',ecfbc)
#Eigenvector centrality.（特征向量中心性？）
ec=nw.eigenvector_centrality(G) #    Compute the eigenvector centrality for the graph G.
ecnp=nw.eigenvector_centrality_numpy(G)  #   Compute the eigenvector centrality for the graph G.
#print('ec is:',ec,'ecnp is:',ecnp)
#Load centrality.（彻底晕菜~~~）
lc=nw.load_centrality(G)   #  Compute load centrality for nodes.
#el=nw.edge_load(G)   #  Compute edge load.
#print('lc is:',lc)
#print(nw.clustering(G))
#print(list(nw.connected_components(G)))
#nx.degree_centrality(G)//节点度中心系数。通过节点的度表示节点在图中的重要性，默认情况下会进行归一化，其值表达为节点度d(u)除以n-1（其中n-1就是归一化使用的常量）。这里由于可能存在循环，所以该值可能大于1.

#       nx.closeness_centrality(G)//节点距离中心系数。通过距离来表示节点在图中的重要性，一般是指节点到其他节点的平均路径的倒数，这里还乘以了n-1。该值越大表示节点到其他节点的距离越近，即中心性越高。

#      nx.betweenness_centrality(G)//节点介数中心系数。在无向图中，该值表示为节点作占最短路径的个数除以((n-1)(n-2)/2)；在有向图中，该值表达为节点作占最短路径个数除以((n-1)(n-2))。

#      nx.transitivity(G)//图或网络的传递性。即图或网络中，认识同一个节点的两个节点也可能认识双方，计算公式为3*图中三角形的个数/三元组个数（该三元组个数是有公共顶点的边对数，这样就好数了）。

#     nx.clustering(G)//图或网络中节点的聚类系数。计算公式为：节点u的两个邻居节点间的边数除以((d(u)(d(u)-1)/2)。
#输出图信息
path=nw.all_pairs_shortest_path(G)     #调用多源最短路径算法，计算图G所有节点间的最短路径
print(path[0][2])                                     #输出节点0、2之间的最短路径序列： [0, 1, 2])
print(G.graph)
#输出节点信息
print(G.nodes(data=True))
#输出边信息
print(G.edges())
#计算图或网络的传递性
print(nw.transitivity(G))
#节点个数
print(G.number_of_nodes())
#边数
print(G.number_of_edges())
#节点邻居的个数
print(G.neighbors(1))
# 图划分D:\game\yang\grape.py
#part = community.partition(G)
#print(part)
#计算模块度
#mod = community.modularity(part,G)
#print(mod)

#绘图
#values = [part.get(node) for node in G.nodes()]
#nw.draw_spring(G, cmap=plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
#plt.show()
nw.write_pajek(G,'yunetwork.net')
G_matrix=nw.to_numpy_matrix(G)
np.savetxt('Out_put_file.txt',G_matrix)#用ucinet读取一下这个输出文件
