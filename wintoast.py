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
app_id = data['MAIN']['app_id']


# 获取方式： 管理员权限  输入：Get-StartApps 即可查询appid


def reminder(name):
    for i in pylist:
        params = {
            'title': i['title'],
            'body': i['body'],
            'app_id': app_id,
            'duration': i['duration']
        }
        if name == 'AdaptiveText':
            pass
        elif name == 'InlineImage':
            params['icon'] = r"" + os.getcwd() + i['icon']
            params['image'] = r"" + os.getcwd() + i['image']
        elif name == 'InlineButton':
            params['image'] = r"" + os.getcwd() + i['image']
            params['duration'] = 'long'
            button = {
                'activationType': 'protocol',
                'arguments': i['launch'],
                'content': i['label']
            }
            params['button'] = button
        elif name == 'HeroImage':
            image = {
                'src': r"" + os.getcwd() + i['image'],
                'placement': 'hero'
            }
            params['image'] = image
        elif name == 'HeroButton':
            image = {
                'src': r"" + os.getcwd() + i['image'],
                'placement': 'hero'
            }
            button = {
                'activationType': 'protocol',
                'arguments': i['launch'],
                'content': i['label']
            }
            params['image'] = image
            params['button'] = button
        elif name == 'Audio':
            params['icon'] = r"" + os.getcwd() + i['icon']
            params['audio'] = i['audio']
        else:
            pass
        toast(**params)


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
