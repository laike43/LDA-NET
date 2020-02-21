import os
from jiexi import em,ernorneibu
from sqlconnect import Sqldata


class Fileop(object):
    def __init__(self):
        pass
    def write_message(self,dict):
        message_id = dict['Message-ID']
        date = dict['Date']
        subject = dict['Subject']
        semail=dict['From']
        body = dict['body']
        Sqldata().sql_message(date,subject,semail,message_id,body)
        num = Sqldata().sql_count()[0][0]
       
        cc = dict['Cc'].split(',')
        bcc = dict['Bcc'].split(',')
        to = dict['To'].split(',')
        if  len(cc)!=0:
            for i in cc:
                rto =i.strip()
                rtype = 'cc'
                if i != '':
                    Sqldata().sql_recip(num,date,rtype,rto)
        if  len(bcc)!=0:
            for i in bcc:
                rto =i.strip()
                rtype = 'bcc'
                if i != '':
                    Sqldata().sql_recip(num,date,rtype,rto)
        if  len(to)!=0:
            for i in to:
                rto =i.strip()
                rtype = 'to'
                if i != '':
                    Sqldata().sql_recip(num,date,rtype,rto)

    def writeemployee(self,dict):
        message = em(dict)
        print('message',message)
        if message==0:
            print('非安然员工')
            return 0
        name = message[0]
        lastname=message[2]  

        firstname= message[1]    
        email = message[3].strip()
        t = Sqldata().employee(firstname,lastname)
        print('数据路',t)
        if len(t)==0:
            Sqldata().sql_emplotee(firstname,lastname,email,'','','')
        else:
            if len(t[0][3])!=0:
                if t[0][3] == email:
                    print('已经存在')
                    return 0
            else:
                Sqldata().upemployee('email_id1',email,firstname,lastname)
                print('添加email1')
                return 1
            if len(t[0][4])!=0:
                if t[0][4] == email:
                    print('已经存在')
                    return 0
            else:
                Sqldata().upemployee('email_id2',email,firstname,lastname)
                print('添加email2')
                return 1
            if len(t[0][5])!=0:
                if t[0][5] == email:
                    print('已经存在')
                    return 0
            else:
                Sqldata().upemployee('email_id3',email,firstname,lastname)
                print('添加email3')
                return 1
            if len(t[0][6])!=0:
                if t[0][6] == email:
                    print('已经存在')
                    return 0
            else:
                Sqldata().upemployee('email_id4',email,firstname,lastname)
                print('添加email4')
                return 1
        return 0
    def out_or_in(self,dict):

        #message_id = dict['Message-ID']
        date = dict['Date']
        subject = dict['Subject']
        semail=dict['From']
        remail = dict['To']
        body = dict['body']
        #x_from = dict['X-From']
        #x_to = dict['X-To']
        #x_cc = dict['X-cc']
        #x_orgin = dict['X-Origin']
        #x_filename = dict['X-FileName']

        b = ernorneibu(dict)
        
        if b==1:
            Sqldata().sql_inmessage(date,subject,semail,remail,body)
        else:
            Sqldata().sql_outmessage(date,subject,semail,remail,body)
    def recip(self,dict):
        empdict ={'Message-ID': '','Date': '','From': '','To':'','Subject': '','Cc':'','Mime-Version': '','Content-Type': '','Content-Transfer-Encoding': '','Bcc': '','X-From': '','X-To': '','X-cc': '','X-bcc': '','X-Folder':'','X-Origin': '','X-FileName': ''}
        for i,j in empdict.items():
            if i not in dict:
                dict[i]=''
                #print(i)
        return dict
        
    def read_file(self,file_path,num_id):
        path = file_path
        dict= {}
        body =''
        id = num_id
        num1=0
        print(file_path)
        with open(path,'r',encoding='windows-1252') as f:
            list1 = f.readlines()
            for i in range(0,len(list1)):
                str = list1[i].strip()
                try:
                    tmp = str.split(':')
                    dict[tmp[0]]=tmp[1]
                except:
                    dict['To'] =  str+ dict['To']
                num1 = i 
                if tmp[0] == 'X-FileName':
                    break
            # print (dict)
            num1 = num1+1
            for  j in range(num1,len(list1)):
                body = body + list1[j]
            dict['body']=body



        dict = self.recip(dict)
        
        #print(dict)
        self.writeemployee(dict)
        self.out_or_in(dict)
        self.write_message(dict)

'''
        print(dict)
        if ernorneibu(dict) ==1 :
            print('内部邮件')
        else:
            print('不是内部邮件')
        #print(em(dict))
        #print(ernorneibu(dict))
        #Sqldata().sql_tmp(id,date,subject,x_from,x_to,x_cc,body)
'''
