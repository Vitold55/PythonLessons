number = 55
counter = 0

while True:

    attempt = int(input('Input your number variant? '))
    counter += 1

    if attempt == number:
        print(f'Congratulation!!! You guess the number by {counter} attempts')
        break
    elif attempt < number:
        print('Input bigger number')
    else:
        print('Input less number')
