from Repo.EmployeeRepo import EmployeeRepo as Emp_Repo
from Repo.UpcomingVoyageRepo import VoyageRepo as Voy_Repo

def menu():
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
            assign_pilots_menu()
        elif choice_str == '2':
            assign_flight_attendants_menu()
        elif choice_str == '3':
            pass # Kalla í listann yfir past flights
        elif choice_str == 'b':
            return choice_str


def assign_pilots_menu():
    choice_str = ''
    while choice_str != 'b':
        voyage_list = [] #Listi fyrir ferðir fyrir valinn dag
        choose_day_to_employ = input("Please type day to employ (DD/MM/YYYY): ")
        all_voyage = Voy_Repo().get_voyage()
        for voyage in all_voyage:
            if voyage.__departure == choose_day_to_employ:
                voyage_list.append(voyage)
        for item in voyage_list:
            print(item)

        if not voyage_list: # ef engar ferðir skráðar
            print('There are no trips on this day')
            


def assign_flight_attendants_menu():
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


        


if __name__ == "__main__":
    menu()