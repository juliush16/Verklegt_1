
from Models.employee import Employee
import csv

class EmployeeRepo:

    def __init__(self):
        self.__employee = []

    def add_employee(self, employee):
        with open("./data/Employee.csv", "a+") as employee_file:
            ssn = employee.get_ssn_str()
            name = employee.get_name_str()
            role = employee.get_role()
            rank = employee.get_rank()
            licence = employee.get_licence()
            address =  employee.get_address()
            phonenumber = employee.get_phonenumber()
            email = employee.get_email()
            employee_file.write("{},{},{},{},{},{},{},{},\n".format(ssn,name,
            role,rank,licence,address,phonenumber,email))

    def get_employee(self):
        if self.__employee == []:
            with open("./Data/Employee.csv", "r", encoding = "utf-8") as employee_file:
                employee_reader = csv.reader(employee_file)
                for line in employee_reader:
                    ssn = line[0]
                    name = line[1]
                    role = line[2]
                    rank = line[3]
                    licence = line[4]
                    address = line[5]
                    phonenumber = line[6]
                    email = line[7]
                    new_employee = Employee(ssn, name, role, rank,licence,
                    address, phonenumber, email)
                    self.__employee.append(new_employee)
        return self.__employee

    def all_employees(self):
        all_employee_list = []
        all_employees = self.get_employee()
        for employee in all_employees:
            all_employee_list.append(employee)
        return all_employee_list

    def print_all_employees(self):
        all_employees = self.all_employees()
        for employee in all_employees:
            print(employee)

    def get_all_pilots(self):
        all_pilots_list = []
        all_employees = self.get_employee()
        all_pilots_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.role == 'Pilot':
                all_pilots_list.append(employee)
        return all_pilots_list

    def print_all_pilots(self):
        all_pilots = self.get_all_pilots()
        for pilot in all_pilots:
            print(pilot)

    # def get_all_captains(self):
    #     all_captains_list = []
    #     all_employees = self.get_employee()
    #     all_captains_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
    #     for employee in all_employees:
    #         if employee.rank == 'Captain':
    #             all_captains_list.append(employee)
    #     return all_captains_list

    # def print_all_captains(self):
    #     all_captains = self.get_all_captains()
    #     for captain in all_captains:
    #         print(captain)

    # def get_all_copilots(self):
    #     all_copilots_list = []
    #     all_employees = self.get_employee()
    #     all_copilots_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
    #     for employee in all_employees:
    #         if employee.rank == 'Copilot':
    #             all_copilots_list.append(employee)
    #     return all_copilots_list

    # def print_all_copilots(self):
    #     all_copilots = self.get_all_copilots()
    #     for copilot in all_copilots:
    #         print(copilot)

    def get_all_cabin_crew(self):
        all_crew_list = []
        all_employees = self.get_employee()
        all_crew_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.role == 'Cabincrew':
                all_crew_list.append(employee)
        return all_crew_list

    def print_all_cabin_crew(self):
        all_cabin_crew = self.get_all_cabin_crew()
        for crew_member in all_cabin_crew:
            print(crew_member)

    # def get_all_flight_service_managers(self):
    #     all_fsm_list = []
    #     all_crew = self.get_all_cabin_crew()
    #     all_fsm_list.append(all_crew[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
    #     for crew_member in all_crew:
    #         if crew_member.rank == 'Flight Service Manager':
    #             all_fsm_list.append(crew_member)
    #     return all_fsm_list

    # def print_all_flight_service_managers(self):
    #     all_fsm = self.get_all_flight_service_managers()
    #     for fsm in all_fsm:
    #         print(fsm)


    # def get_all_flight_attendants(self):
    #     all_flight_attendants_list = []
    #     all_crew = self.get_all_cabin_crew()
    #     all_flight_attendants_list.append(all_crew[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
    #     for crew_member in all_crew:
    #         if crew_member.rank == 'Flight Attendant':
    #             all_flight_attendants_list.append(crew_member)
    #     return all_flight_attendants_list

    # def print_all_flight_attendants(self):
    #     all_flight_attendants = self.get_all_flight_attendants()
    #     for flight_attendant in all_flight_attendants:
    #         print(flight_attendant)

    def create_new_employee(self,ssn,name,role,rank,licence,address,phonenumber,email):
        new_emp = Employee(ssn,name,role,rank,licence,address,phonenumber,email)
        self.add_employee(new_emp)

    def get_by_ssn(self, ssn):
        ret_string = ''
        all_employees = self.get_employee()
        for employee in all_employees:
            if employee.ssn == ssn:
                ret_string += '\n' + str(employee)

        if ret_string != '':
            temp_str = ret_string
            ret_string = str(all_employees[0])
            ret_string += temp_str
            return ret_string
        
        else:
            return 'Employee not found!'

        
    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}\n".format
        ("Ssn:", "Name:","Role:", "Rank:", "Licence:", "address:", "Phonenumber:", "Email:")
        employeelist = self.get_employee()
        for employee in employeelist:
            string += str(employee) + "\n"
        return string


    def update_employee(self, ssn):  #passa að breyta ekki nafni og kt
        all_employee = self.get_employee()
        for employee in all_employee:
            if employee.get_ssn == ssn:
                edit_employee = employee
                empl_string = "{},{},{},{},{},{}".format("Role: ","Rank: ","Licence: ","Address: ","Phonenumber: ", "Email: ")
                print("{}{}\n".format(empl_string, edit_employee))
                print("1. Edit Role\n2. Edit Rank\n"
                    "3. Edit Licence\n4. Edit Address\n5. Edit Phonenumber\n"
                    "5. Edit Email\n6. Return to Main Menu") 
                while True:
                    choice = int(input("What do you want to edit? "))
                    if choice < 1 or choice > 5:
                        print("Choice invalid! Try again")
                    else:
                        break
                while True:
                    if choice == 1:
                        print("Current role: {}".format(edit_employee.get_role()))
                        new_role = input("Enter new role: ")      #Kannski breyta hér að það er bara hægt að velja um 2 role
                        edit_employee.set_role(new_role)
                        print("Role changed to: {}".format(edit_employee.get_role()))
                        break
                    if choice == 2:
                        print("Current licence: {}".format(edit_employee.get_licence()))
                        new_licence = input("Enter new licence: ")  #Kannski breyta hér að það er bara hægt að velja um ákv. licence
                        edit_employee.set_licence(new_licence)
                        print("Licence changed to: {}".format(edit_employee.get_licence()))
                        break
                    if choice == 3:
                        print("Current address: {}".format(edit_employee.get_address()))
                        new_address = input("Enter new address: ")
                        edit_employee.set_address(new_address)
                        print("Address changed to: {}".format(edit_employee.get_address()))
                        break
                    if choice == 4:
                        print("Current Phonenumber: {}".format(edit_employee.get_phonenumber()))
                        new_phonenumber = input("Enter new phonenumber: ")
                        edit_employee.set_phonenumber(new_phonenumber)
                        print("Phonenumber changed to: {}".format(edit_employee.get_phonenumber()))
                        break
                    if choice == 5:
                        print("Current email: {}".format(edit_employee.get_email()))
                        new_email = input("Enter new email: ")
                        edit_employee.set_email(new_email)
                        print("Email changed to: {}".format(new_email.get_email()))


  
    
    def get_available_employees(self): #Sýna starfsmenn sem hafa ekki unnið þennan dag og geta farið i vinnuferð
        pass
            
    def get_employee_for_voyage(self): #Manna vinnuferð, 2 flugmenn og 1 flugþjónn
        pass

