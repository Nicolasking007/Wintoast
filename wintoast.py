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
import schedule
# from winotify import Notification
from win11toast import toast
from apscheduler.schedulers.blocking import BlockingScheduler
from config_handler import YamlHandler

data = YamlHandler('config.yaml').read_yaml()
pylist = data['content']
'''
代码实现每天9点开始定时，下午6点10分结束定时；
每天9，11，14，16，18时提醒喝水；
两个list列表设置提醒内容
'''
app_id = data['MAIN']['app_id']


# start_time = time.strftime('%Y-%m-%d ', time.localtime(time.time())) + data['MAIN']['start_time']
# end_time = time.strftime('%Y-%m-%d ', time.localtime(time.time())) + data['MAIN']['end_time']


# 获取方式： 管理员权限  输入：Get-StartApps 即可查询appid


def reminder(name):
    for i in pylist:
        if name == 'AdaptiveText':
            toast(i['title'], i['body'], app_id=app_id,
                  duration=i['duration'])
        elif name == 'InlineImage':
            toast(i['title'], i['body'], app_id=app_id,
                  icon=r"" + os.getcwd() + i['icon'],
                  image=r"" + os.getcwd() + i['image'],
                  duration=i['duration'])
        elif name == 'InlineButton':
            toast(i['title'], i['body'], app_id=app_id,
                  image=r"" + os.getcwd() + i['image'],
                  duration='long',
                  button={'activationType': 'protocol', 'arguments': i['launch'],
                          'content': i['label']})
        elif name == 'HeroImage':
            image = {
                'src': r"" + os.getcwd() + i['image'],
                'placement': 'hero'
            }
            toast(i['title'], i['body'], app_id=app_id,
                  image=image,
                  duration=i['duration'])
        elif name == 'HeroButton':
            image = {
                'src': r"" + os.getcwd() + i['image'],
                'placement': 'hero'
            }
            toast(i['title'], i['body'], app_id=app_id,
                  image=image,
                  duration=i['duration'],
                  button={'activationType': 'protocol', 'arguments': i['launch'],
                          'content': i['label']})
        elif name == 'Audio':
            toast(i['title'], i['body'], app_id=app_id,
                  icon=r"" + os.getcwd() + i['icon'],
                  duration=i['duration'],
                  audio=i['audio'])


def run():
    for i in pylist:
        schedule.every().day.at(i['date']).do(reminder, i['type'])
        print(i['date'])

    while True:
        schedule.run_pending()
        time.sleep(30)


run()

# if __name__ == '__main__':
#     # 调试
#     run()


# 定时执行
# scheduler = BlockingScheduler()
# # # 每天9，11，14，16，18时提醒喝水；
# scheduler.add_job(reminder, 'interval', minutes=30, start_date=start_time, end_date=end_time)
# # scheduler.add_job(reminder, 'cron', day_of_week='mon-fri', hour=8, minute=55, end_date=end_time)
# scheduler.start()
