# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: request.py
# @Time: 2019-08-18 15:23

import requests
import json

class HttpClient:

    def __init__(self):
        pass


    def send_post(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.post(url=request_url, data=json.dumps(request_params), headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=json.dumps(request_params), headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.post(url=request_url, data=json.dumps(request_params), headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.post(url=request_url, data=json.dumps(request_params), headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return response


    def send_get(self,request_url,request_params,request_header=None):
        response = None
        if request_header == None:
            if request_url in 'https':
                response = requests.get(url=request_url, data=json.dumps(request_params), headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=json.dumps(request_params), headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        else:
            if request_url in 'https':
                response = requests.get(url=request_url, data=json.dumps(request_params), headers=request_header,verify=False).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
            else:
                response = requests.get(url=request_url, data=json.dumps(request_params), headers=request_header).text
                print('request_header：'+str(request_header) + '\n' + 'request_url：'+str(request_url) + '\n' + 'request_data：'+json.dumps(request_params,indent=2))
        return response



    def request(self,request_method,request_url,request_params=None,request_header=None):
        response = None
        if request_method == 'post':
            response = self.send_post(request_url,request_params,request_header)
        else:
            response = self.send_get(request_url,request_params,request_header)
        dict_response = json.loads(response)
        return json.dumps(dict_response, ensure_ascii=False, sort_keys=True, indent=2)
        # return json.dumps(response,ensure_ascii=False,sort_keys=True,indent=2)
        # return response


if __name__ == '__main__':
    url = 'https://api_dev.duobeiyun.com/p/v1/project'
    data = {
        'partner': '388816c02a514c568b5119513b9bd651',
        'timestamp': '11111111111',
        'sign': ''
    }

    http = HttpClient()
    h = http.request('post',url,data)
    print(h)



























