def average(numbers):
    """返回数字序列的平均值。"""
    if not numbers:
        raise ValueError("numbers 不能为空")
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]

num =[10*x for x in range (10)]
print("RANGE 1-5:", f"{average(numbers):.2f}")
print("RANGE 0-90:", average(num))