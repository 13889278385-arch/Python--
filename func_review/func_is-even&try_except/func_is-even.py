#   V 2.0
def is_even(number=None):
    if number is None:
        raise ValueError("No number provided")
    return number % 2 == 0

print(is_even(4))
print(is_even(5))

try:
    print(is_even())
except ValueError as err:
    print(f"捕获错误：{err}")


#  V 1.2
# def is_even(number=None):
#     if number is None:
#         raise ValueError("No number provided")
#     elif not number :   
#         return False
#     return number % 2 == 0

# print(is_even(4)) 
# print(is_even(5)) 
# print(is_even()) 



#   v 1.1
# def is_even(number):
#     if number is None:
#         return False
#     return number % 2 == 0

# print(is_even(4)) 
# print(is_even(5)) 
# print(is_even()) 