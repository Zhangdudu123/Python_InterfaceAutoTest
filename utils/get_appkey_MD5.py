# -*- coding: utf-8 -*-
# @ProjectName：Duobei001
# @Author: DaXiangCai
# @File: get_appkey_MD5.py
# @Time: 2019-08-16 16:43

import hashlib
from collections import OrderedDict

from six import iteritems


def getAppKeyMD5(data):
    appkey = 'a1b9ad6181f7424bad8fb2b7a2c3c6d5'

    sorted_data = OrderedDict(sorted(iteritems(data)))

    # convert all str to unicode
    for k, v in sorted_data.items():
        if isinstance(v, str):
            # sorted_data[k] = v.decode('utf-8', errors='ingore')
            sorted_data[k] = v
    raw = '&'.join(
        '%s=%s' % (k, v) for k, v in sorted_data.items()) + appkey


    # hash = hashlib.md5()
    # hash.update(raw.encode(encoding='utf-8'))

    #md5 = hash.hexdigest()
    # return md5

    m = hashlib.md5(raw.encode('utf-8', errors='ingore'))
    sign = m.hexdigest()
    data['sign'] = sign
    return data

    print('MD5加密前为 ：' + raw)
    print('MD5加密后为 ：' + m.hexdigest())