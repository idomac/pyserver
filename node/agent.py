import argparse
import os
import sys
from common.daemon import Daemon
from main import main

__author__ = 'quanix'


class MyDaemon(Daemon):

    def __init__(self, pid):
        super(self.__class__, self).__init__(pid)

    def run(self):
        main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', default="start", help='start, stop, restart')
    parser.add_argument('-p', '--pidfile', default="./proc/daemon.pid")

    args = parser.parse_args()
    pidpath = os.path.abspath(args.pidfile)
    dirname = os.path.dirname(pidpath)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    mydaemon = MyDaemon(pidpath)
    if 'start' == args.cmd:
        mydaemon.start()
    elif 'stop' == args.cmd:
        pass
    elif 'restart' == args.cmd:
        pass
    else:
        print 'Unknow command'
        sys.exit(2)