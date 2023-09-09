import json
from typing import List

from data_define import Record
from 数据分析案例.data_define import Record


class Filereader:# 定义一个读取文件的抽象类
    def reder_data(self):# 定义一个读取数据的抽象方法
        pass


class Txet_filereder(Filereader):# 定义一个读取txet文件的类
    def __init__(self, path):# 构造一个读取文件路径的方法
        self.path = path

    def reder_data(self):# 构造一个读取文件数据的方法
        f = open(self.path, "r", encoding="UTF-8")
        record_list: List[Record] = []
        for line in f.readlines():# f.readlines将txet文件中的数据逐行读出，封装在列表中，然后通过for循环，读取每一行的数据
            line = line.strip()# 将字符串中开头和结尾的空格，换行符的去掉
            data_list = line.split(",")# 将字符串以“，”分割开，并封装进列表中
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            # print(record_list)
            record_list.append(record)



        f.close()
        return record_list

class Json_filereder(Filereader):
    def __init__(self, path):
        self.path = path

    def reder_data(self):
        f = open(self.path, "r", encoding="UTF-8")
        # print(type(f))
        # print(f.read())
        record_list: List[Record] = []

        for line in f.readlines():
            # print(type(line))
            data_dict = json.loads(line)# 将json数据转换为字典
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])

            record_list.append(record)


        f.close()
        return record_list

if __name__ == "__main__":
    txet_filereader = Txet_filereder("D:/360MoveData/Users/百慕大小海豚/Desktop/python学习资料/课件/第13章/2011年1月销售数据.txt")
    list1 = txet_filereader.reder_data()
    json_filereader = Json_filereder("D:/360MoveData/Users/百慕大小海豚/Desktop/python学习资料/课件/第13章/2011年2月销售数据JSON.txt")
    json_filereader.reder_data()
    list2 = json_filereader.reder_data()
    for l in list1:
        # print(type(l))
        print(l)
    for l in list2:
        print(l)