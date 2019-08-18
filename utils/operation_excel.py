# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: operation_excel.py
# @Time: 2019-08-18 15:23
import os

import xlrd
from xlutils.copy import copy

# data = xlrd.open_workbook('../dataconfig/data.xlsx')
# tables = data.sheets()[0]
# print(tables.nrows)
# # print(tables.cell_value(2,3))


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_path = os.path.abspath(os.path.dirname(__file__))
            self.file_name = os.path.join(self.file_path, '../dataconfig', 'data.xlsx')

            self.sheet_id = 0
        self.data = self.get_data()

    #获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某个一个单元格的内容
    def get_cell_velue(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,vaule):
        '''
        写入excel数据
        :param row:
        :param col:
        :param vaule:
        :return:
        '''
        #打开excel文件
        read_data = xlrd.open_workbook(self.file_name)
        #拷贝一份原来的excel
        write_data = copy(read_data)
        #获取第0个sheet页，
        sheet_data = write_data.get_sheet(0)
        #在某行某列的单元格内写入value
        sheet_data.write(row,col,vaule)
        #保存excel文件
        write_data.save(self.file_name)

    #根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    #根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                print('行号是：',num)
                return num
            num = num+1

    #根据对应的caseid找到对应行的内容
    def get_rows_data(self,casei_d):
        row_num = self.get_row_num(casei_d)
        rows_data = self.get_row_values(row_num)
        return rows_data


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers.get_cell_velue(1,2))


