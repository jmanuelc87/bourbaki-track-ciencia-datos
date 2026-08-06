def function(a, b, call):
    return call(a, b)


print(function(1, 2, lambda a, b: a+b))
print(function(1, 2, lambda a, b: a*b))

def fibonacci(n):
    if n == 1 or n < 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))