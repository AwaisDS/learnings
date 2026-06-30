while True:
    num1 = int(input('enter no 1: '))
    num2 = int(input('enter no 2: '))

    choice = int(input('1.multiply \n2.divide \n3.add \n4.sub\nEnter choice: '))

    if choice == 1:
        res = num1 * num2
    elif choice == 2:
        res = num1 / num2
    elif choice == 3:
        res = num1 + num2
    elif choice == 4:
        res = num1 - num2
    else:
        print('invalid choice')
        res = None

    if res is not None:
        print(f'you answer is {res}')

    ans = input('Do you want to continue? (y/n): ')
    if ans.lower() != 'y':
        break