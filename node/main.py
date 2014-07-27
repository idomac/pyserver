import time
from common import thread_helper
from service import sync_config_service

__author__ = 'quanix'

def init():
    thread_helper.thread_start_func(loop())



def loop():
    while True:
        sync_config_service.sync()
        time.sleep(60)


def scan_job():
    print 'scan_job'


def main():
    print '------'
    init()
    scan_job()


if __name__ == "__main__":
    main()