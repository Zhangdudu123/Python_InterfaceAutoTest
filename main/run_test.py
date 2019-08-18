# -*- coding: utf-8 -*-
"""
 coding:UTF-8
 ProjectName：Duobei001
 ModuleName：run_test
 Author：DaXiangCai
 Time：2019-08-10 15:11
"""

import sys
sys.path.append("/Users/zhangwengao/PycharmProjects/Duobei001")
from base.request import HttpClient
from data.get_data import GerData
from utils.commonUtil import CommonUtil
from data.dependent_data import DependentData
from utils.send_email import SendEmail
class RunTest:

    def __init__(self):
        self.httpclient = HttpClient()
        self.data = GerData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()

    #程序执行的主入口
    def go_on_run(self):
        print("开始执行。。。")
        response = None
        pass_count = []
        fail_count = []

        rows_conut = self.data.get_case_lines()
        print(rows_conut)

        for i in range(1,rows_conut):

            is_run = self.data.get_is_run(i)
            #判断是否运行
            if is_run:
                request_url = self.data.get_request_url(i)
                request_method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect_data = self.data.get_expect_data(i)
                request_header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                #判断是否有依赖
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    #获取响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    #更新depend_response_data值
                    request_data[depend_key] = depend_response_data
                # 参数顺序不能错
                response = self.httpclient.request(request_method, request_url, request_data, request_header)
                print("response：",response)
                print('-----------------------------------------------------------')
                if self.com_util.is_contain(expect_data,response):
                    # print("测试通过：",'result中包含预期值'+expect)
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    # print("测试失败：",'result中不包含预期值'+expect)
                    self.data.write_result(i,response)
                    fail_count.append(i)
        # print('case执行成功数量:',len(pass_count))
        # print('case执行失败数量:',len(fail_count))
        #self.send_mai.send_main(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()





