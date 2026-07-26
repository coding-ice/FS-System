from collections import abc


# 可迭代对象
lst = [1,2,3]

it1 = iter(lst)

# lst → iter() → 新 iterator → next...
# for i in lst:
#     print(i)

# print('-------------')

# for i in lst:
#     print(i)


# it1 → iter()（返回 self）→ next...（耗尽后第二次 for 为空
for i in it1:
    print(i)

for i in it1:
    print(i)


# for x in obj 的本质是：拿到一个迭代器，再对它反复 next，直到 StopIteration。