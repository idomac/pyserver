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


def func_sleep(func_name, sleep_default_time=10):
    while True:
        print '000000'
        try:
            func_name()
        except Exception,e:
            print e
        time.sleep(sleep_default_time)
        print '1111111'