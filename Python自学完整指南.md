# Python 自学完整指南

这是一份从零基础到中小型项目的系统路线。请边读边运行代码，每学完一个主题完成一个小项目。

## 一、目标与方法

你将学习变量、流程控制、数据结构、函数、模块、异常、文件、面向对象、测试、Git、数据库、网络和工程化。建议每天 60—90 分钟，遵循“理解概念、手写代码、修改代码、完成练习、总结错误”的循环。

## 二、环境准备

检查环境：

    python --version
    python -m pip --version

第一个程序：

    name = input("你的名字：")
    print(f"你好，{name}！")

保存为 hello.py，运行 python hello.py。建议使用 VS Code 或 PyCharm，并熟悉终端和调试器。

虚拟环境：

    python -m venv .venv
    source .venv/bin/activate
    .venv\\Scripts\\activate
    python -m pip install --upgrade pip
    python -m pip freeze > requirements.txt
    deactivate

建议结构：

    my_project/
    ├── README.md
    ├── requirements.txt
    ├── src/my_project/
    ├── tests/
    ├── data/
    └── .gitignore

## 三、基础语法

Python 使用缩进表示代码块，通常使用 4 个空格。变量和函数使用 snake_case，类使用 PascalCase，常量使用 UPPER_CASE。

    age = 18
    height = 1.75
    is_student = True
    name = "小明"
    nothing = None

基本类型包括 int、float、bool、str、list、tuple、dict、set 和 None。使用 type(value) 查看类型，使用 int、float、str、bool 进行转换。

运算符：+、-、*、/、//、%、**；比较：==、!=、>、<、>=、<=；逻辑：and、or、not。is 判断对象身份，in 判断成员关系。

## 四、字符串

    text = "Python programming"
    print(text[0], text[-1], text[0:6])
    print(text.strip(), text.lower(), text.upper())
    print(text.replace("Python", "Java"))
    print("Python" in text)

重点方法：strip、split、join、replace、find、count、startswith、endswith。优先使用 f-string：

    name, score = "小王", 95.567
    print(f"{name}的成绩是 {score:.1f} 分")

## 五、条件与循环

    score = 86
    if score >= 90:
        level = "优秀"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"

    for number in range(1, 6):
        print(number)

    total = 0
    number = 1
    while number <= 100:
        total += number
        number += 1

break 结束循环，continue 跳过本轮。熟悉 range、enumerate、zip。

## 六、核心数据结构

列表有序且可修改，常用 append、insert、remove、pop、sort：

    items = ["苹果", "香蕉"]
    items.append("橙子")
    items.insert(0, "梨")
    items.remove("香蕉")
    last = items.pop()
    items.sort()

元组通常表示不希望修改的数据：

    point = (10, 20)
    x, y = point

字典保存键值映射：

    user = {"name": "小李", "age": 20}
    user["city"] = "杭州"
    email = user.get("email", "未填写")
    for key, value in user.items():
        print(key, value)

集合自动去重，支持并集、交集和差集。推导式：

    squares = [x * x for x in range(10)]
    even = {x for x in range(20) if x % 2 == 0}

理解可变对象与不可变对象，避免无意共享引用。

## 七、函数

    def average(numbers):
        """返回数字序列的平均值。"""
        if not numbers:
            raise ValueError("numbers 不能为空")
        return sum(numbers) / len(numbers)

函数可以有默认参数、关键字参数、*args 和 **kwargs。不要把列表、字典等可变对象作为默认参数，应使用 None 后在函数内创建。尽量通过参数和返回值传递数据，少用全局变量。

## 八、模块、包与异常

脚本入口：

    def main():
        print("程序开始")

    if __name__ == "__main__":
        main()

异常处理：

    try:
        value = int(input("请输入整数："))
    except ValueError:
        print("输入格式不正确")
    else:
        print(value * 2)
    finally:
        print("操作结束")

只捕获能够处理的具体异常，不要用空 except 隐藏问题。主动抛出异常时提供清晰信息。遇到错误先阅读 traceback，定位文件、行号和最后一行异常类型。

## 九、文件与数据

优先使用 pathlib：

    from pathlib import Path
    path = Path("notes.txt")
    path.write_text("第一行\n第二行\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")

大文件逐行读取，并明确指定 UTF-8 编码。JSON 使用 json.dump 和 json.load；CSV 使用 csv.reader 或 csv.DictReader。处理文件时考虑路径、权限、编码和文件不存在。

## 十、面向对象

    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self._balance = balance

        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("金额必须为正数")
            self._balance += amount

        @property
        def balance(self):
            return self._balance

核心概念：类、对象、属性、方法、封装、继承、多态和组合。实际开发优先使用组合，只有确实存在“是一种”关系时使用继承。学习 dataclasses 简化数据对象。

## 十一、进阶特性

生成器使用 yield 按需产生数据，适合大数据流。装饰器可以增加日志、计时、权限等行为，使用 functools.wraps 保留原函数信息。

继续学习：迭代器协议、上下文管理器、闭包、类型标注、模式匹配、正则表达式、异步编程。高级特性应服务于可读性和可维护性。

## 十二、标准库

重点掌握：

- pathlib、os、shutil：路径和文件。
- datetime、zoneinfo：日期时间。
- json、csv、re：数据与文本。
- collections：Counter、defaultdict、deque。
- itertools、functools：迭代与函数工具。
- logging：日志；argparse：命令行。
- sqlite3：轻量数据库；concurrent.futures：并发。

日志示例：

    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("程序启动")

## 十三、测试、质量与 Git

安装并运行 pytest：

    python -m pip install pytest
    pytest

测试示例：

    from calculator import add

    def test_add():
        assert add(2, 3) == 5

测试覆盖正常、边界和错误情况。逐步使用 ruff 做检查和格式化，使用类型标注辅助发现问题。遵循 PEP 8，命名清晰、函数短小、避免重复。

Git 基础：git init、git status、git add、git commit、git log。gitignore 应排除虚拟环境、缓存、构建产物、日志和密钥。

## 十四、数据库、网络与 Web

SQLite 使用 sqlite3，SQL 必须参数化，避免 SQL 注入。网络请求必须设置超时、检查状态码、处理连接错误并保护 API 密钥。

Web 学习顺序：HTTP、JSON、REST、Flask 或 FastAPI、数据库、认证、部署。理解请求、响应、状态码、路由和序列化。

线程适合 I/O 等待，多进程适合 CPU 密集任务，asyncio 适合大量异步 I/O。先测量瓶颈再并发化。

## 十五、项目路线

入门：猜数字、计算器、单位转换器、记账本、通讯录。

初级：命令行待办事项、批量文件整理器、CSV 成绩分析器、公开网页信息采集器。

中级：任务管理 API、SQLite 管理系统、自动化报表生成器、带测试日志配置的完整应用。

每个项目应包含 README、安装说明、使用示例、测试、异常处理、日志、配置说明和 gitignore。先完成最小可运行版本，再重构和扩展。

## 十六、12 周计划

| 周次 | 内容 | 任务 |
|---|---|---|
| 1 | 环境、变量、类型 | 个人信息程序 |
| 2 | 条件、循环、随机数 | 猜数字 |
| 3 | 字符串、列表、元组 | 文本统计 |
| 4 | 字典、集合、推导式 | 通讯录 |
| 5 | 函数、模块、作用域 | 重构通讯录 |
| 6 | 文件、JSON、CSV | 记账本 |
| 7 | 异常、调试、日志 | 完善错误处理 |
| 8 | 类、继承、数据类 | 业务模型 |
| 9 | 标准库、命令行 | 文件工具 |
| 10 | 测试、Git、规范 | 补测试和 README |
| 11 | HTTP、数据库、第三方库 | 小型 API |
| 12 | 综合项目与复盘 | 完整作品 |

## 十七、错误排查

- SyntaxError：检查括号、冒号、引号和缩进。
- NameError：检查变量拼写和定义顺序。
- TypeError：检查类型和函数参数。
- ValueError：检查值的格式。
- KeyError：检查字典键，必要时使用 get。
- IndexError：检查索引范围。
- FileNotFoundError：检查当前工作目录和路径。

流程：阅读 traceback → 定位文件和行号 → 查看上下文 → 构造最小复现 → 一次只改一个因素 → 重新测试。

## 十八、检查清单

- [ ] 能解释可变对象与不可变对象。
- [ ] 能熟练使用列表、字典、集合和推导式。
- [ ] 能写有参数、返回值和文档字符串的函数。
- [ ] 能拆分模块并管理虚拟环境。
- [ ] 能读写 UTF-8、JSON 和 CSV。
- [ ] 能处理具体异常并记录日志。
- [ ] 能设计简单类和数据类。
- [ ] 能编写并运行自动化测试。
- [ ] 能使用 Git 保存历史。
- [ ] 能完成独立项目并写 README。

## 十九、方向选择

数据分析：NumPy、pandas、Matplotlib、Jupyter。Web 后端：FastAPI 或 Flask、SQL、认证和部署。自动化：文件处理、浏览器自动化、定时任务。人工智能：NumPy、PyTorch、数据处理和模型调用。工具与运维：命令行、日志、进程、网络和容器。

不要同时学习所有方向。先选择一个方向完成真实项目，再补充相关知识。Python 的核心能力不是背完语法，而是把问题拆成数据、函数和流程，用可验证、可维护的代码解决。

