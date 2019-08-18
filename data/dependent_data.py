# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: dependent_data.py
# @Time: 2019-08-18 15:23

from utils.operation_excel import OperationExcel
from base.request import HttpClient
from data.get_data import GerData
from jsonpath_rw import jsonpath,parse
import json

class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GerData()

    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        httpclient = HttpClient()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        #header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        result = httpclient.request(method,url,request_data)
        return json.loads(result)

    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        print(type(depend_data),"depend_data:",depend_data)
        print(type(response_data),"response_data:",response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]






