import os
from os import path
from wenjian import Fileop
from settings import Settings
from sqlconnect import Sqldata
import datetime



path = Settings.path
num=0
start = datetime.datetime.now()

Sqldata().sql_check_message()
Sqldata().sql_check_inmessage()
Sqldata().sql_check_outmessage()
Sqldata().sql_check_recip()
Sqldata().sql_check_employee()
for root,dirs,files in os.walk(path): 
   # for dir in dirs: 
   #     print (os.path.join(root,dir)) 
    for file in files:
        num = num + 1
        file_path =  os.path.join(root,file)
        Fileop().read_file(file_path,num)
        end =datetime.datetime.now()
        print('##### done #####',num)
        #print((end-start).seconds)













