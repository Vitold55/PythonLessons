from random import randint
import sys

number = randint(1, 100)
counter = 0

while True:

    attempt = int(input('Input your number variant? '))
    counter += 1

    if attempt == number:
        print(f'Congratulation!!! You guess the number by {counter} attempts')
        playAgain = input('If you want to play one more time, please, type Y! ')

        if playAgain == 'Y':
            number = randint(1, 3)
            counter = 0
        else:
            print('Thanks for playing this game!')
            break
    elif attempt < number:
        print('Input bigger number')
    else:
        print('Input less number')

# Second variant
# def guessNumberGame():
#     number = randint(1, 100)
#     counter = 0

#     while True:

#         attempt = int(input('Input your number variant? '))
#         counter += 1

#         if attempt == number:
#             print(f'Congratulation!!! You guess the number by {counter} attempts')
#             playAgain = input('If you want to play one more time, please, type Y! ')

#             if playAgain == 'Y':
#                 guessNumberGame()
#             else:
#                 sys.exit()
#         elif attempt < number:
#             print('Input bigger number')
#         else:
#             print('Input less number')


# guessNumberGame()
