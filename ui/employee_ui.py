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
        print('Press "6" to update employee info')

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
        elif choice_str == '6':
            employee_ssn = input('Please input employee SSN :')
            temp = Emp_Repo()
            temp.update_employee(employee_ssn)


def reg_employee_menu():
    print('\n-----Register new employee-----\n')
    new_emp_SSN = ""
    while new_emp_SSN.isdigit() == False:
        new_emp_SSN = input('Enter employee social security number :')
    new_emp_name = input('Enter employee name :').capitalize()
    new_emp_role = ""
    new_emp_rank = "" 
    new_emp_licence = ""
    while new_emp_role != '1' or '2': #1 er pilot og 2 er cabin crew
        new_emp_role = input('Choose an option for employee role\n1:Pilot\n2:Cabincrew\n')
        if new_emp_role == '1':
            new_emp_role = "Pilot"
            while new_emp_role != '1' or '2': #pilot rank (captain or copilot)
                new_emp_rank = input('Choose an option for employee rank\n1:Captain\n2:Copilot\n')
                if new_emp_rank == '1':
                    new_emp_rank = 'Captain'
                elif new_emp_rank == '2':
                    new_emp_rank = "Copilot"
                break #fer ut ur while loopunni og i næstu
            
            while new_emp_licence != '1' or '2' or '3': #licence
                new_emp_licence = input('Choose an option for employee licence\n1:NABAE146\n2:NAFokkerF28\n3:NAFokkerF100\n')
                if new_emp_licence == '1':
                    new_emp_licence = "NABAE146"
                elif new_emp_licence == '2':
                    new_emp_licence = "NAFokkerF28"
                elif new_emp_licence == '3':
                    new_emp_licence = "NAFokkerF100"
                break #fer út ur while
            break #fer ut ur if

        elif new_emp_role == '2':
            new_emp_role = "Cabincrew"
            new_emp_licence = "N/A"
            while new_emp_rank != '1' or '2': #cabincrew rank (flight service manager og flight attendant)
                new_emp_rank = input('Choose an option for employee rank\n1:Flight Service Manager\n2:Flight Attendant\n')
                if new_emp_rank == '1':
                    new_emp_rank = "Flight Service Manager"
                elif new_emp_rank == '2':
                    new_emp_rank = "Flight Attendant"
                break
            break

#    new_emp_licence = input('Enter employee licence :') #á bara við pilot, pilot velur á milli flugvélar / cabincrew skrifast N/A
    new_emp_address = input('Enter employee address :').capitalize()
    new_emp_phonenumber = input('Enter employee phone number :')
    new_emp_email = input('Enter employee email :')
    new_employee = Employee(new_emp_SSN, new_emp_name, new_emp_role, new_emp_rank, new_emp_licence, new_emp_address, new_emp_phonenumber, new_emp_email)
    temp = Emp_Repo()
    temp.add_employee(new_employee)
    print('Employee : "',str(new_emp_name),'" has been added!')
