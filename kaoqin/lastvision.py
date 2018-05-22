import xlrd
import xlwt
from datetime import datetime


xls=xlrd.open_workbook('崭新的报表.xls',formatting_info='ture')
xls_sheet=xls.sheet_by_name('考勤记录')
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('考勤记录')

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER

borders=xlwt.Borders()
borders.left=1
borders.right=1
borders.top=1
borders.bottom=1
borders.bottom_colour=0x3A


def writeHead():
    font = xlwt.Font()
    font.bold = True
    font.name = '宋体'
    font.height = 400
    style = xlwt.XFStyle()
    style.font = font
    style.alignment = alignment
    worksheet.write_merge(0, 1, 0, 30, '考勤记录表', style)
    worksheet.write(2, 0, '考勤时间')
    worksheet.write(2, 2, xls_sheet.cell_value(2, 2))
    worksheet.write(2, 9, xls_sheet.cell_value(2, 9))
    worksheet.write(2, 11, xls_sheet.cell_value(2, 11))

def writeDay(ncols):
    style = xlwt.XFStyle()
    style.alignment = alignment
    style.borders = borders
    for day in range(1, ncols + 1):
        worksheet.col(day - 1).width = 1350
        worksheet.write(3, day - 1, day, style)

def writeInfo(rb_row,wb_row):
    worksheet.write(wb_row, 0, xls_sheet.cell_value(rb_row, 0))
    worksheet.write(wb_row, 2, xls_sheet.cell_value(rb_row, 2))
    worksheet.write(wb_row, 8, xls_sheet.cell_value(rb_row, 8))
    worksheet.write(wb_row, 10, xls_sheet.cell_value(rb_row, 10))
    worksheet.write(wb_row, 18, xls_sheet.cell_value(rb_row, 18))
    worksheet.write(wb_row, 20, xls_sheet.cell_value(rb_row, 20))

def writeTime(rb_row,wb_row):
    rowData = xls_sheet.row_values(rb_row + 1)
    day = 0
    workday = 0
    overtime = 0
    for data in rowData:
        if (data != ''):
            workday += 1
        worksheet.write(wb_row + 1, day, data)
        day += 1

def writeDate(rb_row,wb_row):
    return

def writeCount(rb_row,wb_row):
    return


def main():
    nrows = xls_sheet.nrows
    ncols = xls_sheet.ncols
    rb_row = 4
    wb_row= 4
    while rb_row < nrows:
        writeHead()
        writeDay(ncols)
        writeInfo(rb_row,wb_row)
        writeTime(rb_row,wb_row)
        writeDate(rb_row,wb_row)
        writeCount(rb_row,wb_row)
        rb_row+=2
        rb_row+=5


if __name__=="__main__":
    main()

    try:
        workbook.save('报告结果1.xls')
    except Exception as e:
        print("   请关闭\n报告结果.xls")