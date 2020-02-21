import os
from os import path
from wenjian import Fileop
from settings import Settings
from sqlconnect import Sqldata
import datetime


file_path = r'F:\maildir\beck-s\deleted_items\13'
Fileop().read_file(file_path,5)

print('##### done #####')

