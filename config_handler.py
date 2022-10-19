#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ***************************************
# @File    : config_handler.py
# @CreatTime    : 2022/9/15 14:44
# @Author  : Nicolas-kings
# @Github  : https://github.com/Nicolasking007
# @Desc :   读写yaml文件方法封装
# ---------------------------------------

import yaml


class YamlHandler:
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding='utf-8'):
        """读取yaml数据"""
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        """向yaml文件写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


# if __name__ == '__main__':
#     data = {
#         "user": {
#             "username": "vivi",
#             "password": "123456"
#         }
#     }
#     # 读取config.yaml配置文件数据
#     read_data = YamlHandler('../config/config.yaml').read_yaml()
#     # 将data数据写入config1.yaml配置文件
#     write_data = YamlHandler('../config/config1.yaml').write_yaml(data)
#     print(read_data)
