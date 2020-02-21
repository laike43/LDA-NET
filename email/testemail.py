#python mail

import os
import email

#邮件文件的存放位置
path = r'G:\email\email\10'

#读取文件
def read_mail(path):
    if os.path.exists(path):
        with open(path) as fp:
            for line in fp:
                print(line)
    else:
        not_find_file()

#打开一个文件   
def open_file(path):
    if os.path.exists(path):
        return open(path, 'r')
    else:
        not_find_file()

#创建消息对象
def get_message(path):
    if os.path.exists(path):
        fp = open_file(path)
        return email.message_from_file(fp)
    else:
       not_find_file()

#获取subject对象
def get_subject(path):
    if os.path.exists(path):
        message = get_message(path)
        return message.get('subject')
    else:
        not_find_file()

#解析subject对象
def parse_subject(msg):
    if msg != None:
        subject = msg.get('subject')
        #header = email.Header.Header(subject)
        #decode_h = email.Header.decode_header(header)
        #return decode_h[0][0]
    else:
        empty_obj()

#获取发件人邮箱   
def get_from(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get("from"))[1]
    else:
        empty_obj()

#获取收件人邮箱
def get_to(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('to'))[1]
    else:
        empty_obj()


#获取邮件的生成时间
def get_date(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('date'))[1]
    else:
        empty_obj()

#获取邮件的生成版本
def get_mime_version(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('mime-version'))[1]
    else:
        empty_obj()

#获取邮件的文本类型
def get_content_type(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('content-type'))[1]
    else:
        empty_obj()

#获取邮件的邮件的id
def get_message_id(msg):
    if msg != None:
        return email.utils.parseaddr(msg.get('message-id'))[1]
    else:
        empty_obj()


#文件不存在
def not_find_file():
    print('文件不存在!')

#msg is empty
def empty_obj():
    print('msg is empty!')
    
def main():
    global PATH
    PATH = 'E:\\test_mail.eml'
    print(PATH)
    msg = get_message(PATH)
    #print(msg)
    print('#' * 50)
    print('subject:{}'.format(get_subject(PATH)))
    print('#' * 50)
    print(parse_subject(msg))
    print('#' * 50)
    print('from:{}'.format(get_from(msg)))
    print('to:{}'.format(get_to(msg)))
    print('date:{}'.format(get_date(msg)))
    print('mime-version:{}'.format(get_mime_version(msg)))
    print('content-type:{}'.format(get_content_type(msg)))
    print('message-id:{}'.format(get_message_id(msg)))

if __name__ == '__main__':
    main()