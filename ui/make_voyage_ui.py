from Repo.UpcomingVoyageRepo import VoyageRepo
from Repo.AircraftRepo import AirCraftRepo
from Repo.Destinations2Repo import Destinations2Repo
from Repo.destinationsRepo import DestinationsRepo
import datetime
import dateutil.parser
def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Make a voyage-----\n')
        print('Press "1" to make a new voyage')
        print('Press "2" to list all upcoming voyages')
        print('Press "3" to list all past voyages')
        print('Press "4" to change contact information')
        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            create_new_voyage_menu()
            choice_str = 'q'
        elif choice_str == '2':
            temp = VoyageRepo()
            temp.print_all_upcoming_voyage()
        elif choice_str == '3':
            pass
        elif choice_str == '4':
            destinations_location = input("Please input contact location: ")
            temp = DestinationsRepo()
            temp.update_contact(destinations_location)
        




def create_new_voyage_menu():
    print('\n-----Make a new voyage-----\n')
    # print('\nSelect Airplane\n')
    # Aircrafts = AirCraftRepo()
    # Aircrafts.print_all_airplanes()
    # airplane = input('Please select an airplane (Type plane insignia) :').capitalize()

    
    print('\nSelect Destination\n') # Menu - Sækir upplýsingar
    Destinations2Repo().print_all_destinations()
    destination = input('Plese select a destination (Type destination name): ').capitalize()
    departure_date_and_time = input('\nPlease choose a departure date and time (DD/MM/YYYY/HH/MM) :')
    if(departure_date_and_time == ""):
        departure_date_and_time = "09/12/2019/18/30"
    
    departure_list = departure_date_and_time.split('/')
    new_date = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()

    arrival_time = VoyageRepo().get_arrival_time(destination,new_date) # Ná í arrival tíma.
    print(arrival_time)
    VoyageRepo().make_new_flight(destination,new_date,arrival_time)        # Búa til nýtt flug með öllum upplýsingum

    print(('\nNew flight to "{}" has been created!\n').format(destination))

    
