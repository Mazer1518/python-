'''
    需求：
        购物流程。
        1.商品在货架上
        2.空的购物车
        3.自己的初始化资金
    技术选型：
        1.容器
            列表： []
        2.循环技术
            while
            for i in  enumerate(li)
        3.判断
        4.键盘输入
    任务：
    [10张老干妈：1折优惠券，20张联想电脑5折优惠券,15张华为优惠券0.6]
    开始买东西之前，提示是否要抽一张优惠券。
        若是：随机给一张，最终要进行使用优惠券的进行结算。
        若否：正常买东西
'''
from collections import Counter


def shop():
    import random
    answer = input("是否要进行抽取优惠券？")
    if answer == "是":
        num = random.randint(1, 45)
        if num <= 10:
            print("您抽到了一张老干妈1折优惠券！")
        elif 10 < num < 30:
            print("您抽到了一张华为手环6折优惠券！")
        else:
            print("您抽到了一张联想电脑5折优惠券！")
    else:
        print("好的")
    # 1.准备商品
    shop1 = [
        ["lenovo PC", 5000],
        ["Mac pc", 12000],
        ["HUAWEI  WATCH PRO 20", 2000],
        ["机械革命", 15000],
        ["老干妈", 7.5],
        ["卫龙辣条", 3],
        ["西瓜", 2]
    ]
    # 2. 初始化钱包
    money = input("请输入您的余额：")
    money = int(money)  # "200000" --> 200000

    # 3.空的购物车
    mycart = []

    # 4.买东西
    i = 0
    while i <= 20:
        # 4.1 展示商品
        for key, value in enumerate(shop1):
            print(key, value)
        # 4.2 请输入您想要的商品
        chose = input("亲输入您想要的商品编号：")  # "1"
        # 4.3
        if chose.isdigit():
            chose = int(chose)
            # 4.4 先判断是否存在该商品
            if chose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                # 4.5 判断您的余额是否足够
                if money < shop1[chose][1]:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
                    # 4.6 将商品添加到购物车 ，余额减去对应的钱
                    mycart.append(shop1[chose])
                    if answer == "是":
                        if chose == 0:
                            answer1 = input("是否有优惠券？")
                            if answer1 == "是":
                                money = money - shop1[chose][1] * 0.5
                            else:
                                money = money - shop1[chose][1]
                        if chose == 2:
                            answer2 = input("是否有优惠券？")
                            if answer2 == "是":
                                money = money - shop1[chose][1] * 0.6
                            else:
                                money = money - shop1[chose][1]
                        if chose == 4:
                            answer2 = input("是否有优惠券？")
                            if answer2 == "是":
                                money = money - shop1[chose][1] * 0.1
                            else:
                                money = money - shop1[chose][1]
                    else:
                        money = money - shop1[chose][1]

                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
        elif chose == "q" or chose == "Q":
            print("拜拜了，您嘞！欢迎下次光临！")
            break
        else:
            print("对不起，您输入有误，请重新输入！")
        i = i + 1

    # 打印购物小条
    print("以下是您的购物小条，请拿好：")
    for key, value in enumerate(mycart):
        print(key,value)
    print("本次余额还剩：￥", money)


shop()
