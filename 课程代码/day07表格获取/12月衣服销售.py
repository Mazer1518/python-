import xlrd

# 打开
wb = xlrd.open_workbook(filename=r"12月份衣服销售数据.xlsx")
# 2.选中用户管理选项卡
st = wb.sheet_by_index(0)
# 3.获取所有行  所有列
rows = st.nrows
cols = st.ncols

# 横向获取
for i in range(rows):  # 6
    data = st.row_values(i)
    # print(data)
# 列查询
for i in range(cols):
    data = st.col_values(i)

sals_name = st.col_values(1)  # 服装名称
sals_money = st.col_values(2)  # 价格/件
sals_num = st.col_values(4)  # 销售量/每日
del sals_name[0]
del sals_money[0]
del sals_num[0]
list_sals = list(map(lambda x, y: x * y, sals_money, sals_num))  # 每件衣服的销售额
list_salsNum = [round(i / sum(sals_num) * 100, 2) for i in sals_num]  # 每件衣服的销售占比（件数）
list_salsNum = [str(i) + "%" for i in list_salsNum]

list_salsmoney = [round(i / sum(list_sals) * 100, 2) for i in list_sals]
list_salsmoney = [str(i) + "%" for i in list_salsmoney]
# 12月份销售总金额
print("销售总金额为；", round(sum(list_sals), 2))
# 每件衣服的销售占比（件数）
print("每件衣服销售量占比：")
print(sals_name)
print(list_salsNum)
# 每件衣服的销售额占比
print("每件衣服销售额占比为：")
print(list_salsmoney)

