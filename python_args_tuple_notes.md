# Python 中的 `*args`：可变位置参数与解包

## 一句话先记住核心

- 符号是规则，`args` 只是大家习惯起的名字，换成别的单词完全没问题。
- `*变量名` 会把多余的位置参数全部装进一个元组（tuple）里。
- `*` 在函数定义和函数调用中的作用不同：定义时用于“打包”，调用时用于“解包”。

## 一、函数定义：名字随便改，`*` 才是灵魂

### 标准写法：`*args`

```python
def test(*args):
    print(args)

test(1, 2, 3)
# 输出：(1, 2, 3)
```

这里，传入的多个位置参数被打包成了一个元组：

```python
args == (1, 2, 3)
```

### 换成 `*nums`，效果完全一样

```python
def test(*nums):  # 只改了名字，功能不变
    print(nums)

test(10, 20, "hello", True)
# 输出：(10, 20, 'hello', True)
```

因此，`args` 只是行业约定，并不是 Python 的固定关键字。下面这些名字都可以：

```python
def test(*numbers):
    print(numbers)
```

注意：变量名前面的星号不能丢，否则就不再表示可变位置参数。

## 二、函数调用：`*` 用来解包

假设有一个列表，希望把里面的每个元素分别传给函数。

### 错误写法：直接传入列表

```python
def func(*args):
    print(args)

li = [1, 2, 3]
func(li)
# 输出：([1, 2, 3],)
```

这里整个列表被当成了一个参数，所以最终元组中只有一个元素——这个列表。

### 正确写法：在列表前加 `*` 解包

```python
li = [1, 2, 3]
func(*li)
# 等价于：func(1, 2, 3)
# 输出：(1, 2, 3)
```

通俗地说：

```python
*li
```

就是把列表 `[1, 2, 3]` 拆开，变成独立的 `1`、`2`、`3` 三个位置参数传入函数。

元组也可以解包：

```python
t = (5, 6)
func(*t)
# 等价于：func(5, 6)
```

## 三、参数的摆放顺序

常见的函数参数顺序如下：

```text
普通参数 → 默认参数 → *args → 关键字专用参数 → **kwargs
```

其中，`*args` 后面的参数会成为“关键字专用参数”，调用时通常必须使用参数名传入。

### 正确示范

```python
def total(a, b=10, *args):
    print("必填 a：", a)
    print("默认 b：", b)
    print("可变参数 args：", args)

total(1, 2, 3, 4, 5)
```

参数拆解：

```text
a = 1                  # 必填参数
b = 2                  # 覆盖默认值 10
args = (3, 4, 5)       # 剩余位置参数被打包进 args
```

### `*args` 后面可以继续写关键字专用参数

```python
def total(*args, a, b=10):
    print(args, a, b)

total(1, 2, 3, a=4)
# args = (1, 2, 3)，a = 4，b = 10
```

所以，`def total(*args, a, b=10):` 本身是合法语法；但 `a` 需要用关键字形式传入，例如 `a=4`。

### `**kwargs` 通常放在最后

```python
def demo(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, color="blue", size=12)
# a = 1
# b = 2
# args = (3, 4)
# kwargs = {'color': 'blue', 'size': 12}
```

## 四、快速对比

| 写法 | 作用 | 示例 |
|---|---|---|
| `def func(*args)` | 定义函数时，把多个位置参数打包成元组 | `func(1, 2, 3)` → `args=(1, 2, 3)` |
| `func(*li)` | 调用函数时，把列表或元组解包成多个参数 | `li=[1, 2, 3]` → `func(1, 2, 3)` |
| `def func(**kwargs)` | 把多个关键字参数打包成字典 | `func(x=1)` → `kwargs={'x': 1}` |

## 五、最终记忆口诀

> 定义时，`*` 把参数打包；调用时，`*` 把容器解包。  
> `args` 只是名字，星号才是规则。
