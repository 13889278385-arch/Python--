# Python 中的 `**kwargs`：可变关键字参数与字典解包

## 一句话先记住核心

- `**kwargs` 用来接收任意多个关键字参数，并自动打包成字典（`dict`）。
- `kwargs` 只是约定俗成的名字，换成 `**data`、`**kv` 等也完全可以。
- 两个星号 `**` 才是关键。

## 一、基础写法：接收关键字参数

```python
def func(**kwargs):
    print(kwargs, type(kwargs))

func(name="张三", age=20, gender="男")
# 输出：{'name': '张三', 'age': 20, 'gender': '男'} <class 'dict'>
```

函数会把所有关键字参数自动打包成一个字典：

```python
kwargs == {
    "name": "张三",
    "age": 20,
    "gender": "男",
}
```

关键字名称会成为字典的键，对应的值会成为字典的值。

## 二、`kwargs` 只是变量名

下面几种写法的功能完全相同：

```python
def func(**kwargs):
    print(kwargs)

def func(**data):
    print(data)

def func(**kv):
    print(kv)
```

这里真正起作用的是两个星号 `**`，而不是名字 `kwargs`。

## 三、调用时：用 `**` 解包字典

```python
def func(**kwargs):
    print(kwargs)

info = {"a": 1, "b": 2}
func(**info)
# 等价于：func(a=1, b=2)
# 输出：{'a': 1, 'b': 2}
```

通俗地说，`**info` 会把字典中的键值对拆开，转换成关键字参数。

## 四、单星号与双星号的区别

```text
单个 *  ：解包列表或元组，传递位置参数
两个 ** ：解包字典，传递关键字参数
```

示例：

```python
def func(*args, **kwargs):
    print("位置参数：", args)
    print("关键字参数：", kwargs)

func(*(1, 2), **{"name": "张三"})
# 位置参数：(1, 2)
# 关键字参数：{'name': '张三'}
```

## 五、完整参数顺序

常见且完整的函数参数顺序是：

```text
必选普通参数 → 默认参数 → *args → 关键字专用参数 → **kwargs
```

其中，`**kwargs` 通常放在最后，用来接收没有被前面参数明确接收的关键字参数。

```python
def total(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

total(1, 2, 3, 4, x=100, y=200)
# a = 1
# b = 2
# args = (3, 4)
# kwargs = {'x': 100, 'y': 200}
```

参数拆解：

```text
a      = 1
b      = 2
args   = (3, 4)
kwargs = {'x': 100, 'y': 200}
```

## 六、最终记忆口诀

> 定义函数时，`**kwargs` 把多个关键字参数打包成字典。  
> 调用函数时，`**` 把字典解包成多个关键字参数。  
> `kwargs` 只是名字，两个星号 `**` 才是规则。
