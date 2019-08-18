# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: run_test.py
# @Time: 2019-08-18 19:18
from datetime import datetime
import time

from base.request import HttpClient
from utils.get_appkey_MD5 import getAppKeyMD5


class RunTest:

    def __init__(self):
        self.httpclient = HttpClient()
        self.now = datetime.now()


    def select_project(self):
        url = 'https://api_dev.duobeiyun.com/p/v1/project'
        data = {
            'partner': '4a82946d15b2465581dfc5218097c209',
            'timestamp': int(time.time() * 1000)     #int(time.mktime(self.now.timetuple()) * 1000)
        }
        result = self.httpclient.request('post',url,getAppKeyMD5(data))
        print("reponse：", result)

        t = int(time.time() * 1000)
        print(t)


if __name__ == '__main__':
    run = RunTest()
    run.select_project()