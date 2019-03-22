#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Hunter Yi
#判断进程是否是活动的

import os
cmd='ps aux | grep monitor.py'
pro=os.popen(cmd).read()
processName='LDAPConvert.jar'
for line in pro.splitlines():
 print(line)
 if processName in line:
     print('在运行')

else:
    print('没运行')
    cmd='java -jar LDAPConvert.jar > LDAPConvert.log &'
#    cmd='cd /'
    r=os.system(cmd)
    print(r)
    if r==0:
        print('重启成功')
    else:
        print('重启失败')

