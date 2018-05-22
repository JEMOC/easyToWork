import xlrd
import sys,xdrlib
import os




os.remove('fo.txt')
fo=open('fo.txt','w',encoding='utf-8')



def read_xls():
    print('hello')
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\1_标准报表.xls')     #获取文档
    booksheet = workbook.sheet_by_name('考勤记录')      #获取工作表
    return booksheet


def getData(booksheet):
    nrows=booksheet.nrows
    row=5
    while row < nrows:      #行循环
        name = booksheet.cell_value(row - 1, 10)        #获取员工姓名
        print(name + ':')


        fo.write(name+':')                             #写入姓名
        fo.write('\n')


        rowData=booksheet.row_values(row)
        print(rowData)
        day = 1
        newData = []
        for nrow in rowData:        #列循环
            print('day' + str(day)+':',end='')
            if(nrow==''):
                print('null,',end='')
                day += 1
                continue
            i = 0
            data = []
            while i < len(nrow):        #分割时间戳
                data.append(nrow[i:i+5])
                print(nrow[i:i + 5]+',',end='')
                i += 5


            day += 1
            compute(data)
            print
            print(data)

            ######################
            fo.write(str(day)+'号:')
            fo.write('[')
            for item in data:
                fo.write('\'')      #文件输出
                fo.write(item)
                fo.write('\',')
            fo.write(']')
            fo.write('\n')
            print
            #####################

        row+=2
        day=1


def compute(timeList):
    morning = []
    afternoon = []
    night = []
    for times in timeList:
        time=int(times[0:2])
        min=int(times[3:6])
        if time in range(6,13):
            morning.append(times)
            continue

        if time in range(13,19):
            if time==13:
                afternoon.append(times)
                continue
            elif (time==18)&(min<15):
                afternoon.append(times)
                continue
            else:
                night.append(times)
                continue

        night.append(times)

    print('morning:', end='')
    print(morning)
    print('after:', end='')
    print(afternoon)
    print('night:', end='')
    print(night)



if __name__=="__main__":
    booksheet=read_xls()
    getData(booksheet)
    fo.colse()

