from Repo.EmployeeRepo import EmployeeRepo as Emp_Repo
from Models.employee import Employee
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
            reg_employee_menu()
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


def reg_employee_menu():
    print('\n-----Register new employee-----\n')
    new_emp_SSN = input('Enter employee social security number :')
    new_emp_name = input('Enter employee name :')
    new_emp_role = input('Enter employee role :')
    new_emp_rank = input('Enter employee rank :')
    new_emp_licence = input('Enter employee licence :')
    new_emp_address = input('Enter employee address :')
    new_emp_phonenumber = input('Enter employee phone number :')
    new_emp_email = input('Enter employee email :')
    new_employee = Employee(new_emp_SSN, new_emp_name, new_emp_role, new_emp_rank, new_emp_licence, new_emp_address, new_emp_phonenumber, new_emp_email)
    temp = Emp_Repo()
    temp.add_employee(new_employee)
    print('Employee : "',str(new_emp_name),'" has been added!')
