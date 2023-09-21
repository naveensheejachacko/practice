def swap_numerator(func):
    def wrapper(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrapper



@swap_numerator
def divide(a,b):
    return a/b

result = divide(2,6)
print(result)