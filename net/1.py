import mysql.connector
conn = mysql.connector.connect(user='root', password='password', database='test')

c = nx.betweenness_centrality(G)
print('c=', c)