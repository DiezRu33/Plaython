
txt = 'Hola'
price = 100

def cuenta(n, n2, n3):
    res = price + n
    res1 = price + n + n2
    res2 = price + n + n2 * n3 
    
    
    resultado = res
    resultado2 = res1
    resultado3 = res2

    for i in range(n, n2, n3):
        sum = n
        sum2 = n2
        sum3 = n3
        # print(range(n, n2, n3))
        sum += i
        sum2 += n + n3
        sum3 += n + n2 + n3
        return sum, sum2, sum3
    
print(cuenta(15, 100, 200))
# cuenta(10, 50, 100)
        
    # print(res, res2)

    # return res, res1, res2

# print(cuenta(10, 50, 100))
    # print("El resultado es: ", cuenta(10, 50, 100))
    # val = 
    
# print(cuenta(5 + 10 * 2))
    
# print(cuenta(5 + 10 * 20))
