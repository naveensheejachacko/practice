def fib(limit):
    a=0
    b=1
    i = 0
    while a<limit:
        a,b = b, a+b
        yield b
x= fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))







