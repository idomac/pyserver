#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import base64
import md5


def get_md5(content):
    return md5.new(content).hexdigest()


def base64_encode(content):
    return base64.b64encode(content)


def base64_decode(content):
    return base64.b64decode(content)