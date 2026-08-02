user = {"name": "小李", "age": 20}
user["city"] = "杭州"
#新增键city，字典变为：{'name': '小李', 'age': 20, 'city': '杭州'}
email = user.get("email", "未填写") 
#标准函数  user.get(键, 默认值)：找字典里有没有 email 这个键
#标准格式  字典.get(要查找的键, 找不到时返回的默认值)
for key, value in user.items():
    print(key, value)   