def gen_num():
    print('start generator')
    yield 1
    yield 2
    yield 3

    return 4

print(gen_num)

gen = gen_num() # 生成器对象

print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

# try:
#     print(next(gen))
# except StopIteration as e:
#     print('generator return value:',e.value)
