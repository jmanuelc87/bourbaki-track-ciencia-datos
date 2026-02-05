a = [i * 2 for i in range(1, 11)]

b = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]
b = filter(lambda a: len(a) > 4, b)

c = { k: k*2 for k in range(1, 6) }
