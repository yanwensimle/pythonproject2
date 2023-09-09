def str_reverse(s):
    print(f"字符串s为：{s}")
    s = s[::-1]
    print(f"反转后字符串s为：{s}")


def sub_str(s, x, y):
    """

    :param s:
    :param x:
    :param y:
    :return:
    """
    s = s[x:y:]
    print(f"切片后s为：{s}")
