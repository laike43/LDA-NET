import mysql.connector
from settings import Settings

class Sqldata(object):
    def __init__(self):
        self.user =  Settings.mysqluser
        self.passwd = Settings.msqlpassword
        self.table = Settings.database

    def employee(self,firstname,lastname):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('select * from employeelist where firstname=%s and lastname=%s',[firstname,lastname])
        t = cursor.fetchall()
        cursor.close()
        coon.close()
        return t
    def upemployee(self,location,email,firstname,lastname):
        print(location)
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        sql = 'UPDATE employeelist SET '+location
        sql2 =sql+'= %s where firstname=%s and lastname =%s'
        cursor.execute(sql2,[email,firstname,lastname])
        coon.commit()
        cursor.close()
        coon.close()
    def sql_emplotee(self,firstname,lastname,email1,email2,email3,email4):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('insert into employeelist (firstname,lastname,email_id1,email_id2,email_id3,email_id4) value (%s,%s,%s,%s,%s,%s)',[firstname,lastname,email1,email2,email3,email4])
        coon.commit()
        cursor.close()
        coon.close()
    def sql_outmessage(self,date,subject,semail,remail,body):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('insert into outmessage (date,subject,semail,remail,body) value (%s,%s,%s,%s,%s)',[date,subject,semail,remail,body])
        coon.commit()
        cursor.close()
        coon.close()
    def sql_inmessage(self,date,subject,semail,remail,body):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('insert into inmessage (date,subject,semail,remail,body) value (%s,%s,%s,%s,%s)',[date,subject,semail,remail,body])
        coon.commit()
        cursor.close()
        coon.close()
    def sql_message(self,date,subject,semail,message_id,body):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('insert into message (date,subject,semail,message_id,body) value (%s,%s,%s,%s,%s)',[date,subject,semail,message_id,body])
        coon.commit()
        cursor.close()
        coon.close()
    def sql_count(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('select count(id) from message')
        t=  cursor.fetchall()
        cursor.close()
        coon.close()
        return t
    def sql_recip(self,mid,date,rtype,evalue):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute('insert into recip (mid,date,rtype,evalue) value (%s,%s,%s,%s)',[mid,date,rtype,evalue])
        coon.commit()
        cursor.close()
        coon.close()
    
    def sql_check_message(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute("drop table if exists message")
        sql = """
        create table message(
        id int(8) NOT NULL AUTO_INCREMENT primary key ,
        date varchar(500),
        subject text,
        message_id varchar(500),
        semail varchar(500),
        body text)
        """
        cursor.execute(sql)
        cursor.close
        coon.close
    def sql_check_outmessage(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute("drop table if exists outmessage")
        sql = """
        create table outmessage(
        id int(8) NOT NULL AUTO_INCREMENT primary key ,
        date varchar(200),
        subject text,
        semail varchar(200),
        remail text,
        body text)
        """
        cursor.execute(sql)
        cursor.close
        coon.close
    def sql_check_inmessage(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute("drop table if exists inmessage")
        sql = """
        create table inmessage(
        id int(8) NOT NULL AUTO_INCREMENT primary key,
        date varchar(200),
        subject text,
        semail varchar(200),
        remail text,
        body text)
        """
        cursor.execute(sql)
        cursor.close
        coon.close
    
    def sql_check_employee(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute("drop table if exists employeelist")
        sql = """
        create table employeelist(
        id int(8) NOT NULL AUTO_INCREMENT primary key,
        firstname varchar(200),
        lastname varchar(200),
        email_id1 varchar(200),
        email_id2 varchar(200),
        email_id3 varchar(200),
        email_id4 varchar(200))
        """
        cursor.execute(sql)
        cursor.close
        coon.close
    def sql_check_recip(self):
        coon = mysql.connector.connect(user=self.user,password=self.passwd,database=self.table)
        cursor = coon.cursor()
        cursor.execute("drop table if exists recip")
        sql = """
        create table recip(
        rid int(8) NOT NULL AUTO_INCREMENT primary key ,
        mid int(8),
        date varchar(500),
        rtype varchar(300),
        evalue varchar(500)) 
        """
        cursor.execute(sql)
        cursor.close
        coon.close
        return 
if __name__ == '__main__':
    Sqldata().sql_check_recip()
