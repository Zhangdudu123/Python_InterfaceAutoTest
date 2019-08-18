"""
 ProjectName：Duobei001
 ModuleName：operation_json
 Author：DaXiangCai
 Encoding：utf-8
 Time：2019-08-08 21:32
"""

import json

# fp = open("../dataconfig/login.json")
# data = json.load(fp)
# print(data['login'])

class OperetionJson:

    def __init__(self):
        self.data = self.read_data()


    #读取json文件
    def read_data(self):
        with open("../dataconfig/login.json") as fp:
            data = json.load(fp)
            return data


    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]


if __name__ == '__main__':
    opjson =  OperetionJson()
    print(opjson.get_data('login1'))











