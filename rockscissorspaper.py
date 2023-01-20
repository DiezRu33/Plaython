import random

# options = ['piedra', 'papel', 'tijera']

# rounds = 1
# computer_wins = 0
# user_wins = 0

# def choose_options():
#     user_option = input('piedra,papel o tijera => ')
#     user_option = user_option.lower()

#     rounds += 1

#     if not user_option in options:
#         print('esa opcion no es valida')
    
#         computer_option = random.choice(options)


# while True:

#     print("*" * 10)
#     print('ROUND', rounds)
#     print("*" * 10)

#     print('computer1_wins', computer_wins)
#     print('user_wins', user_wins)

# if user_option == computer_option:
#         print("Empate!")
# elif user_option == 'piedra':
#         if computer_option == 'tijera':
#             print('Piedra gana a tijera')
#             print('User ganó')
#             user_wins += 1
            
# else:
#         print('Papel gana a piedra')
#         print("computer ganó")
#         computer_wins += 1

# if user_option == 'tijera':
#         if computer_option == 'papel':
#             print('tijera gana a papel')
#             print('user ganó')
#             user_wins += 1
# else:
#         print('piedra gana a tijera')
#         print('computer ganó')
#         computer_wins += 1
# if computer_wins == 2:
#         print('El ganador es la computadora')
#         break
    
# if user_wins == 2:
#     print('El ganador es User')
#     break

#             print('User option =>', user_option)
#             print('Computer option =>', computer_option)


num = 0
num1 = 1000

if num > num1:
    print("El numero ", num, " es mayor que ",num1)
elif num == num1:
    print("El numero",num, "es malditamente identico a",num1)
elif num < num1:
    print("El",num, "es menor a ", num1)

else:
    print("El numero ", num , " es mayór que ", num1)

