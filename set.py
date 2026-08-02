squares = [x * x for x in range(10)]
even = {x for x in range(20) if x % 2 == 0}

''' # 1. squares = [x * x for x in range(10)]
格式：列表推导式 []
range(10)：0,1,2,3,4,5,6,7,8,9

x*x：每个数字求平方
最终结果：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
作用：快速生成一个列表，替代冗长 for 循环。

2. even = {x for x in range(20) if x % 2 == 0}
格式：集合推导式 {}
大括号 = 集合（自带自动去重）

遍历 0~19 所有数字
条件 if x%2==0：只保留偶数
结果：{0,2,4,6,...,18}
'''