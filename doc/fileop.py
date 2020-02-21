import os
from setting import Settings

class Fileop(object):
    def __init__(self):
        self.path = Settings.file_path

    def file_read(self,sender_path):
        file_path = self.path+sender_path
        with  open(file_path,'r') as f:
            print('文件读取')
            print(f.read())

    def file_write(self,file_path,data):
        with open(file_path,'a') as f:
            f.write(data)
            f.write('\n')
    def file_check(self,name,data):
        path = self.path + name
        self.file_write(path,data)
    def file_set_read(self,path):
        file_path ='./result/' + path
        topic = set()
        with open(file_path,'r') as f:
            for line in f.readlines():
                str = line.strip()
                topic.add(str)
        return topic

if __name__=='__main__':
    path = './result/01019@salespoint.dealerconnection.com'
    a=Fileop().file_set_read(path)
    print(a)


            







