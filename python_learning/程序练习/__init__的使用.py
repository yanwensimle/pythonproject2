class Student:
    def __init__(self):
        i = 0
        for i in range(0, 10):
            print(f"当前录入第{i + 1}名学生信息，共要录入10名学生信息")
            self.name = input("请输入学生姓名：")
            self.age = input("请输入学生年龄：")
            self.address = input("请输入学生地址：")
            print(f"第{i + 1}名学生信息录入完成，信息为：【学生姓名：{self.name}，学生年龄：{self.age}，学生住址：{self.address}")
            i += 1
            print(f"当前录入第{i + 1}名学生信息，共要录入10名学生信息")


stu = Student()
print(stu)
