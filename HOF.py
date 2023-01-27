def increment(x):
    return x * 2

despiste = lambda x: x + 1

# take num by parameters:
def increment_v2(x, func):
    return x + func(x)

# print(increment(10))

increment_v3 = lambda x, func: x + func(x)

result = increment_v2(1, increment)
print(result)

# print(increment_v2(5, increment))

result = increment_v3(3, despiste)
print(result)



