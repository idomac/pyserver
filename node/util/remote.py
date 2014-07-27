#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from util.http_util import http_get, http_post

__author__ = 'quanix'

def get_post_response(host, port, action, params,timeout=30, to_json=True):
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    response = http_post(host, port, action, timeout, params, headers=headers)
    if to_json:
        response = json.dumps(response)
    return response

def get_response(host,port,action,timeout=30,to_json=True):
    response = http_get(host, port, action, timeout)
    if to_json:
        response = eval(response)
    return response