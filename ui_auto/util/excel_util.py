import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "E:/ui_auto/config/ddt_data.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        #获取excel sheet table
        self.table = self.data.sheets()[index]
        #获取行数

        #获取excel 数据，按照每行一个list，添加到一个大的list 里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                row = self.table.row_values(i)
                result.append(row)
            return result
        return None

    #获取excel 行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >=1:
            return rows
        return None

    #获取单元格的数据
    def get_col_values(self,row,col):
        if self.get_lines() > row:
            data= self.table.cell(row,col).value
            return data
        return None
    #写入数据
    def write_value(self,row,col,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save(self.excel_path)

if __name__ == '__main__':
    ex = ExcelUtil("E:/ui_auto/config/keyword.xls")
    print(ex.get_col_values(2,2))
