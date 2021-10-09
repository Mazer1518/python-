'''
    猜数字游戏：
        需求：
            1.系统产生一个随机数，
            2.用户从键盘输入数据，与随机数进行比对
                2.1 若大了，温馨提示：大了
                2.2 若小了，提示：小了
                2.3 提示：恭喜您，猜中！

        技术选型：
            1.随机数技术
                import random
                random.randint(开始数据，结束数据)
            2.键盘输入技术
                name = input()
            3.判断技术：多分支判断
                if....else
                if...elif.....elif....else
            4.循环技术
                while 条件：
    任务：
        加上金币赌博功能。
            初始化有5000金币，没猜错一次，扣500金币。
            10机会，钱扣完为止。
            在机会过程中，若猜中，奖励5000金币。
            然后询问，是否继续？是，否。
'''
import random
money = 5000

def game(money):
    # 1. 让系统产生一个随机数
    data = random.randint(0,1000) # 22
    print(data)
    count = 0
    money2 = 500
    money3 = 10000
    print("欢迎体验本游戏，您当前拥有money：",money,"输错一次扣除：",money2)
    print("您可以选择加注，若加注，失败一次扣除1000，成功后可得30000")
    chose = input("您是否需要加注：1：是, 2,:否")
    chose = int(chose)
    # 2.循环的让用户去猜
    i = 1
    if chose == 1:
        money2 = money2 * 2
        money3 = money3 * 3
        print("恭喜您加注成功")
    else:
        print("很遗憾您错过了一次发财的机会")

    while i <= 10:

        if money > money2:
            print("您的钱足够您挥霍了！")
        else:
            print("穷鬼，再输裤衩都输没了！")

        count = count + 1
        num = input("请输入您要猜的数字：")# "22"   "23"
        num = int(num) # "22"  -->  22
        if num > data:
            money = money - money2
            print("大了！","当前money:",money)

        elif num < data:
            money = money - money2
            print("小了！","当前money：",money)

        else:
            money = money + money3
            print("恭喜，猜中了！本次幸运数字为：",data,"，本次猜了",count,"次！","当前money：",money)
            print("赢了这么多钱，再来一局呗！")
            chose1 = input("1:是，2：否")
            chose1 = int(chose1)
            if chose1 == 1:
                game(money)
            else:
                print("客官下次再来啊！")
            break  # 终止循环

        i = i + 1
game(money)


















