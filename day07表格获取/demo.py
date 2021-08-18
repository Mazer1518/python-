'''
    容器类型：
        变量：
        列表、元组、字典
        excel读
        mysql数据库
        1.安装组件：xlrd
            python  -m pip install xlrd==0.9.3
                xlrd不支持新xlsx
                0.9.3都支持xls,xlsx
        2.打开工作薄

        3.选中要操作的选项卡可

        4.通过方法来获取里面的表格数据

'''

import xlrd



# 1.打开
wb = xlrd.open_workbook(filename=r"用户统计数据.xlsx")


# 2.选中用户管理选项卡
st = wb.sheet_by_name("用户管理")

# 3.获取所有行  所有列
rows = st.nrows
cols = st.ncols

# 横向获取
for i in range(rows): # 6
    data = st.row_values(i)
    print(data)

# 列查询
for i in range(cols):
    data = st.col_values(i)
    print(data)


# 平均年龄 ， 总工资多少
data = st.col_values(1)
sals = st.col_values(2)
print("平均年龄：",(sum(data[1:])  //  len(data[1:])))
print("总薪资",round(sum(sals[1:]) , 2))
print("总共有",rows,"行数据,有",cols,"列数据！")




















