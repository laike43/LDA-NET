from sqlconnect import Sqldata
import community
import networkx as nx
import networkx as nw
import matplotlib.pyplot as plt
#定义有向图
import datetime
from dateutil.relativedelta import relativedelta
def timeadd(linitdate,month):
    #linitdate = "2017-07-18"
    date_time = datetime.datetime.strptime(linitdate, '%Y-%m-%d')
    now = date_time - relativedelta(months=-month)
    return now.strftime('%Y%m%d')
def monthadd(linitdate,month):
    #linitdate = "2017-07-18"
    date_time = datetime.datetime.strptime(linitdate, '%Y-%m-%d')   #转换时间格式
    now = date_time - relativedelta(months=-month)
    return now.strftime('%Y-%m-%d')

def emplotlist():
    emdict = {}
    namelist = Sqldata().sender_node()
    for i in namelist:
        name = i[1]+'.'+i[2] +' '+ str(i[8])
        if len(i[3])!=0:
            emdict[i[3]] = name
        if len(i[4])!=0:
            emdict[i[3]] = name
        if len(i[5])!=0:
            emdict[i[3]] = name
    return emdict

def check(emdict,sen_ri):
    if sen_ri[0] in emdict and sen_ri[1] in emdict:
        return emdict[sen_ri[0]],emdict[sen_ri[1]]
    else:
        return 0
def draw(initdate,em):
    t = Sqldata().sender_date(timeadd(initdate, 0), timeadd(initdate, 5))   #全部的接受邮件和发送邮件，得到一个二维矩阵
    #print(t)
    num = 0
    DG = nx.Graph()       #生成一个空的networkx图的对象
    eglist = []           #定义一个列表

    for i in t:             #for循环迭代从数据库中读取的二维数组
        name = check(em, i)   #将收发邮件地址替换为邮件地址所对应的人，并剔除非安然公司内部人员
        if name != 0:           #判断收发人是否有一方不为安然公司内部人员
            num = num + 1
            DG.add_node(name[0])
            DG.add_node(name[1])
            eglist.append(name)     #存储所有符合条件的收件人和发送人为一组
            #print(name)
    #print(eglist)           #打印矩阵
    DG.add_edges_from(eglist)     #在两个节点之间加入边
    # colors = ['red', 'green', 'blue', 'yellow']
    try:
        nx.draw(DG, with_labels=True, pos=nx.circular_layout(DG))
        plt.show()

        #nx.draw(DG, with_labels=True, pos=nx.random_layout(DG))
        #plt.show()
    except:
        pass
   # nx.draw(DG, with_labels=True, pos=nx.circular_layout(DG))
    #plt.show()
   # nx.draw(DG, with_labels=True, pos=nx.shell_layout(DG))
    #plt.show()
   # nx.draw(DG, with_labels=True, pos=nx.spring_layout(DG))
    #plt.show()
    #nx.draw(DG, with_labels=True, pos=nx.spectral_layout(DG))
   # plt.show()
    #plt.savefig("yu.png")
    return DG
def com_dra(DG):
    G = DG
    nx.draw(DG, with_labels=True, pos=nx.circular_layout(DG))
    plt.show()
    partition = community.best_partition(G)

    # drawing
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0.
    for com in set(partition.values()):
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20,
                               node_color=str(count / size))

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()

def pingjia(G):
    c = nx.clustering(G)
    print(c)

'''
    nx.average_shortest_path_length(G) #平均最短距离

    nx.triangles(G)#三角形个数

    nx.clustering(G)#局部聚类系数

    nw. betweenness_centrality(G)#节点介数中心性特征计算

    nw.edge_betweenness_centrality(G)#边介数中心性特征计算

    nw.degree_centrality(G)#度中心性

    nw.closeness_centrality(G)#紧密中心性

    nw.eigenvector_centrality(G)#特征向量中心性

    nw. betweenness_centrality(G)#间接中心性
    

    nx.average_clustering(G)#平均聚类特征函数

    nx.rich_club_coefficient(G)#峰会系数

    nx.transitivity(G)#网络的传递性

    nw.is_chordal(G)#判断是否为弦图

    nw.chordal_graph_cliques(G)#求弦图的最大派系集

    nw.global_efficiency(G)#整体效率
    
    
'''
if __name__=="__main__":

    em = emplotlist()
    #print('字典为：',em)
    initdate = '2001-1-1'
    for i in range(4):     #共4个周期
        print('第',i+1,'个周期的局部聚类系数为：')
        DG = draw(initdate,em)
        pingjia(DG)
        initdate = monthadd(initdate, 5)   #以5个月为一个周期








