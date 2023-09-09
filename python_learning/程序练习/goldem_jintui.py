# 进退试算法
h = 0.1
a1 = 0


def f(x):
    result = 3 * x ** 3 - 5 * x + 9
    return result

f1 = f(a1)
a2 = a1 + h
f2 = f(a2)
if f1 > f2:
    h = 2 * h
    a3 = a2 + h
    f3 = f(a3)
else:
    h = -h
    a3 = a1
    f3 = f1
    a1 = a2
    f1 = f2
    a2 = a3
    f2 = f3
    h = 2 * h
    a3 = a2 + h
    f3 = f(a3)
while f3 <= f2:
    a1 = a2
    f1 = f2
    a2 = a3
    f2 = f3
    h = 2 * h
    a3 = a2 + h
    f3 = f(a3)
if h > 0:
    a = a1
    b = a3
    print("单峰区间为({0:.1f},{1})".format(a, b))
else:
    a = a3
    b = a1
    print("单峰区间为({0:.1f},{1})".format(a, b))
# 黄金分割法
Lambda = 0.618
Epsilon = 0.01
x1 = b - Lambda * (b - a)
f1 = f(x1)
x2 = a + Lambda * (b - a)
f2 = f(x2)
if f1 > f2:
    a = x1
    x1 = x2
    f1 = f2
    x2 = a + Lambda * (b - a)
    f2 = f(x2)
else:
    b = x2
    x2 = x1
    f2 = f1
    x1 = b - Lambda * (b - a)
    f1 = f(x1)
while b - a > Epsilon:
    if f1 > f2:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + Lambda * (b - a)
        f2 = f(x2)
    else:
        b = x2
        x2 = x1
        f2 = f1
        x1 = b - Lambda * (b - a)
        f1 = f(x1)
X = 0.5 * (b + a)
print(f"极值点为：{X}")
