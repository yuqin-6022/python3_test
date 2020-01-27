#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/1/27 23:51
# @Author    : Shawn Li
# @FileName  : handlers.py
# @IDE       : PyCharm
# @Blog      : 暂无

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
