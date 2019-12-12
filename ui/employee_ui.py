from Logic.Employee_logic import EmployeeLogic
from Data.EmployeeData import EmployeeData
from Models.employee import Employee
from Data.inputCheck import InputCheck
from ui.aircraftUI import Aircraft_UI
from Logic.get_pilots_license import PilotLicence

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
                self.pilots_menu_display()
                #print()
                #Aircraft_UI().print_all_airplanes()
                #airplane = input("Select licence to see the Pilots: ")
                #print("\n")
                #PilotLicence().get_pilots_wLicence(airplane)
                #self.print_all_pilots()
            elif choice_str == '4':
                self.print_all_cabin_crew()
            elif choice_str == '5':
                employee_ssn = input('Please input employee SSN: ')
                print()
                print("{:<15}{:<20}{:<15}{:<20}{:<15}{:<15}{:<15}{:<15}".format("SSN","Name","Role","Rank","Licence","Address","Phonenumber","Email"))
                print(EmployeeLogic().get_by_ssn(employee_ssn))
            elif choice_str == '6':
                self.updateEmployee()



    def reg_employee_menu(self):
        print('\n-----Register new employee-----\n')
        new_emp_SSN = InputCheck().check_ssn()
        new_emp_name = input('Enter employee name: ').capitalize()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
        new_emp_role = InputCheck().check_role()
        new_emp_rank = InputCheck().check_rank(new_emp_role)
        new_emp_licence = InputCheck().check_licence(new_emp_role)
        new_emp_address = input('Enter employee address: ').capitalize()
        new_emp_phonenumber = InputCheck().check_phonenumber()
        new_emp_email = InputCheck().check_email()
        new_employee = Employee(new_emp_SSN, new_emp_name, new_emp_role, new_emp_rank, new_emp_licence, new_emp_address, new_emp_phonenumber, new_emp_email)
        EmployeeData().add_employee(new_employee)
        print('Employee: "',str(new_emp_name),'" has been added!')
#
    def updateEmployee(self):
        self.print_all_employees()
        print()
        ssnToUpdate = input("Enter ssn of employee to update: ")
        empToUpdate = EmployeeLogic().get_by_ssn(ssnToUpdate)
        if empToUpdate == None:
            print("Invalid employee")
            return
        choice = ""
        print('Press "1" to update address\nPress "2" to update Phonenumber\nPress "3" to update email\nPress "4" to Return to Main Menu')
        while True: 
            choice = int(input("What do you want to update? "))
            if choice == 1:
                empToUpdate.address = input("Enter address: ")
                print('\nAdress has been updated!')
                break
            elif choice == 2:
                new_phonenumber = InputCheck().check_phonenumber()
                empToUpdate.phonenumber = new_phonenumber
                print("\nPhone number updated to: ",new_phonenumber) 
                break
            elif choice == 3:
                new_email = InputCheck().check_email()
                empToUpdate.email = new_email
                print("\nEmail adress updated to: ",new_email)
                break
            elif choice == 4:
                break
            else:
                print("Invalid input try again!")
        EmployeeLogic().update_employee(empToUpdate)

    def print_all_employees(self):
        all_employees = EmployeeLogic().all_employees()
        for employee in all_employees:
            print(employee)

    def print_all_pilots(self):
        all_pilots = EmployeeLogic().get_all_pilots()
        for pilot in all_pilots:
            print(pilot)
    
    def pilots_menu_display(self):
        print()
        choice_string = ""
        while choice_string != "q":
            print('Press "1" to list all Pilots')
            print('Press "2" to list Pilots after licence')
            print('Press "3" to list all Captains')
            print('Press "4" to list all Co Pilots')
            print('Press "q" to Quit\n')
            choice_string = input('Choose an option: ')

            if choice_string == 'q':
                return choice_string
                break
            elif choice_string == '1':
                self.print_all_pilots()
                break
            elif choice_string == '2':
                Aircraft_UI().print_all_airplanes()
                airplane = input("Select licence to see the Pilots: ")
                print("\n")
                PilotLicence().get_pilots_wLicence(airplane)
                break
            elif choice_string == '3':
                self.print_all_captains()
                break
            elif choice_string == '4':
                self.print_all_copilots()
                break



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


