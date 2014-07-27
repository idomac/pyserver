#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os
import conf

__author__ = 'quanix'

class Logger:
    def __init__(self):
        try:
            logging.config.fileConfig(conf.LOG_FILE_PATH)
        except IOError, io_err:
            dir_name = os.path.dirname(io_err.filename)
            os.makedirs(dir_name)
            logging.config.fileConfig(conf.LOG_FILE_PATH)
        self.logger = logging.getLogger('allInfo')

    def get_logger(self):
        return self.logger

