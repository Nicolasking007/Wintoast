#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# *******************************************
# @File : demo.py
# @Author : Nicolas-kings
# @CreateTime : 2022/10/25 11:14:52
# Github : https://github.com/Nicolasking007
# @Desc : 
# -------------------------------------------


import os
from win11toast import toast
from winotify import Notification


# toast = Notification(app_id='D:\Program Files (x86)\DingDing\DingtalkLauncher.exe',
#                      title='***',
#                      icon=r"" + os.getcwd() + "/logo.ico",
#                      msg='晚上***游戏',
#                      duration='long')
# toast.show()


image = {
    'src': r"" + os.getcwd() + '/water.gif',
    'placement': 'hero'
}

res = toast('Hello', 'Hello from Python', image=image, app_id = 'D:\Program Files (x86)\Tencent\WeChat\WeChat.exe')
print('res', res)