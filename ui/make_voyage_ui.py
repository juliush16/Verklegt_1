def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Make a voyage-----\n')
        print('Press "1" to make a new voyage')
        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            create_new_voyage()
            choice_str = 'q'
            return choice_str


def create_new_voyage():
    input('Create new voyage? : ')

if __name__ == "__main__":
    menu()