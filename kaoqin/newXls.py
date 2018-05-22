import xlrd
from xlutils.copy import copy
import os
import os.path

rootdir = "./"
path=rootdir
def foundxls(rootdir):
    global  path
    for lists in os.listdir(rootdir):
        if lists[-3:]=='xls':
            path = os.path.join(rootdir,lists)
            continue
foundxls(rootdir)
print(path)

dirpath="./报表"
def mkdir(dirpath):
    folder=os.path.exists(dirpath)

    if not folder:
        os.makedirs(dirpath)




def app():
    try:
        rb=xlrd.open_workbook(path,formatting_info='true')
    except Exception as e:
        print("找不到\n1_标准报表.xls")
    rs=rb.sheet_by_index(2)
    nrows=rs.nrows
    wb=copy(rb)
    if(nrows%2!=0):
        ws=wb.get_sheet(2)
        ws.write(nrows,0," ")
    try:
        wb.save('./报表/崭新的报表.xls')
    except Exception as e:
        print("无法生成可执行文件,可能系统空间不足",endcoding="")

if __name__=="__main__":
    mkdir(dirpath)
    app()