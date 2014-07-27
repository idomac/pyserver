#!/usr/bin/env python
# -*- coding:utf-8 -*-
import string
import conf
from util import fileUtil,encrypt_util
from util.remote import get_response

__author__ = 'quanix'


def request_config(url_dic,md5_val):
    host, port = url_dic.get('host'), url_dic.get('port')
    action = url_dic.get('action') + '?md5=%s' % md5_val
    return get_response(host, port, action)

def request_update_config(md5_val):
    '''
    配置文件更新信息请求
    :param md5_val:
    :return:
    '''
    agent_conf_dic = eval(fileUtil.read_file(conf.AGENT_CONF_FILE_PATH))
    if agent_conf_dic:
        update_url_list = agent_conf_dic.get('update_url')
        for update_url_dic in update_url_list:
            try:
                response_dic = request_config(update_url_dic,md5_val)
                if response_dic:
                    return response_dic
            except Exception,e:
                print e
    else:
        print 'no update config'


def process_conf(conf_dic):
    fileUtil.write_file(conf.CONF_FILE_PATH, conf_dic)


def process_script_conf(script_dic):
    pass

def sync():
    try:
        md5_value = string.strip(fileUtil.read_file(conf.CONF_FILE_PATH))
        md5_value.replace('\n', '')

        print 'start to request update config with md5:%s' % md5_value

        response = request_update_config(md5_value)

        if response:
            process_conf(response.get('conf'))
            process_script_conf(response.get('script'))
        else:
            print 'request update config no response'

    except Exception, e:
        print e


if __name__ == '__main__':
    sync()