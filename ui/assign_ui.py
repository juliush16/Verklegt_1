from Logic.Upcomig_voy_logic import UpcomingVoyageLogic
from ui.aircraftUI import Aircraft_UI
from ui.employee_ui import EmployeeUI
from Logic.get_pilots_license import PilotLicence
from Data.inputCheck import InputCheck
from datetime import datetime

class AssignUI:

    def menu(self):
        choice_str = ''
        while choice_str != 'q':
            print('\n---Assign employees to a voyage---\n')
            print('Press "1" to assign staff members to a voyage')
            print('Press "2" to print employees working on a speciffic date')
            print('Press "2" to print employees NOT working on a speciffic date')
            print('Press "q" to Quit')
            print('Press "b" to go back to Main Menu\n')
            choice_str = input('Choose an option: ')

            if choice_str == 'q':
                return choice_str
            elif choice_str == '1':
                self.assign_staff_menu()
            elif choice_str == '2':
                self.get_employee_by_date()
            elif choice_str == '3':
                self.get_employee_not_working()
            elif choice_str == 'b':
                return choice_str

    def get_date(self):
        date = input('Please input date :(YYYY-MM-DD)')
        dArr = date.split("-")
        retDate = datetime(int(dArr[0]), int(dArr[1]), int(dArr[2]))
        return retDate

    def get_employee_by_date(self):
        date = self.get_date()
        employee_lis = UpcomingVoyageLogic().get_staff_by_date(date)
        for employee in employee_lis:
            if employee == None:
                pass
            else:
                EmployeeUI().print_by_ssn(employee)
    
    def get_employee_not_working(self):
        date = self.get_date()
        employee_lis = UpcomingVoyageLogic().get_not_working(date)
        for employee in employee_lis:
            print(employee)



    def assign_staff_menu(self):
        print("\n-----Assign Pilots to Voyage-----\n")
        self.print_from_kef()
        choose_flight = input("Please select flight (type the integer): ")
        flights_from_kef = UpcomingVoyageLogic().get_from_kef()
        choose_day_to_employ = flights_from_kef[int(choose_flight) -1]
        print()
        voyage_update = UpcomingVoyageLogic().get_by_voyage(choose_day_to_employ) #sækja listann og velja flugnúmer
        if voyage_update == None: #ef flugnúmerið er ekki til prenta ut invalid voyage
            print("Invalid voyage")
            return
        Aircraft_UI().print_all_airplanes() #fá flugvéla lista
        voyage_update.airplane = input("Select Airplane: ")
        PilotLicence().get_pilots_wLicence(voyage_update.airplane) #ALLA MEÐ LEYFI A X VÉLAR
        print("\nSelect Captain\n")
        voyage_update.captain = InputCheck().check_ssn()
        print("\nSelect Copilot\n")
        voyage_update.copilot = InputCheck().check_ssn()
        #########################################################
        EmployeeUI().print_all_flight_service_managers() #PRENTA ALLAN FLIGHT SERVICE MANAGER
        print("\nSelect Flight Service Manager\n")
        voyage_update.fsm = InputCheck().check_ssn()
        EmployeeUI().print_all_flight_attendants() #PRENTA ALLAN FLIGHT ATTENDANTS
        print("\nSelect Flight Attendant\n")
        voyage_update.fa1 = InputCheck().check_ssn()
        more_attendants = ''
        while more_attendants != 'N':
            more_attendants = input('Do you want to add another flight attendant?(Y/N) :').upper()
            if more_attendants == 'Y':
                voyage_update.fa2 = InputCheck().check_ssn()
                more_attendants = 'N'
            elif more_attendants == 'N':
                break
            else:
                print('Try again! \n')
        UpcomingVoyageLogic().update_voyage(voyage_update)


    def print_from_kef(self):
        flights_from_kef = UpcomingVoyageLogic().get_from_kef()
        i = 0
        for flight in flights_from_kef:
            i += 1
            if i <10:
                print( str(i) + ') ', end=' ')
                print(flight)
            else:
                print( str(i) + ')', end=' ')
                print(flight)

                        
'''
    def assign_flight_attendants_menu(self):
        UpcomingVoyageLogic().print_all_upcoming_voyage()
        choose_day_to_employ = input("Please type flight number: ").upper()
        print()
        voyage_update = UpcomingVoyageLogic().get_by_voyage(choose_day_to_employ) #sækja listann og velja flugnúmer
        if voyage_update == None: #ef flugnúmerið er ekki til prenta ut invalid voyage
            print("Invalid voyage")
            return
        EmployeeUI().print_all_flight_service_managers() #PRENTA ALLAN FLIGHT SERVICE MANAGER
        voyage_update.fsm = input("Select Flight Service Manager: ")
        EmployeeUI().print_all_flight_attendants() #PRENTA ALLAN FLIGHT ATTENDANTS
        voyage_update.fa1 = input("Select Flight Attendant: ")
        voyage_update.fa2 = input("Select Flight Attendant: ")
        UpcomingVoyageLogic().update_voyage(voyage_update) #UPDATEA NYJA LISTANN 
'''
        #for i in airplane:
           # if(str(str(i).split()[1]) == choosen_airplane.strip()):
              #  print("HEllo")
            #if(str(str(up).split()[3]).strip() == new_date.strip()):
            #    print("nei") # stoppa 
        #all_aircrafts = AircraftLog().get_all_airplanes()
        #for a in all_aircrafts:
        #    print(a)

        #EmployeeUI().print_all_pilots()
        #captain = input("Select capatain: ") # vantar virkni svo copilot skráist

        #copilot = input("Select Co Pilot: ") # líka hér


# vantar að bjóða að savea eða edita






