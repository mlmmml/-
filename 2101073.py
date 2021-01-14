a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c) # [1, 2] [3, 4] [5, 6]

data = ([1, 2], [3, 4], [5, 6])
print(*data) # [1, 2] [3, 4] [5, 6]

def asterisk_test(a, b, c, d):
    print(a, b, c, d)
data = {'b':1, 'c':2, 'd':3}
asterisk_test(10, **data) # 10 1 2 3

for data in zip(*([1, 2], [3, 4], [5, 6])): # = for data in zip([1, 2], [3, 4], [5, 6]):
    print(data)
    print(sum(data))
# (1, 3, 5)
# 9
# (2, 4, 6)
# 12

def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)

asterisk_test(1, 3, 4, 8) # 1 3 4 8 0
data = {'d':1, 'e':5, 'c':2}
asterisk_test(10, 3, **data) # 10 3 2 1 5
