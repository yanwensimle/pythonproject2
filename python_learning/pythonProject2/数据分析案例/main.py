from typing import List

from file_define import Filereader, Txet_filereder, Json_filereder
from data_define import Record

text_file_reader = Txet_filereder("D:/360MoveData/Users/百慕大小海豚/Desktop/python学习资料/课件/第13章/2011年1月销售数据.txt")
json_file_reader = Json_filereder("D:/360MoveData/Users/百慕大小海豚/Desktop/python学习资料/课件/第13章/2011年2月销售数据JSON.txt")

jan_data: List[Record] = text_file_reader.reder_data()
feb_data: List[Record] = json_file_reader.reder_data()
# 将2个月份的数据合并为1个list来存储
all_data: List[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for record in all_data:
    # 判断在字典data_dict中是否有key:record.date,如果没有，就在data_date中加入key为record.date,value为record.money的字典元素，
    # 然后从all_data中取下一个列表元素，再次进行判断，在data_dict中是否有record.date的key值，如果有，将关键字相同的value值相加。
    if record.date in data_dict:
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)
