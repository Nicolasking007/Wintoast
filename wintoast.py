#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***************************************
# @File    : wintoast.py
# @CreatTime  : 2022/10/19 11:01
# @Author  : Nicolas-kings
# @Github  : https://github.com/Nicolasking007
# @Desc :
# ---------------------------------------

import time
import os
from winotify import Notification
from apscheduler.schedulers.blocking import BlockingScheduler
from config_handler import YamlHandler

data = YamlHandler('config.yaml').read_yaml()
pylist = data['content']
'''
代码实现每天9点开始定时，下午6点10分结束定时；
每天9，11，14，16，18时提醒喝水；
'''
app_id = data['MAIN']['app_id']
start_time = time.strftime('%Y-%m-%d ', time.localtime(time.time())) + data['MAIN']['start_time']
end_time = time.strftime('%Y-%m-%d ', time.localtime(time.time())) + data['MAIN']['end_time']


# 获取方式： 管理员权限  输入：Get-StartApps 即可查询appid


def reminder():
    hour = time.strftime("%H", time.localtime())
    for i in pylist:
        if hour == i['date']:
            toast = Notification(app_id=app_id,
                                 title=i['title'],
                                 msg=i['body'],
                                 icon=r"" + os.getcwd() + i['icon'],
                                 duration=i['duration'])
            if i['label'] is None:
                toast.show()
            else:
                toast.add_actions(label=i['label'],
                                  launch=i['launch'])
                toast.show()


if __name__ == '__main__':
    # 调试
    # reminder()

    # 定时执行
    scheduler = BlockingScheduler()
    # # 每天9，11，14，16，18时提醒喝水；
    scheduler.add_job(reminder, 'interval', minutes=30, start_date=start_time, end_date=end_time)
    # scheduler.add_job(reminder, 'cron', day_of_week='mon-fri', hour=8, minute=55, end_date=end_time)
    scheduler.start()
