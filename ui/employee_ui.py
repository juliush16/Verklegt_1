def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Register or list employees-----\n')
        print('Press "1" to register a new employee ')
        print('Press "2" to list all employees ')
        print('Press "3" to list all pilots')
        print('Press "4" to list all flight attendants')

        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            choice_str = 'q'
            return choice_str
        elif choice_str == '2':
            choice_str = 'q'
            return choice_str
        elif choice_str == '3':
            choice_str = 'q'
            return choice_str
        elif choice_str == '4':
            choice_str = 'q'
            return choice_str
