from Data.EmployeeData import EmployeeData
from Logic.Upcomig_voy_logic import UpcomingVoyageLogic
from ui.aircraftUI import Aircraft_UI
from ui.employee_ui import EmployeeUI
from Logic.get_pilots_license import PilotLicence
from Data.PastFlightsData import PastFlightsData
from Models.PastFlights import PastFlights

class AssignUI:

    def menu(self):
        choice_str = ''
        while choice_str != 'q':
            print('\n---Assign eployees to a voyage---\n')
            print('Press "1" to assign Pilots to a voyage')
            print('Press "2" to assign Flight Attendant to a voyage')
            print('Press "3" to print past Voyages')
            print('Press "q" to Quit')
            print('Press "b" to go back to Main Menu\n')
            choice_str = input('Choose an option: ')

            if choice_str == 'q':
                return choice_str
            elif choice_str == '1':
                self.assign_pilots_menu()
            elif choice_str == '2':
                self.assign_flight_attendants_menu()
            elif choice_str == '3':
                past = PastFlights()
                past = print_past_flights()
            elif choice_str == 'b':
                return choice_str


    def assign_pilots_menu(self):
        print("\n-----Assign Pilots to Voyage-----\n")
        UpcomingVoyageLogic().print_all_upcoming_voyage()
        choose_day_to_employ = input("Please type flight number: ").upper()
        
        #return choose_day_to_employ
        Aircraft_UI().print_all_airplanes()
        airplane = input("Select Airplane: ")
        PilotLicence().get_pilots_wLicence(airplane)
        captain = input("Select Captain: ")
        copilot = input("Select Co Pilot: ")
        
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

                        

    def assign_flight_attendants_menu(self):
        choice_str = ''
        while choice_str != 'b':
            print('\n---Assign flight attendants to voyage---\n')
            print('Press "1" to see all upcoming voyages')  # Ekki buinn að utfæra þennan option
            print('Press "b" to go back to Main Menu!\n')
            choice_str = input('Choose an option: ')

            if choice_str == 'b':
                return choice_str
            elif choice_str == '1':
                pass

