items = 'zero one two three'.split()
print(items) # ['zero', 'one', 'two', 'three']
example = 'python,javascript'
example.split(',')
print(example) # python,javascript
ex = 'a,b,c,d'
a, b, c, d = ex.split(',')
print(a, b, d) # a b d

colors = ['red', 'green', 'blue']
result = ' + '.join(colors)
print(result) # red + green + blue

List comprehensions
result = []
for i in range(10):
    result.append(i)
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [i for i in range(10)]
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [i for i in range(10) if i % 2 == 1]
print(result) # [1, 3, 5, 7, 9]
word_1 = 'Hello'
word_2 = 'Hi'
result = [i+j for i in word_1 for j in word_2]
print(result) # ['HH', 'Hi', 'eH', 'ei', 'lH', 'li', 'lH', 'li', 'oH', 'oi']
case_1 = ['a', 'b', 'c']
case_2 = ['K', 'Z', 'E']
result = [i+j for i in case_1 for j in case_2]
print(result) # ['aK', 'aZ', 'aE', 'bK', 'bZ', 'bE', 'cK', 'cZ', 'cE']
result.sort()
print(result) # ['aE', 'aK', 'aZ', 'bE', 'bK', 'bZ', 'cE', 'cK', 'cZ']
result = [[i+j for i in case_1] for j in case_2] 
print(result) # [['aK', 'bK', 'cK'], ['aZ', 'bZ', 'cZ'], ['aE', 'bE', 'cE']]
words = 'All I want for christmas is you'.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i) # ['ALL', 'all', 3] ... ['YOU', 'you', 3]

Enumerate : list의 index와 값을 unpacking
for i,v in enumerate(['tic','tac','toc']):
    print(i)
    print(i, v)

my_list = ['a', 'b', 'c', 'd']
print(list(enumerate(my_list))) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist): # a1은 a에, b1은 b에
    print(a, b)
a, b, c = zip((100, 200, 300),(1, 2, 3),(10, 20, 30))
print(a) # (100, 1, 10)

k = [sum(x) for x in zip((100, 200, 300),(1, 2, 3),(10, 20, 30))]
print(k) # [111, 222, 333]

