"""
 ProjectName：Duobei001
 ModuleName：commonUtil
 Author：DaXiangCai
 Encoding：utf-8
 Time：2019-08-10 17:39
"""
#coding:utf-8
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否再另一个字符串中
        str_one:查找的字符串
		str_two：被查找的字符串
        :return:
        '''
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
