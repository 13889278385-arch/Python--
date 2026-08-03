# def func(a=[]):
#     a.append(1)
#     print(a)

# func()  # [1]
# func()  # [1, 1]
# func()  # [1, 1, 1]






# def func(a=[]):
#     print(id(a))

# func()
# func()
# # 两次输出的 id 相同





def func(a=None):
    # 如果没有传入参数，就新建空列表
    if a is None:
        a = []

    a.append(1)
    print(a)
    print(id(a))

func()  # [1]
func()  # [1]
func(a=[10086])

# 每次调用时，`a is None` 都会成立，于是函数内部都会创建一个全新的空列表。


def func(a=None):
    if a is None:
        a = []

    a.append(1)
    print(a)
    print(id(a))
    return a

x = func()
y = func()

print(x)
print(y)
print(x is y)



# 输出结果
# (base) PS E:\desktop test\Python--> & "E:\Python Install Space address\python.exe" "e:/desktop test/Python--/func_arg_rules.py"
# [1]
# 1945274793216
# [1]
# 1945274793216
# [1]
# 1945274793216
# [1]
# 1945276235392
# [1]
# [1]
# False