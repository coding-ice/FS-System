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
# for i in it1:
#     print(i)

# for i in it1:
#     print(i)


# for x in obj 的本质是：拿到一个迭代器，再对它反复 next，直到 StopIteration。



# 生成器表达式

def gen_num():
    print('start generator')
    yield 1
    print('continue generator')
    yield 2

# 列表推导范式 及时求值
res = [x for x in gen_num()]
print(res)

# 生成器表达式 惰性求值
res = (x for x in gen_num())
print(res)

for x in res:
    print(x)

print('------生成器表达式-------')

gen = (x for x in range(5))
print(x for x in range(5))

for x in gen:
    print(x)

