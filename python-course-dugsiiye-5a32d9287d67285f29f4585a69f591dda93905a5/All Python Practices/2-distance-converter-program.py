print('Welcome to distance converter program')
while True:
    choice = input('(MI) for miles, (KM) for kilometers & (q) for quit: ').lower()
    if choice == 'q':
        break
    elif choice == 'mile':
        km = int(input('Enter the kilometers: '))
        mile = km / 1.609
        print(f'{km} killometers is {mile} miles')
    elif choice == 'km':
        mi = int(input('Enter the miles: '))
        km = mi * 1.609
        print(f'{mi} miles is {km} killometers')
    else:
        print('Invalid! please try again.')