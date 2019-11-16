try:
    100 / 0
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Else only if try worked')
finally:
    print('Finally')


while True:
    try:
        num = int(input('Input the number: '))
        print(f"100 / {num} = {100 / num}")
        break
    except ZeroDivisionError:
        print('Input not zero')
    except ValueError:
        print('Input only number')
