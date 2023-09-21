def my_generator(limit):
    current = 0
    while current <limit:
        yield current
        current += 1
gen = my_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
