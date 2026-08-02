def func(**kwargs):
    print(kwargs, type(kwargs))

func(name="张三", age=20, gender="男")
# 输出：{'name': '张三', 'age': 20, 'gender': '男'}  <class 'dict'>