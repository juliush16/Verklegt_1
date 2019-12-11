from Logic.Employee_logic import EmployeeLogic
from Data.EmployeeData import EmployeeData
from Models.employee import Employee
from Data.inputCheck import *

class EmployeeUI:



    def menu(self):
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
                self.reg_employee_menu()
            elif choice_str == '2':
                self.print_all_employees()
            elif choice_str == '3':
                self.print_all_pilots()
            elif choice_str == '4':
                self.print_all_cabin_crew()
            elif choice_str == '5':
                employee_ssn = input('Please input employee SSN :')
                print(EmployeeLogic().get_by_ssn(employee_ssn))
            elif choice_str == '6':
                employee_ssn = input('Please input employee SSN :')
                EmployeeLogic().update_employee(employee_ssn)


    def reg_employee_menu(self):
        print('\n-----Register new employee-----\n')
        new_emp_SSN = check_ssn()
        new_emp_name = input('Enter employee name :').capitalize()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
        new_emp_role = check_role()
        new_emp_rank = check_rank(new_emp_role)
        new_emp_licence = check_licence(new_emp_role)
        new_emp_address = input('Enter employee address :').capitalize()
        new_emp_phonenumber = check_phonenumber()
        new_emp_email = check_email()
        new_employee = Employee(new_emp_SSN, new_emp_name, new_emp_role, new_emp_rank, new_emp_licence, new_emp_address, new_emp_phonenumber, new_emp_email)
        EmployeeData().add_employee(new_employee)
        print('Employee : "',str(new_emp_name),'" has been added!')

    def print_all_employees(self):
        all_employees = EmployeeLogic().all_employees()
        for employee in all_employees:
            print(employee)

    def print_all_pilots(self):
        all_pilots = EmployeeLogic().get_all_pilots()
        for pilot in all_pilots:
            print(pilot)

    def print_all_captains(self):
        all_captains = EmployeeLogic().get_all_captains()
        for captain in all_captains:
            print(captain)
    
    def print_all_copilots(self):
        all_copilots = EmployeeLogic().get_all_copilots()
        for copilot in all_copilots:
            print(copilot)

    def print_all_cabin_crew(self):
        all_cabin_crew = EmployeeLogic().get_all_cabin_crew()
        for crew_member in all_cabin_crew:
            print(crew_member)

    def print_all_flight_service_managers(self):
        all_fsm = EmployeeLogic().get_all_flight_service_managers()
        for fsm in all_fsm:
            print(fsm)

    def print_all_flight_attendants(self):
        all_flight_attendants = EmployeeLogic().get_all_flight_attendants()
        for flight_attendant in all_flight_attendants:
            print(flight_attendant)





    # new_emp_role = ""
    # new_emp_rank = "" 
    # new_emp_licence = ""
    # while new_emp_role != '1' or '2': #1 er pilot og 2 er cabin crew
    #     new_emp_role = input('Choose an option for employee role\n1:Pilot\n2:Cabincrew\n')
    #     if new_emp_role == '1':
    #         new_emp_role = "Pilot"
    #         while new_emp_role != '1' or '2': #pilot rank (captain or copilot)
    #             new_emp_rank = input('Choose an option for employee rank\n1:Captain\n2:Copilot\n')
    #             if new_emp_rank == '1':
    #                 new_emp_rank = 'Captain'
    #             elif new_emp_rank == '2':
    #                 new_emp_rank = "Copilot"
    #             break #fer ut ur while loopunni og i næstu

    #         while new_emp_licence != '1' or '2' or '3': #licence
    #             new_emp_licence = input('Choose an option for employee licence\n1:NABAE146\n2:NAFokkerF28\n3:NAFokkerF100\n')
    #             if new_emp_licence == '1':
    #                 new_emp_licence = "NABAE146"
    #             elif new_emp_licence == '2':
    #                 new_emp_licence = "NAFokkerF28"
    #             elif new_emp_licence == '3':
    #                 new_emp_licence = "NAFokkerF100"
    #             break #fer út ur while
    #         break #fer ut ur if

    #     elif new_emp_role == '2': #cabincrew 
    #         new_emp_role = "Cabincrew"
    #         new_emp_licence = "N/A"
    #         while new_emp_rank != '1' or '2': #cabincrew rank (flight service manager og flight attendant)
    #             new_emp_rank = input('Choose an option for employee rank\n1:Flight Service Manager\n2:Flight Attendant\n')
    #             if new_emp_rank == '1':
    #                 new_emp_rank = "Flight Service Manager"
    #             elif new_emp_rank == '2':
    #                 new_emp_rank = "Flight Attendant"
    #             break
    #         break
