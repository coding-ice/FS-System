# 遍历一个超大的数组, 此时是非常占用内存

# 数组是可迭代对象 （list/tuple/set）
l = [i for i in range(10000001)]


# for i in l:
#     print(i)