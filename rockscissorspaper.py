import random

computer_wins = 0
user_wins = 0
rounds = 1

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('esa opcion no es valida')
        return None, None
    
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User ganó')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print("computer ganó")
            computer_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user ganó')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer ganó')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('--- USER GANA ---')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('--- COMPUTER GANA ---')
            computer_wins += 1

    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print("*" * 10)
        print('ROUND', rounds)
        print("*" * 10)

        print('PC: ', computer_wins)
        print('USER: ', user_wins)
        rounds += 1

        if computer_wins == 3:
            print(
                '------',
                'GANA LA PC',
                '------'
                )
        # break
        elif user_wins == 3:
            print(
                '------',
                'GANA EL USUARIO',
                '------')
        # break

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)




run_game()