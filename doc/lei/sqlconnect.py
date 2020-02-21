import mysql.connector
from setting import Settings

class Sqldata(object):
    def __init__(self):
        self.user =  Settings.mysqluser 
        self.passwd = Settings.msqlpassword
        self.table = Settings.database
        self.result = Settings.result
    def sql_kw(self,id):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.result)
        cursor = coon.cursor()
        cursor.execute('select kw1,kw2,kw3 from kw_weight limit %s,1', [id])
        kw = cursor.fetchall()
        kw1 = kw[0][0]
        kw2 = kw[0][1]
        kw3 = kw[0][2]
        cursor.execute('select sender from kw_weight limit %s,1', [id])
        sender = cursor.fetchall()
        sender = sender[0][0]
        cursor.close()

        return [kw1,kw2,kw3,sender]
    def sql_conn(self,id):

        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('select body from message limit %s,1',[id])
        body = cursor.fetchall()
        cursor.execute('select sender from message limit %s,1',[id])
        sender =  cursor.fetchall()
        cursor.close()
        #coon.close()
        return [body,sender]
    def data_num(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('select count(body) from message')
        num = cursor.fetchall()
        cursor.close()
        coon.close()
        return num
    def kw_num(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.result)
        cursor = coon.cursor()
        cursor.execute('select count(id) from kw_weight')
        num = cursor.fetchall()
        cursor.close()
        coon.close()
        return num
    def sql_insert(self,id,kw,pd,sender):
        print(id,sender,kw,pd)
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.result)
        cursor = coon.cursor()
        kw1 = kw[0]
        kw2 = kw[1]
        kw3 = kw[2]
        weight1 = pd[0]
        weight2 = pd[1]
        weight3 = pd[2]
        print(id,sender,kw1,kw2,kw3,weight1,weight2,weight3)
        cursor.execute('insert into kw_weight (id,sender,kw1,kw2,kw3,weight1,weight2,weight3) values (%s,%s,%s,%s,%s,%s,%s,%s)',[id,sender,kw1,kw2,kw3,weight1,weight2,weight3])
        coon.commit()

        cursor.close()
        coon.close()

    def sql_check(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.result)
        cursor = coon.cursor()
        cursor.execute("drop table if exists kw_weight")
        sql  = """
        create table kw_weight(
        id int NOT NULL,
        sender varchar(200),
        kw1 varchar(200),
        kw2 varchar(200),
        kw3 varchar(200),
        weight1 varchar(200),
        weight2 varchar(200),
        weight3 varchar(200)
        )
        """
        cursor.execute(sql)
        cursor.close
        coon.close



if __name__ == '__main__':
    #count=Sqldata().data_num()
    #print(count)
   # i = count[0][0]
    #print(i)
    o=Sqldata().sql_kw(2)
    print(o)







