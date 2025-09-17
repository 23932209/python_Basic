import json


"""
# Json数据类型：python和json可以无缝的切换。
json其实质就是python的字典或python列表内嵌套的字典（嵌套的元素都是字典）。json数据就是把python中的字典转换成string字符串，或者把python列表内嵌套的字典转换成string字符串
    1）json就是python的字典。
                 例如：{"用户名":"admin","密码":123456}
    2）json就是python列表内嵌套的字典。其中，唯一的要求就是，列表内嵌套的元素都是字典。例如：[
		     {"用户名":"admin","密码":123456},
		     {"姓名":"root","类别":"数据库"} ,
		     {"应用领域":"深度学习","联系方式":23932209}
		]
"""

data01 = {"用户名":"admin","密码":123456}
data02 = [{"用户名":"admin","密码":123456},{"姓名":"root","类别":"数据库"},{"应用领域":"深度学习","联系方式":23932209}]
# python转json格式
json_str01 = json.dumps(data01,ensure_ascii=False)
json_str02 = json.dumps(data02,ensure_ascii=False)
print(json_str01)
print(json_str02)
#json转python格式
list01 = json.loads(json_str01)
dict01 = json.loads(json_str02)
print(list01)
print(dict01)
