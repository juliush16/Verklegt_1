from Repo.EmployeeRepo import EmployeeRepo as Emp_Repo
def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Register or list employees-----\n')
        print('Press "1" to register a new employee ')
        print('Press "2" to list all Employees ')
        print('Press "3" to list all Pilots')
        print('Press "4" to list all Captains')
        print('Press "5" to list all Copilots')
        print('Press "6" to list all Cabin Crew')
        print('Press "7" to list all Flight Service Managers')
        print('Press "8" to list all Flight Attendants')

        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            pass
        elif choice_str == '2':
            temp = Emp_Repo()
            temp.print_all_employees()
        elif choice_str == '3':
            temp = Emp_Repo()
            temp.print_all_pilots()
        elif choice_str == '4':
            temp = Emp_Repo()
            temp.print_all_captains()
        elif choice_str == '5':
            temp = Emp_Repo()
            temp.print_all_copilots()
        elif choice_str == '6':
            temp = Emp_Repo()
            temp.print_all_cabin_crew()
        elif choice_str == '7':
            temp = Emp_Repo()
            temp.print_all_flight_service_managers()
        elif choice_str == '8':
            temp = Emp_Repo()
            temp.print_all_flight_attendants()