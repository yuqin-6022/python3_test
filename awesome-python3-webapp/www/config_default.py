#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/1/27 18:11
# @Author    : Shawn Li
# @FileName  : config_default.py
# @IDE       : PyCharm
# @Blog      : 暂无

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www',
        'password': 'www',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
