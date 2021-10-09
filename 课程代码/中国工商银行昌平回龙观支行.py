'''
    中国工商银行账户管理系统：
'''
import random

# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库
'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平回龙观支行        *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    # 1.判断数据库是否已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if username in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))


def add_money():
    account = int(input('请输入账号：'))
    if account in bank:
        money = int(input('请输入要存贮的金额：'))
        bank[account]["money"] += money
    else:
        print("账号输入错误")
        return False


def take_money():
    account = int(input('请输入账号：'))
    if account not in bank:
        print('账号不存在')
    else:
        password = input('请输入密码：')
        if password != bank[account]["password"]:
            print('密码不正确')
        else:
            takemoney1 = int(input('请输入要取出的金额：'))
            if takemoney1 > bank[account]["money"]:
                print("余额不足")
            else:
                bank[account]["money"] -= takemoney1


def trans_money():
    account1 = int(input('请输入转出的账号：'))
    account2 = int(input('请输入转入的账号：'))
    result1 = account1 or account2 in bank
    if result1 == False:
        print("账号错误")
    else:
        password1 = input('请输入转出账户的密码：')
        if password1 != bank[account1]["password"]:
            print("密码错误")
        else:
            money1 = int(input('请输入需要转出多少金额：'))
            if bank[account1]["money"] < money1:
                print('余额不足！')
            else:
                bank[account1]["money"] -= money1
                bank[account2]["money"] += money1


def find_bank():
    account = int(input('请输入账号：'))
    if account not in bank:
        print('该用户不存在')
    else:
        password = input('请输入密码')
        if password != bank[account]["password"]:
            print('密码错误')
        else:
            print('账号：', account)
            print('密码：', password)
            print('余额：', bank[account]["money"], '元')
            print('用户居住地址：', bank[account]["country"], bank[account]["province"], bank[account]["street"],
                  bank[account]["gate"])
            print('当前的开户行：', bank_name)


while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        add_money()
    elif chose == "3":
        take_money()
    elif chose == "4":
        trans_money()
    elif chose == "5":
        find_bank()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")
