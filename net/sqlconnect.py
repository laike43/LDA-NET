import mysql.connector
from setting import Settings




class Sqldata(object):
    def __init__(self):
        self.user =  Settings.mysqluser 
        self.passwd = Settings.msqlpassword
        self.table = Settings.database
        self.result = Settings.result

    def sender_date(self,send_date,nowdate):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        predate = send_date
        nowdate = nowdate
        cursor.execute("select sender,rvalue from message,recipientinfo where message.mid=recipientinfo.mid and DATE_FORMAT(date,'%Y%m%d') "
                       "> %s and DATE_FORMAT(date,'%Y%m%d') < %s limit 1,10000;",[predate,nowdate])
        stock = cursor.fetchall()
        cursor.close()
        coon.close()
        return stock

    def sender_node(self):
        coon = mysql.connector.connect(user=self.user, password=self.passwd, database=self.table)
        cursor = coon.cursor()
        cursor.execute("select * from employeelist ")
        egar = cursor.fetchall()
        cursor.close()
        coon.close()
        return egar










