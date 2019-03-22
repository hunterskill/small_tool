#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Hunter Yi
#判断进程是否是活动的

import os
cmd='ps aux | grep LDAPConvert.jar'
pro=os.popen(cmd).read()
processName = '/root/tools/LDAPConvert.jar'
if processName in pro:
    print('在运行')
else:
    print('没运行')
    cmd='java -jar /root/tools/LDAPConvert.jar > LDAPConvert.log &'
#    cmd='cd /'
    r=os.system(cmd)
    print(r)
    if r==0:
        print('重启成功')
    else:
        print('重启失败')

