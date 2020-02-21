from sqlconnect import Sqldata
from ldatrain import Model_lda
from multiprocessing import Pool
from refer.print_ctrl import ProgressBar
import datetime
import time

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


start = datetime.datetime.now()
count = Sqldata().data_num()[0][0]

bar  = ProgressBar(total=count)

Sqldata().sql_check()
def pro_main(i):
    Model_lda().train(i)
    end =datetime.datetime.now()
    print('正在处理第%s条数据'% i)
    print((end-start).seconds,'S')



if __name__ == '__main__':
    print(count)
#    for  i in range(10):
#        pro_main(i)

    p =Pool(8)
    for i in range(count):
        p.apply_async(pro_main,args=(i,))
       # time.sleep(1)
        if i == 6:
            break

  #      bar.move()
 #       bar.log()
    p.close()
    p.join()
    end =datetime.datetime.now()
    print('all done')
    print((end-start).seconds)













#$          pass
  #        for i in range(0,10):




'''
#  结果处理
    topic = ldamodel.show_topics(num_topics=1,num_words=3)
    data=topic[0][1]
    dat = data.split('+')
    str=''
    for i in  dat:
        s = (i.split('*'))[1]
        Fileop().file_check(sender,s)
    print("写入数据到 %s 中....." % sender)
    endtime=datetime.datetime.now()
    print((endtime-start).seconds)

end = datetime.datetime.now()
print('共用时间：',(end-start).seconds,'s')
 '''
