from sqlconnect import Sqldata

from fileop import Fileop
import datetime
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


#start = datetime.datetime.now()
count = Sqldata().data_num()[0][0]
with  open('txt', 'a') as f:
    for  i in range(count):
        sql = Sqldata().sql_conn(i)
        data = sql[0][0][0]
        print(data)
        str = '正在处理第{0}条数据'.format(i)
        #f.write(str)
        f.write(data)
        f.write('\n')



        print('正在处理第%s条数据'% i)





print('all done')










