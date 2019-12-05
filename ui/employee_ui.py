from Repo.EmployeeRepo import EmployeeRepo as Emp_Repo
from Models.employee import Employee
def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Register or list employees-----\n')
        print('Press "1" to register a new employee ')
        print('Press "2" to list all Employees ')
        print('Press "3" to list all Pilots')
        print('Press "4" to list all Cabin Crew')
        print('Press "5" to find employee by SSN')

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
            temp.print_all_cabin_crew()
        elif choice_str == '5':
            employee_ssn = input('Please input employee SSN :')
            temp = Emp_Repo()
            print(temp.get_by_ssn(employee_ssn))


def reg_employee_menu():
    print('\n-----Register new employee-----\n')
    new_emp_SSN = ""
    while new_emp_SSN.isdigit() == False:
        new_emp_SSN = input('Enter employee social security number :')
    new_emp_name = input('Enter employee name :').capitalize()

    new_emp_role = ""
    while new_emp_role != '1' or '2':
        new_emp_role = input('Choose an option for employee role\n1:Pilot\n2:Cabincrew\n')
        if new_emp_role == '1':
            new_emp_role = "Pilot"
            break
        elif new_emp_role == '2':
            new_emp_role = "Cabincrew"
            break

    new_emp_rank = ""
    while new_emp_rank != '1' or '2' or '3' or '4':
        new_emp_rank = input('Choose an option for employee rank\n1:Captain\n2:Copilot\n3:Flight Service Manager\n4:Flight Attendant\n')
        if new_emp_rank == '1':
            new_emp_rank = "Captain"
            break
        elif new_emp_rank == '2':
            new_emp_rank = "Copilot"
            break
        elif new_emp_rank == '3':
            new_emp_rank = "Flight Service Manager"
            break
        elif new_emp_rank == '4':
            new_emp_rank = "Flight Attendant"
            break

    new_emp_licence = input('Enter employee licence :')
    new_emp_address = input('Enter employee address :').capitalize()
    new_emp_phonenumber = input('Enter employee phone number :')
    new_emp_email = input('Enter employee email :')
    new_employee = Employee(new_emp_SSN, new_emp_name, new_emp_role, new_emp_rank, new_emp_licence, new_emp_address, new_emp_phonenumber, new_emp_email)
    temp = Emp_Repo()
    temp.add_employee(new_employee)
    print('Employee : "',str(new_emp_name),'" has been added!')
