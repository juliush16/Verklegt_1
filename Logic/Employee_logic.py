from Data.EmployeeData import EmployeeData


class EmployeeLogic:

    def all_employees(self):
        all_employee_list = []
        all_employees = EmployeeData().get_employee()
        for employee in all_employees:
            all_employee_list.append(employee)
        return all_employee_list

    def get_all_pilots(self):
        all_pilots_list = []
        all_employees = EmployeeData().get_employee()
        all_pilots_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.role == 'Pilot':
                all_pilots_list.append(employee)
        return all_pilots_list


    def get_all_captains(self):
        all_captains_list = []
        all_employees = self.get_employee()
        all_captains_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.rank == 'Captain':
                all_captains_list.append(employee)
        return all_captains_list


    def get_all_copilots(self):
        all_copilots_list = []
        all_employees = self.all_employees()
        all_copilots_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.rank == 'Copilot':
                all_copilots_list.append(employee)
        return all_copilots_list


    def get_all_cabin_crew(self):
        all_crew_list = []
        all_employees = self.all_employees()
        all_crew_list.append(all_employees[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for employee in all_employees:
            if employee.role == 'Cabincrew':
                all_crew_list.append(employee)
        return all_crew_list


    def get_all_flight_service_managers(self):
        all_fsm_list = []
        all_crew = self.get_all_cabin_crew()
        all_fsm_list.append(all_crew[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for crew_member in all_crew:
            if crew_member.rank == 'Flight Service Manager':
                all_fsm_list.append(crew_member)
        return all_fsm_list



    def get_all_flight_attendants(self):
        all_flight_attendants_list = []
        all_crew = self.get_all_cabin_crew()
        all_flight_attendants_list.append(all_crew[0]) # Til þess að fá fyrstu línuna með ssn, name og því :D
        for crew_member in all_crew:
            if crew_member.rank == 'Flight Attendant':
                all_flight_attendants_list.append(crew_member)
        return all_flight_attendants_list


    def create_new_employee(self,ssn,name,role,rank,licence,address,phonenumber,email):
        new_emp = Employee(ssn,name,role,rank,licence,address,phonenumber,email)
        self.add_employee(new_emp)

    def get_by_ssn(self, ssn):
        ret_string = ''
        all_employees = self.all_employees()
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

        
    #breyta maili, address, phonenumber
    def update_employee(self, ssn):  #passa að breyta ekki nafni og kt
        all_employee = self.all_employees()
        #first_line = all_employee[0]
        for employee in all_employee:
            if employee.get_ssn_str() == ssn:

                empl_string = ("\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}\n{}{}\n".format('SSN: ',employee.ssn,'Name: ',employee.name,'Role: ',employee.role,'Rank: ',employee.rank,'Licence: ',employee.licence,'Address: ',employee.address,'Phonenumber: ',employee.phonenumber,'Email: ',employee.email))
                #empl_string = ("{:<5}{:<10}{:<15}{:<15}{:<10}{:<15}".format("Role:", "Rank:", "Licence:","Address:","Phonenumber","Email")
                #print(first_line)

            
                print(empl_string)
                print("1. Edit address\n2. Edit Phonenumber\n3. Edit email\n"
                    "4. Return to Main Menu") 

                while True:
                    choice = int(input("What do you want to edit? "))
                    if choice < 1 or choice > 4:
                        print("Choice invalid! Try again")
                        clear()
                    else:
                        break
                while True: 
                    if choice == 1:
                        print("Current address: {}".format(edit_employee.get_address()))
                        new_address = input("Enter new address: ")
                        edit_employee.set_address(new_address)
                        print("Address changed to: {}".format(edit_employee.get_address()))
                        break
                    if choice == 2:
                        print("Current Phonenumber: {}".format(edit_employee.get_phonenumber()))
                        new_phonenumber = check_phonenumber()
                        #new_phonenumber = input("Enter new phonenumber: ")
                        edit_employee.set_phonenumber(new_phonenumber)
                        print("Phonenumber changed to: {}".format(edit_employee.get_phonenumber()))
                        break
                    if choice == 3:
                        print("Current email: {}".format(edit_employee.get_email()))
                        #new_email = input("Enter new email: ")
                        new_email = check_email()
                        edit_employee.set_email(new_email)
                        print("Email changed to: {}".format(edit_employee.get_email()))
                        break
                    if choice == 4:
                        break





  
    
    def get_available_employees(self): #Sýna starfsmenn sem hafa ekki unnið þennan dag og geta farið i vinnuferð
        pass
            
    def get_employee_for_voyage(self): #Manna vinnuferð, 2 flugmenn og 1 flugþjónn
        pass

