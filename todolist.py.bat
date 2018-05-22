import xlrd
import sys,xdrlib
import json



def read_xls():
    print('hello')
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\1_标准报表.xls')     #获取文档
    booksheet = workbook.sheet_by_name('考勤记录')      #获取工作表
    return booksheet


def getData(booksheet):
    nrows=booksheet.nrows
    row=5
    while row < nrows:
        rowData=booksheet.row_values(row)
        print(rowData)
        name = booksheet.cell_value(row - 1, 10)
        print(name + ':')
        day = 1
        for nrow in rowData:
            strDay=str(day)
            print('day' + strDay+':',end='')
            if(nrow==''):
                print('null,',end='')
                day += 1
                continue
            i = 0
            while i < len(nrow):
                data = []
                data.append(nrow[i:i+5])
                print(nrow[i:i + 5]+',',end='')
                i += 5
                day += 1
            print
        row+=2
        day=1








if __name__=="__main__":
    booksheet=read_xls()
    getData(booksheet)

