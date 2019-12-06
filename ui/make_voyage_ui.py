from Repo.UpcomingVoyageRepo import VoyageRepo
from Repo.AircraftRepo import AirCraftRepo
from Repo.Destinations2Repo import Destinations2Repo
import datetime
def menu():
    choice_str = ''
    while choice_str != 'q':
        print('\n-----Make a voyage-----\n')
        print('Press "1" to make a new voyage')
        print('Press "2" to list all upcoming voyages')
        print('Press "3" to list all past voyages')
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




def create_new_voyage_menu():
    print('\n-----Make a new voyage-----\n')
    # print('\nSelect Airplane\n')
    # Aircrafts = AirCraftRepo()
    # Aircrafts.print_all_airplanes()
    # airplane = input('Please select an airplane (Type plane insignia) :').capitalize()
    print('\nSelect Destination\n')
    Destinations = Destinations2Repo()
    Destinations.print_all_destinations()
    destination = input('Plese select a destination (Type destination id): ').capitalize()
    print('\n')
    departure_date_and_time = input('Please choose a departure date and time (DD/MM/YYYY/HH/MM) :')
    departure_list = departure_date_and_time.split('/')
    new_date = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()
    print(new_date)


    ## Fyrst velja flugvél, svo áfangastað, svo tíma

    
