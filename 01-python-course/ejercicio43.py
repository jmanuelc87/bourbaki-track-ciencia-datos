from functools import reduce

a = list(range(10))
b = map(lambda a: a**2, a)
c = filter(lambda a: a % 2 == 0, b)
d = reduce(lambda a, b: a+b, c, 0)

print(d)
