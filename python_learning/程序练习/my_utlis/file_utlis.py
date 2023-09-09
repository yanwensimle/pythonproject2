def print_file_info(file_name):
    name = file_name
    print(f"文件路径为：{name}")
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except Exception as e:
        print(f"文件出现异常，原因是：{e}")
        f = open(file_name, "w", encoding="UTF-8")
    else:
        print(f"文件内容为：{f.read()}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    name = file_name
    print(f"文件路径为：{name}")
    f = open(file_name, "r", encoding="UTF-8")
    print(f"追加数据前{file_name}里的数据为:{f.read()}")
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f = open(file_name, "r", encoding="UTF-8")
    print(f"追加数据后{file_name}里的数据为：{f.read()}")
    f.flush()
    f.close()
