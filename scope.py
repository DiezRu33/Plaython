
txt = 'Hola'
price = 100
def cuenta(n, n2, n3):
    res = price + n
    res1 = price + n + n2
    res2 = price + n + n2 * n3 
    return res, res1, res2

print("El resultado es: ", cuenta(10, 50, 100))

# print(cuenta(5 + 10 * 2))
    
# print(cuenta(5 + 10 * 20))
