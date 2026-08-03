def func(d=None):
    if d is None:
        d = {}

    d["count"] = d.get("count", 0) + 1
    print(d)

func()  # {'count': 1}
func()  # {'count': 1}

print("手动传同一个字典")
# 如果手动传同一个字典进去才会累加
temp = {}
func(temp)  # {'count': 1}
func(temp)  # {'count': 2}