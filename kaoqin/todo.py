import xlrd
import xlwt
from datetime import datetime

xls=xlrd.open_workbook('./报表/崭新的报表.xls',formatting_info='ture')
xls_sheet=xls.sheet_by_name('考勤记录')
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('考勤记录')

nrows = xls_sheet.nrows
ncols = xls_sheet.ncols
flag='false'

borders=xlwt.Borders()
borders.left=1
borders.right=1
borders.top=1
borders.bottom=1
borders.bottom_colour=0x3A

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT

Data_style = xlwt.XFStyle()
Data_style.borders = borders
Data_style.alignment=alignment

def writeHead():
    font=xlwt.Font()
    font.bold=True
    font.name='宋体'
    font.height=400
    alignment=xlwt.Alignment()
    alignment.horz=xlwt.Alignment.HORZ_CENTER
    alignment.vert=xlwt.Alignment.VERT_CENTER

    style=xlwt.XFStyle()
    style.font=font
    style.alignment=alignment

    str_head='考 勤 记 录 表'

    worksheet.write_merge(0,1,0,30,str_head,style)

    worksheet.write(2,0,'考勤时间')
    worksheet.write(2,2,xls_sheet.cell_value(2,2))
    worksheet.write(2,9,xls_sheet.cell_value(2,9))
    worksheet.write(2,11,xls_sheet.cell_value(2,11))

def writeDays():        #写入日期
    style = xlwt.XFStyle()
    style.alignment=alignment
    style.borders=borders
    for day in range(1,ncols+1):
        worksheet.col(day-1).width=1350
        worksheet.write(3,day-1,day,style)

def writeInfo(rb_row,wb_row):       #写入人员信息
    worksheet.write(wb_row, 0, xls_sheet.cell_value(rb_row, 0))
    worksheet.write(wb_row, 2, xls_sheet.cell_value(rb_row, 2))
    worksheet.write(wb_row, 8, xls_sheet.cell_value(rb_row, 8))
    worksheet.write(wb_row, 10, xls_sheet.cell_value(rb_row, 10))
    worksheet.write(wb_row,18,xls_sheet.cell_value(rb_row,18))
    worksheet.write(wb_row,20,xls_sheet.cell_value(rb_row,20))

def writeData(rb_row,wb_row):       #写入时间
    rowData = xls_sheet.row_values(rb_row + 1)
    day=0
    workday=0
    for data in rowData:
        if(data!=''):
            workday+=1
        worksheet.write(wb_row + 1, day, data, Data_style)
        compute(data,wb_row,day)
        day += 1
        infostr1 = "\"上班\"&AF" + str(wb_row+2) + "&\"天+" + "加班\"&AF" + str(wb_row + 5) + "&\"小时\""
        infostr2 = "\"上班\"&AF" + str(wb_row + 2) + "&\"天\""
    strlate="sum(A"+str(wb_row+3)+":AE"+str(wb_row+3)+")"
    strearly="sum(A"+str(wb_row+4)+":AE"+str(wb_row+4)+")"
    strovertime="sum(A"+str(wb_row+5)+":AE"+str(wb_row+5)+")"
    worksheet.write(wb_row+1,31,workday)
    worksheet.write(wb_row+2,31,xlwt.Formula(strlate))
    worksheet.write(wb_row+3,31,xlwt.Formula(strearly))
    worksheet.write(wb_row+4,31,xlwt.Formula(strovertime))
    worksheet.write(wb_row, 22, xlwt.Formula(infostr1))


def compute(data,wb_row,day):       #计算入口
    times_list=[]
    ot=0
    i=0
    while i < len(data):  # 分割时间戳
        times_list.append(data[i:i + 5])
        i += 5
    lens = len(times_list)
    if lens ==4 or lens ==6:
        late=comLate(times_list[0],times_list[2])
        early=comEarly(times_list[1],times_list[3])
        worksheet.write(wb_row + 2, day,late)
        worksheet.write(wb_row + 3, day,early)
        if lens == 6 :
            ot=comOvertme(times_list[5])
            worksheet.write(wb_row+4,day,ot)
    else:
        return


def comOvertme(time):       #计算加班
    hour=int(time[0:2])
    min=int(time[3:6])
    t=datetime(2018,1,1,hour,min)
    ct=datetime(2018,1,1,18,30)
    ct1=datetime(2018,1,1,20,50)
    ct2=datetime(2018,1,1,21,25)
    ot=(t-ct).seconds/3600
    t1=(ct1-ct).seconds/3600
    t2=(ct2-ct).seconds/3600
    if ot > t1 and ot < t2:
        return 2.5
    elif ot > t2:
        return 3


def comLate(time1,time2):   #计算迟到
    hour1=int(time1[0:2])
    min1=int(time1[3:6])
    hour2 = int(time2[0:2])
    min2 = int(time2[3:6])
    t1=datetime(2018,1,1,hour1,min1)
    t2=datetime(2018,1,1,hour2,min2)
    ct1=datetime(2018,1,1,8,0)
    ct2=datetime(2018,1,1,13,30)
    if t1 > ct1:
        if t2 > ct2:
            return ((t1-ct1).seconds+(t2-ct2).seconds)/60
        else:
            return (t1-ct1).seconds/60
    else:
        if t2 >ct2:
            return (t2-ct2).seconds/60
        else:
            return 0

def comEarly(time1, time2):     #计算早退
    hour1 = int(time1[0:2])
    min1 = int(time1[3:6])
    hour2 = int(time2[0:2])
    min2 = int(time2[3:6])
    t1 = datetime(2018, 1, 1, hour1, min1)
    t2 = datetime(2018, 1, 1, hour2, min2)
    ct1 = datetime(2018, 1, 1, 12, 0)
    ct2 = datetime(2018, 1, 1, 18, 0)
    if t1 < ct1:
        if t2 < ct2:
            return ((ct1-t1).seconds+(ct2 -t2).seconds)/60
        else:
            return (ct1-t1).seconds/60
    else:
        if t2 < ct2:
            return (ct2-t2).seconds/60
        else:
            return 0


def Main():
    rb_row=4
    wb_row=4
    while rb_row <nrows:
        writeInfo(rb_row,wb_row)    #写入个人信息
        writeData(rb_row,wb_row)    #写入打卡时间
        rb_row+=2                   #原表格步进
        wb_row+=5                   #结果表步进

if __name__=="__main__":
    writeHead()
    writeDays()
    Main()
    try:
        workbook.save('./报表/报告结果1.xls')
    except Exception as e:
        print("   请关闭\n报告结果.xls",endcoding="")
