try:
    width = float(input('Please enter width: '))
    length = float(input('Please enter length: '))

    if width == length:
        print('This is a square.')

    area = width * length
    print(f'The area is {area}')
except ValueError:
    print('Please enter a number.')