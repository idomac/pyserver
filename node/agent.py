import argparse
import os
import sys

__author__ = 'quanix'


class MyDaemon(object):

    def test(self):
        print "Hello Test"

    def run(self):
        print 'Hello World'


if __name__ == "__main__":
    myDaemon = MyDaemon()
    parser = argparse.ArgumentParser()

    parser.add_argument('cmd', default="start", help='start, stop, restart')
    parser.add_argument('-p', '--pidfile', default="./proc/daemon.pid")

    args = parser.parse_args()
    pidpath = os.path.abspath(args.pidfile)
    dirname = os.path.dirname(pidpath)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    if 'start' == args.cmd:
        pass
    elif 'stop' == args.cmd:
        pass
    elif 'restart' == args.cmd:
        pass
    else:
        print 'Unknow command'
        sys.exit(2)