# -*- coding:utf-8 -*-
import xlrd
import xlwt



wb = xlrd.open_workbook("demo.xls")
wb1 = xlwt.Workbook()
sht = wb.sheet_by_name("Sheet1")

nrows = sht.nrows
print (nrows)
ncols = sht.ncols
print (ncols)

sht.write(2, 8, 'aruba')
wb.save("aruba.xls")
