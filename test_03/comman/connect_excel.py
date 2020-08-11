import  datetime as dt
import xlrd
import xlutils as xlutils
import xlwt

"""
在 xlutils的init文件中导入这些功能才能使用
from .compat import *
from .copy import *
from .display import *
from .filter import *
from .margins import *
from .save import *
from .styles import *
from .view import *
"""
import time


class connect_excel:

    def __init__(self,excel_name,sheet_name):
        self.excel_name=excel_name
        self.sheet_name=sheet_name


    def read_date(self):
        data=xlrd.open_workbook(self.excel_name)
        sheet=data.sheet_by_name(self.sheet_name)
        #获取第一行的数据
        row_first=sheet.row_values(0)
        data_list=[]
        #获取其余行的数据
        for i  in range(1,sheet.nrows):
            rows = sheet.row_values(i)
            bb=dict(zip(row_first,rows))
            data_list.append(bb)
        print(data_list)
        return data_list

    def  write_excel(self ,row, column, value):
        data = xlrd.open_workbook(self.excel_name)
        table = data.sheet_by_name(self.sheet_name)
        workbook = xlutils.copy(data)
        worksheet = workbook.get_sheet(self.sheet_name)
        worksheet.write(row-1, column-1, value)
        workbook.save(self.excel_name)

    #写入最后一行
    def  write_excel_lastline(self,value):
        # current_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #打开excel表格
        data = xlrd.open_workbook(self.excel_name)
        workbook = xlutils.copy(data)
        #得到表格的sheet的名称
        worksheet = workbook.get_sheet(self.sheet_name)
        #获取表格sheet的队形
        table = data.sheet_by_name(self.sheet_name)
        rowNum = table.nrows  #行数
        #样式
        style = xlwt.XFStyle()

        worksheet.write(rowNum, 0, value)
        worksheet.write(rowNum, 1, time.strftime("%Y-%m-%d %X", time.localtime()), style)
        workbook.save(self.excel_name)

if __name__ == '__main__':
    cases=connect_excel("/Users/xiaoff/python/pytest/test_03/data/test_new.xlsx","Sheet1").read_date()


