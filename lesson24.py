number = 55
counter = 1
finish = False

while finish == False:

    attempt = int(input('Input your number variant? '))

    if attempt == number:
        print(f'Congratulation!!! You guess the number by {counter} attempts')
        finish = True
    else:
        counter += 1
        if attempt < number:
            print('Input bigger number')
        else:
            print('Input less number')
