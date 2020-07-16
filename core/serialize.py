#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json


def deserialization(content: json):
    """
    反序列化
        json对象 -> python数据类型
    """
    return json.loads(content)


def serialization(content, ensure_ascii=True):
    """
    序列化
        python数据类型 -> json对象
    """
    return json.dumps(content, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    pass