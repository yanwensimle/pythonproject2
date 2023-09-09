""""
name = "黑马程序员"
message = "学IT，来：%s" % name
print(message)
num1 = 10
num2 = 45.598
print("%5d" % num1)
print("%.2f" % num2)
"""
""""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司:{name}｝,股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是%.1f,经过%d的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
user_name = input("你的名字是？")
print("您好！，%s" % user_name)
user_type = input("您的用户类型是？")
print("您是尊贵的：% s" % user_type,"用户，欢迎您登陆！")

"""
# height = int(input("欢迎来到儿童游乐园，请输入您的身高："))
#
# if height >= 120:
#     print("您的身高超过120cm，需要补票10元")
# else:
#     print("您的身高不足120cm,可以免费游玩！")
#
# print("祝您玩的愉快！")
# num = int(input("请输入我心里想的数字："))
#
# if num != 10:
#     input("不对，再猜一次")
# if num != 10:
#     input("不对，在才最后一次")
# if num != 10:
#     input("sorry,全部猜错了，我想的是10")
# else:
#     print("恭喜你答对了！")
""""
import random
num = random.randint(1, 10)
guess_num = int(input("猜测的数字"))

if guess_num == num:
    print("恭喜你第一次就猜对了")
else:
    if guess_num > num:
        print("你猜的数大了")
    else:
        print("你猜的数小了")

        guess_num = int(input("猜测的数字"))

        if guess_num == num:
            print("恭喜你第二次猜对了")
        else:
            if guess_num > num:
                print("你猜的数大了")
            else:
                print("你猜的数小了")

            guess_num = int(input("猜测的数字"))

            if guess_num == num:
                print("恭喜你第三次猜对了")
            else:
                print("不好意思，你三次机会都用完了")
"""
# i = 0
# a = 0
# while i < 100:
#     i += 1
#     a += i
# print(a)
""""
import random
num = random.randint(1, 100)
guess_num = int(input("猜测的数字"))
i = 1
while guess_num != num:
    i += 1
    if guess_num > num:
        print("你猜的数大了")
    else:
        print("你猜的数小了")
    guess_num = int(input("猜测的数字"))
print(f"恭喜你第{i}次就猜对了")
"""
"""
i = 0
while i < 100:
    i += 1
    print(f"今天是准备像小美表白的第{i}天")
    j = 0
    while j < 10:
        j += 1
        print(f"这是今天第{j}次给小美送花")
    print("小美我喜欢你")
print(f"第{i}天表白成功了")
"""

# 九九乘法表

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#
#         print(f"{j}*{i}={j*i}\t",end='')
#         j += 1
#     i += 1
#     print()


# name = "heima is a brand of itcast"
# count = 0
# for x in name:
#    # print(x)
#     if x=="a":
#         count += 1
# print(count)
# count = 0
# for x in range(875):
#     if x % 2 == 0:
#         count += 1
# print(f"共有{count}个偶数")


# i = 0
# for i in range(100):
#     i += 1
#     print(f"今天是准备像小美表白的第{i}天")
#
#     for j in range(10):
#
#         print(f"这是今天第{j}次给小美送花")
#     print("小美我喜欢你")
# print(f"第{i}天表白成功了")


# 九九乘法表
# for i in range(1,10):
#
#     for j in range(1,i+1):
#
#         print(f"{j}*{i}={j*i}\t",end='')
#
#
#     print()

# import random
# count = 1
# sum_salary = 10000
# salary = 1000
# for i in range(1,20):
#     num = random.randint(1, 11)
#     if num < 5:
#         print(f"员工{i},绩效分{num},小于5，不发工资，下一个")
#     else:
#
#         sum_salary -= salary * count
#         print(f"向员工{i}发放工资{salary}元，账户剩余工资{sum_salary}元")
#         if sum_salary == 0:
#             print("工资发完了，下个月领取吧")
#             break

# def exit():
#     global name
#     name = input("请输入您的姓名：")
# def mean_menu():
#     print(f"{name}你好，欢迎来到黑马银行，请选择操作")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     global num
#     num = input("请输入您的选择：")
# def balance():
#     print("------查询余额------")
#     print(f"您的余额为:{money}元")
#     mean_menu()
# def deposit():
#     amount_deposit = int(input("请输入您的存款金额："))
#     global money
#     money += amount_deposit
#     print("-------存款--------")
#     print(f"您好,您存入{amount_deposit}元成功\n您的余额剩余：{money}元")
#     mean_menu()
# def withdraw():
#     amount_withdraw = int(input("请输入您的取款金额："))
#     global money
#     money -= amount_withdraw
#     print("-------取款--------")
#     print(f"您好,您取走{amount_withdraw}元成功\n您的余额剩余：{money}元")
#     mean_menu()
# money = 5000000
# exit()
# mean_menu()
# i = 0
# while i == 0:
#     if int(num) == 1:
#         balance()
#     if int(num) == 2:
#         deposit()
#     if int(num) == 3:
#         withdraw()
#     if int(num) == 4:
#         exit()
#         money = 5000000
#         mean_menu()
# my_list = [20,25,21,23,22,20]
# my_list1 = [29,33,30]
# my_list.append(31)
# print(my_list)
# my_list.extend(my_list1)
# print(my_list)
# number1 = my_list.pop(0)
# print(number1)
# number2 = my_list.pop(-1)
# print(number2)
# number3 = my_list.index(31)
# print(number3)
# my_tubple = ("周杰伦",11,["football","music"])
# year = my_tubple.index(11)
# print(f"年龄是：{year}")
# name = my_tubple[1]
# print(f"名字是：{name}")
# del my_tubple[2][1]
# print(my_tubple)
# my_tubple.insert([2][0],"coding")
# print(my_tubple)
# my_str = "itheima itcast buxuegu"
# number = my_str.count("it")
# print(f"it的个数为:{number}")
# my_new_str = my_str.replace(" ","|")
# print(my_new_str)
# my_list = my_new_str.split("|")
# print(my_list)
# my_str = "万过薪月，员序程马黑来，nohtyp学"
# my_new_str = my_str[-10:-15:-1]
# print(my_new_str)
# my_list = ["黑马程序员","传播智客","黑马程序员","传播智客","itheima","itcast","itheima","itcast","best"]
# my_set = set()
# for i in my_list:
#     my_set.add(i)
# print(my_set)

# my_dict = {
#     "王理红":{"部门":"科技部","工资":3000,"级别":1},
#     "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#     "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
#     "张学有":{"部门":"科技部","工资":4000,"级别":1},
#     "刘的话":{"部门":"市场部","工资":6000,"级别":2}
#           }
# for name in my_dict:
#     if my_dict[name]["级别"] == 1:
#        my_dict[name]["级别"] = 2
#        my_dict[name]["工资"] += 1000
# print(my_dict)
# def add(x,y):
#     result = x+y
#     return 0
# number = add(5,6)
# print(number)

# def user_info(**agrs):
#     print(agrs)
# user_info(name="小明",age=11,gender="女")
# 统计word.txt中的"itheima"的个数
# import time
# count = 0
# with open("D:/pythonProject/word.txt","r",encoding = "UTF-8") as f:
#     for line in f:
#         count += line.count("itheima")
# print(count)
# f = open("D:/pythonProject/word.txt","r",encoding = "UTF-8")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# time.sleep(500)

# import my_utlis.str_utlis
# import my_utlis.file_utlis
# my_str = "heimachengxuyuan"
# data = "\n黑马程序员"
# my_utlis.str_utlis.str_reverse(my_str)
# my_utlis.str_utlis.sub_str(my_str, 2, 3)
# my_utlis.file_utlis.append_to_file("D:/pythonProject/word.txt", data)
# my_utlis.file_utlis.print_file_info("D:/pythonProject/word.txt")
from pyecharts.charts import Line

line = Line()
line.add_xaxis(["中国", "英国", "美国"])
line.add_yaxis("GDP", [20, 30, 60])
line.render()
