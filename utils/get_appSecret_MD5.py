# -*- coding: utf-8 -*-
# @ProjectName：Duobei001
# @Author: DaXiangCai
# @File: get_appSecret_MD5.py
# @Time: 2019-08-17 14:39

import hashlib
from collections import OrderedDict

from six import iteritems


def getAppSecretMD5(data):
    appSecret = '57e458173ec544cfb8c6b28d85165cb3'

    sorted_data = OrderedDict(sorted(iteritems(data)))

    # convert all str to unicode
    for k, v in sorted_data.items():
        if isinstance(v, str):
            # sorted_data[k] = v.decode('utf-8', errors='ingore')
            sorted_data[k] = v
    raw = '&'.join(
        '%s=%s' % (k, v) for k, v in sorted_data.items()) + appSecret


    # hash = hashlib.md5()
    # hash.update(raw.encode(encoding='utf-8'))

    #md5 = hash.hexdigest()
    # return md5

    m = hashlib.md5(raw.encode('utf-8', errors='ingore'))
    sign = m.hexdigest()
    data['sign'] = sign
    return data
