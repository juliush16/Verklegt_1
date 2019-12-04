from Repo.EmployeeRepo import EmployeeRepo as Emp_Repo
from Repo.voyageRepo import VoyageRepo as Voy_Repo

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
            assign_pilots_menu()
        elif choice_str == '2':
            assign_flight_attendants_menu()
        elif choice_str == '3':
            pass


def assign_pilots_menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n---Assign pilots to voyage---\n')
        print('Press "1" to see all upcoming voyages')  # Ekki buinn að utfæra þennan option
        print('Press "q" to go back!\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            pass


def assign_flight_attendants_menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n---Assign flight attendants to voyage---\n')
        print('Press "1" to see all upcoming voyages')  # Ekki buinn að utfæra þennan option
        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            pass

        


if __name__ == "__main__":
    menu()