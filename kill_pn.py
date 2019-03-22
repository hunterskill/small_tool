#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:Hunter Yi
import os
cmd='ps aux | grep LDAPConvert.jar'
pro=os.popen(cmd).read()

processName='LDAPConvert.jar'
for line in pro.splitlines():
 print(line)
 if processName in line:
     print('是',line.split()[1])
     pid=line.split()[1]
     cmd_kill='kill -s 9 %s'%pid
     try:
         r=os.system(cmd_kill)
         if r==0:
             print("成功杀死进程")
         else:
             print("没成功")
     except Exception as e:
         print("有异常"+e)
