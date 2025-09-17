x = [1,2,3,4,5,6,7]

# 传统写法
for i in x:
    if i>3:
        print(i)

# 简化写法
list = [i for i in x if i>3]
print(list,type(list))

# 将一维list转换成二维list
array = [[i] for i in x]
print(array,type(array))
