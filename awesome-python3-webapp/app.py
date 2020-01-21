#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time      : 2020/1/21 17:18
# @Author    : Shawn Li
# @FileName  : app.py
# @IDE       : PyCharm
# @Blog      : 暂无

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>awesome</h1>', headers={'Content-type': 'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
