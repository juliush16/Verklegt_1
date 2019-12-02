def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n---Assign eployees to a voyage---\n')
        print('Press "1" to assign pilots to a voyage')
        print('Press "2" to assign flight attendant to a voyage')
        print('Press "3" to change crew member information')
        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            pass
        elif choice_str == '2':
            pass
        elif choice_str == '3':
            pass

if __name__ == "__main__":
    menu()