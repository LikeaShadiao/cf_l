import pymysql
import xlrd

"""
一、连接mysql数据库
"""
# 打开数据库连接
# conn = pymysql.connect(
#     host='localhost',  # MySQL服务器地址
#     user='root',  # MySQL服务器端口号
#     password='root',  # 用户名
#     charset='utf8',  # 密码
#     port=3308,  # 端口
#     db='test',  # 数据库名称
# )

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='dbtest1', charset='utf8mb4')

# 使用cursor()方法获取操作游标
c = conn.cursor()

"""
二、读取excel文件
"""
FilePath = 'hrs.xlsx'

# 1.打开excel文件
wkb = xlrd.open_workbook(FilePath)
# 2.获取sheet
sheet = wkb.sheet_by_index(0)  # 获取第一个sheet表['学生信息']
# 3.获取总行数
rows_number = sheet.nrows
# 4.遍历sheet表中所有行的数据，并保存至一个空列表cap[]
cap = []
for i in range(rows_number):
    x = sheet.row_values(i)  # 获取第i行的值（从0开始算起）
    cap.append(x)
print(cap)  # [['9022478', '郭赛', '男', 34.0, 'CS'], ['9022472', '林伟', '男', 36.0, 'MA'], ···]
cap = cap[1:]
print(cap)

"""
三、将读取到的数据批量插入数据库
"""
for Stu in cap:
    Sno = str(Stu[0])
    Sname = Stu[1]
    Ssex = Stu[2]
    Sage = Stu[3]
    Sdept = Stu[4]
    # 使用f-string格式化字符串，对sql进行赋值
    c.execute(f"insert into tb_emp(Sno,Sname,Ssex,Sage,Sdept) value ('{Sno}','{Sname}','{Ssex}','{Sage}','{Sdept}')")
conn.commit()
conn.close()
print("插入数据完成！")
