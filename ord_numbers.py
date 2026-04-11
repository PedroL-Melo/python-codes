numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number >= 4: print('{}th'.format(number))
    elif number == 3: print('{}rd'.format(number))
    elif number == 2: print('{}nd'.format(number))
    elif number == 1: print('{}st'.format(number))