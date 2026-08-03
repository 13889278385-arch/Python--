def average(numbers):
    """返回数字序列的平均值。"""
    if not numbers:  # 判断序列为空（空列表/空元组）
        raise ValueError("numbers 不能为空")
    return sum(numbers) / len(numbers)\
    
print(average([1, 2, 3, 4, 5]))
print(average([]))