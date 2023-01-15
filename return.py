
def contador(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

# for x in range(contador(min, max)):
#     res = contador()
#     # res += contador(1, 10)
#     print('El resultado es: ', contador(min, max))
# print()

def test(min, max, maxx):
    res = 0
    for i in range(min, max, maxx):
        res += i
    return res

print(test(1, 10, 12))

# contador(1, 10)
# contador(11, 20)

# contador(21, 30)

# result = contador(1,10)
# print(result)
# result_2 = contador(result, result + 10)
# print(result_2)    

