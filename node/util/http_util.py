#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import httplib


def http_post(url, port, action, timeout=30, params=None, method='POST', headers=None):
    try:
        conn = httplib.HTTPConnection(url, port, timeout)
        conn.request(method, action, params, headers)
        r = conn.getresponse()
        response = r.read()
        conn.close()
    except Exception, e:
        raise e
    return response


def http_get(url, port, action, timeout=30, method='GET'):
    try:
        conn = httplib.HTTPConnection(url, port, timeout)
        conn.request(method, action)
        r = conn.getresponse()
        response = r.read()
        conn.close()
    except Exception, e:
        raise e
    return response