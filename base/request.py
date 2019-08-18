# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: request.py
# @Time: 2019-08-18 15:23

import time

from utils.get_appkey_MD5 import getAppKeyMD5
import requests
import json

class HttpClient:

    def __init__(self):
        pass


    def send_post(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.post(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return json.loads(response)

    def send_get(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.get(url=request_url, data=request_params, headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=request_params, headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return response



    def request(self,request_method,request_url,request_params=None,request_header=None):
        response = None
        if request_method == 'post':
            response = self.send_post(request_url,request_params,request_header)
        else:
            response = self.send_get(request_url,request_params,request_header)
        return json.dumps(response, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == '__main__':
    url = 'https://api_dev.duobeiyun.com/p/v1/project'
    data = {
        'partner': '4a82946d15b2465581dfc5218097c209',
        'timestamp': int(time.time() * 1000),
    }

    http = HttpClient()
    h = http.request('post',url,getAppKeyMD5(data))
    print('response：',h)



























