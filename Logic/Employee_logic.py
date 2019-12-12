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
        all_employees = self.all_employees()
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
        new_emp = EmployeeData(ssn,name,role,rank,licence,address,phonenumber,email)
        self.add_employee(new_emp)

    def get_by_ssn(self, ssn):
        allemps = self.all_employees()
        for emp in allemps:
            if emp.ssn == ssn:
                return emp
        return None

        
    #breyta maili, address, phonenumber
    def update_employee(self, updatedEmployee):  #passa að breyta ekki nafni og kt
        EmployeeData().update_employee(updatedEmployee)


  
    
    def get_available_employees(self): #Sýna starfsmenn sem hafa ekki unnið þennan dag og geta farið i vinnuferð
        pass
            
    def get_employee_for_voyage(self): #Manna vinnuferð, 2 flugmenn og 1 flugþjónn
        pass

