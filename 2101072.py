def f(x,y):
    return x+y
print(f(1,3))

f = lambda x,y: x + y
print(f(1,3))

f = lambda x: x**2
print(f(2))

print((lambda x: x+1)(5))

ex = [1, 2, 3, 4, 5]
f = lambda x: x**2
print(list(map(f,ex))) # [1, 4, 9, 16, 25]

f = lambda x, y: x+y
print(list(map(f, ex, ex))) # [2, 4, 6, 8, 10]

print(list(map(lambda x: x**2 if x % 2 == 0 else x, ex))) # [1, 4, 3, 16, 5]

ex = [1, 2, 3, 4, 5]
print(list(value ** 2 for value in ex)) # [1, 4, 9, 16, 25]
print([value ** 2 for value in ex]) # [1, 4, 9, 16, 25]

from functools import reduce
print(reduce(lambda x, y: x+y, ex)) # 15

def factorial(n):
    return reduce(lambda x, y: x*y, range(1,n+1))
print(factorial(5)) # 120

def asterisk_test(a, *args): # *이 1개
    print(a, args)
    print(type(args))
    print(args[0])

asterisk_test(1,2,3,4,5,6)
# 1 (2, 3, 4, 5, 6)
# <class 'tuple'>
# 2

def asterisk_test(a, **kargs): # *이 2개
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)
# 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# <class 'dict'>

def asterisk_test(a, args):
    print(a, *args) # unpacking
    print(type(args))

asterisk_test(1, (2,3,4,5,6))

# 1 2 3 4 5 6
# <class 'tuple'>
