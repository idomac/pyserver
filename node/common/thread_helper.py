#!/usr/bin/env python
#-*- coding:utf-8 -*-

import threading
import time

__author__ = 'quanix'

def thread_start_func(func,args=(),daemon=True):
    '''
    启动线程
    :param func:
    :param args:
    :param daemon:
    :return:
    '''
    thread = threading.Thread(target=func,args=args)
    thread.setDaemon(daemon)
    thread.start()
