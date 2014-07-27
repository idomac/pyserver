#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from util import fileUtil

__author__ = 'quanix'

conf_dir = os.path.dirname(os.path.abspath(__file__))



def _get_file_path(file_name, init_content=''):
    file_path = conf_dir + '/' + file_name
    if not fileUtil.exists(file_path):
        fileUtil.create_file(file_path)
        fileUtil.write_file(file_path, init_content)
    return file_path


LOG_FILE_PATH = _get_file_path('log4python.ini')
CONF_FILE_PATH = _get_file_path('conf.conf')
AGENT_CONF_FILE_PATH = _get_file_path('agent_conf.conf')
JOB_CONF_FILE_PATH = _get_file_path('job_conf.conf',init_content=str({}))
