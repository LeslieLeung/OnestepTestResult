# -*- coding:utf-8 -*-
import xlrd

wb = xlrd.open_workbook("demo.xls")
sht1 = wb.sheet_by_name('Sheet1')

test = sht1.cell_value(2,8)
print(test)
