"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/16 8:59
E-mail  : 506615839@qq.com
File    : 2020_08_16.py
============================
"""
import openpyxl
class CaseData:
    pass

class ReadExcel:
    def __init__(self,filename,sheetname):
        '''
        :param filename: 文件地址
        :param sheetname:表单
        '''
        self.filename=filename
        self.sheetname=sheetname

    def open(self):
        '''打开工作簿，选中表单'''
        self.workbook=openpyxl.load_workbook(self.filename)
        self.sheet=self.workbook[self.sheetname]

    def save(self):
        '''保存工作簿'''
        self.workbook.save(self.filename)

    def close(self):
        '''关闭工作簿'''
        self.workbook.close()

    def read_excel(self):
        self.open()
        rows = list(self.sheet.rows)
        title=[]
        for r in rows[0]:
            title.append(r.value)
        cases=[]
        for row in rows[1:]:
            data=[]
            for item in row:
                data.append(item.value)
            datas=dict(zip(title,data))
            cases.append(datas)
        self.close()
        return cases

    def read_excel_obj(self):
        self.open()
        rows = list(self.sheet.rows)
        title = []
        for i in rows[0]:
            title.append(i.value)
        cases = []
        for row in rows[1:]:
            data = []
            for item in row:
                data.append(item.value)
            datas = list(zip(title, data))
            casedata=CaseData()
            for k,v in datas:
                setattr(casedata,k,v)
            cases.append(casedata)
        self.close()
        return (cases)

    def write(self,row,column,value):
        '''回写'''
        self.open()
        self.sheet.cell(row=row,column=column,value=value)
        self.save()
        self.close()





if __name__ == '__main__':
    from common.contains import DATADIR
    import os
    data_path=os.path.join(DATADIR,'cases.xlsx')
    excel=ReadExcel(data_path, 'register')
    data=excel.read_excel()
    print(data)