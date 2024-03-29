from datetime import datetime
from Data.Destinations2Data import Destinations2Data


class InputCheck:
    def check_ssn(self):
        new_emp_SSN = input('Enter employee social security number: ')
        while new_emp_SSN.isdigit() != True or len(new_emp_SSN) != 10:
            print('Invalid employee social security number Try again!')
            new_emp_SSN = input('Enter employee social security number: ')
            # Vatntar að athuga hér hvort starfsmaður sé í listanum
        
        return new_emp_SSN

    # def check_if_ssn_exist(self,new_employee):
    #     all_employees = EmployeeLogic().all_employees()
    #     for employee in all_employees:
    #         if employee.ssn == new_employee:
    #             print("Employee is already registered Try again!\n")
    #             return self.check_ssn()



    def check_phonenumber(self):
        new_emp_phonenumber = input('Enter employee phone number: ')
        while new_emp_phonenumber.isdigit() != True or len(new_emp_phonenumber) != 7:
            print('Invalid employee phone number Try again!')
            new_emp_phonenumber = input('Enter employee phone number: ')
        return new_emp_phonenumber
        
        
    def check_role(self):
        new_emp_role = ""
        while new_emp_role != '1' or '2':
            print('Press "1" for Pilot\nPress "2" for Cabin Crew\n')
            new_emp_role = input('Choose an role: ')
            if new_emp_role == '1':
                new_emp_role = "Pilot"
                break
            elif new_emp_role == '2': #cabincrew 
                new_emp_role = "Cabincrew"
                break
            print("Invalid employee role try again!")
        return new_emp_role

    def check_rank(self,new_emp_role):
        new_emp_rank = ""
        while new_emp_role == "Pilot" or "Cabincrew":
            if new_emp_role == "Pilot":
                print('Press "1" for Captain\nPress "2" for Co Pilot\n')
                new_emp_rank = input('Choose rank: ')
                if new_emp_rank == '1':
                    new_emp_rank = 'Captain'
                    break
                elif new_emp_rank == '2':
                    new_emp_rank = "Copilot"
                    break
                print("Invalid option for employee rank try again!")
            if new_emp_role == "Cabincrew":
                print('Press "1" for Flight Service Manager\nPress "2" for Flight Attendant\n')
                new_emp_rank = input('Choose rank: ')
                if new_emp_rank == '1':
                    new_emp_rank = "Flight Service Manager"
                    break
                elif new_emp_rank == '2':
                    new_emp_rank = "Flight Attendant"
                    break
                print("Invalid option for employee rank try again!")
        return new_emp_rank

    def check_licence(self,new_emp_role):
        new_emp_licence = ""
        if new_emp_role == "Cabincrew":
            new_emp_licence = "N/A"
            return new_emp_licence
        if new_emp_role == "Pilot":
            while new_emp_licence != '1' or '2' or '3': #licence
                print('Press "1" for NABAE146\nPress "2" for NAFokkerF28\nPress "3" for NAFokkerF100\n')
                new_emp_licence = input('Choose licence: ')
                if new_emp_licence == '1':
                    new_emp_licence = "NABAE146"
                    break
                elif new_emp_licence == '2':
                    new_emp_licence = "NAFokkerF28"
                    break
                elif new_emp_licence == '3':
                    new_emp_licence = "NAFokkerF100"
                    break
                print("Invalid employe licence try again!")
            return new_emp_licence

    def check_email(self):
        new_emp_email = ""
        while new_emp_email[-7:] != "@nan.is":
            new_emp_email =  input('Enter employee email(@nan.is): ')
            if new_emp_email[-7:] == "@nan.is":
                return new_emp_email
            print("Invalid email try again!")

    def check_destination(self):
        destination_list = ['Longyearbyen','Nuuk','Kulusuk','Thorshavn','Tingwall','Keflavik']
        destination = ""
        while destination not in destination_list:
            destination = input('Plese select a destination (Type destination id): ').upper()
            if destination in destination_list:
                print(destination)
                return destination
            print("Invalid destination Try again!")

    # def check_location(self,location):
    #     all_destinations = Destinations2Data().__destinations


