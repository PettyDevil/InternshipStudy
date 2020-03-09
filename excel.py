# 操作excel表格

import xlwt

# txt先确定路径然后通过open方法创建并打开文件
# 获得一个工作表操作对象
wb=xlwt.Workbook()
# 获取一个工作簿操作对象
sheet=wb.add_sheet("测试")
# 写入内容（行标，列表，内容）
sheet.write(0,0,'qwer')
sheet.write(4,5,'aaaa')
# 直接写入一行数据（不可以）
# 字体
style=xlwt.XFStyle() # 创建一个初始的样式
font=xlwt.Font()  # 创建一个初始字体样式
font.bold=True
# 合并单元格、单个单元格的大小
style.font=font # 将加粗字体放入style中
sheet.write(0,1,'哈哈',style)
# 保存当前的工作表
wb.save('output/test.xls')