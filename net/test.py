import os
import operator
import time
import datetime
from sqlconnect import Sqldata
from dateutil.relativedelta import relativedelta

def timeadd(linitdate,month):
    #linitdate = "2017-07-18"
    date_time = datetime.datetime.strptime(linitdate, '%Y-%m-%d')
    now = date_time - relativedelta(months=-month)
    return now.strftime('%Y%m%d ')
t = timeadd('2002-2-1',1)
print(t)