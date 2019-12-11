from Repo.EmployeeRepo import EmployeeRepo
from Logic.Upcomig_voy_logic import UpcomingVoyageLogic

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
                pass # Kalla í listann yfir past flights
            elif choice_str == 'b':
                return choice_str


    def assign_pilots_menu(self):
        UpcomingVoyageLogic().print_all_upcoming_voyage()
        choose_day_to_employ = input("Please type flight number: ").upper()
        print(choose_day_to_employ)
            
                


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