#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  time;

#将时间写入文件

filename = 'write_data.txt'
timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#打印时间
print(timestr)
with open(filename,'a') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    f.write("现在时间是："+ timestr +".\n" )


