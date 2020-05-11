"""
創建Excel文件

Version: 0.1
Author: 駱昊
Date: 2018-03-26
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
sheet = workbook.active
data = [
    [1001, '白元芳', '男', '13123456789'],
    [1002, '白潔', '女', '13233445566']
]
sheet.append(['學號', '姓名', '性別', '電話'])
for row in data:
    sheet.append(row)
tab = Table(displayName="Table1", ref="A1:E5")

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
sheet.add_table(tab)
workbook.save('./res/全班學生數據.xlsx')
