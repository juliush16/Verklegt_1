
from Repo.UpcomingVoyageRepo import VoyageRepo
from Repo.PastFlightsRepo import PastFlights
from Repo.AircraftRepo import AirCraftRepo
from Repo.Destinations2Repo import Destinations2Repo
from Repo.destinationsRepo import DestinationsRepo
from Repo.inputCheck import *

from Logic.Upcomig_voy_logic import UpcomingVoyageLogic
from Logic.Aircraft_logic import AircraftLog
from ui.destinations2_ui import Destinations2UI
from ui.destinations_ui import DestinationsUI

import datetime
import dateutil.parser

class VoyageUI:

    def menu(self):
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
                self.create_new_voyage_menu()
                choice_str = 'q'
            elif choice_str == '2':
                UpcomingVoyageLogic().print_all_upcoming_voyage()
            elif choice_str == '3':
                pass
            elif choice_str == '4':
                destinations_location = input("Please input contact location: ")
                DestinationsUI().update_contact(destinations_location)
            




    def create_new_voyage_menu(self):
        print('\n-----Make a new voyage-----\n')
        # print('\nSelect Airplane\n')
        # Aircrafts = AirCraftRepo()
        # Aircrafts.print_all_airplanes()
        # airplane = input('Please select an airplane (Type plane insignia) :').capitalize()

from Logic.Upcomig_voy_logic import UpcomingVoyageLogic
from Logic.Aircraft_logic import AircraftLog
from Logic.Destinations2_logic import Destinations2Logic
from ui.destinations2_ui import Destinations2UI
from ui.destinations_ui import DestinationsUI
import datetime
import dateutil.parser


class VoyageUI:

        if choice_str == 'q':
            return choice_str
        elif choice_str == '1':
            create_new_voyage_menu()
            choice_str = 'q'
        elif choice_str == '2':
            temp = VoyageRepo()
            temp.print_all_upcoming_voyage()
        elif choice_str == '3':
            past = PastFlights()
            past = print_past_flights()
        elif choice_str == '4':
            destinations_location = input("Please input contact location: ")
            temp = DestinationsRepo()
            temp.update_contact(destinations_location)
        
        print('\nSelect Destination\n') # Menu - Sækir upplýsingar
        Destinations2UI().print_all_destinations()
        destination = input('Plese select a destination (Type destination name): ').capitalize()
        departure_date_and_time = input('\nPlease choose a departure date and time (DD/MM/YYYY/HH/MM) :')
        if(departure_date_and_time == ""):
            departure_date_and_time = "09/12/2019/18/30"
        
        departure_list = departure_date_and_time.split('/')
        new_date = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()

        arrival_time = UpcomingVoyageLogic().get_arrival_time(destination,new_date) # Ná í arrival tíma.
        print(arrival_time)
        UpcomingVoyageLogic().make_new_flight(destination,new_date,arrival_time)        # Búa til nýtt flug með öllum upplýsingum
    def menu(self):
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
                self.create_new_voyage_menu()
                choice_str = 'q'
            elif choice_str == '2':
                UpcomingVoyageLogic().print_all_upcoming_voyage()
            elif choice_str == '3':
                pass
            elif choice_str == '4':
                destinations_location = input("Please input contact location: ")
                DestinationsUI().update_contact(destinations_location)
            

        print(('\nNew flight to "{}" has been created!\n').format(destination))



    def create_new_voyage_menu(self):
        print('\n-----Make a new voyage-----\n')
        # print('\nSelect Airplane\n')
        # Aircrafts = AirCraftRepo()
        # Aircrafts.print_all_airplanes()
        # airplane = input('Please select an airplane (Type plane insignia) :').capitalize()

        
        print('\nSelect Destination\n') # Menu - Sækir upplýsingar
        Destinations2UI().print_all_destinations()
        destination = input('Plese select a destination (Type destination name): ').capitalize()
        destination_id = Destinations2Logic().find_destination_id(destination)
        print(destination_id)
        departure_date_and_time = input('\nPlease choose a departure date and time (DD/MM/YYYY/HH/MM) :')
        if(departure_date_and_time == ""):
            departure_date_and_time = "09/12/2019/18/30"
        
        departure_list = departure_date_and_time.split('/')
        new_date = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()

        arrival_time = UpcomingVoyageLogic().get_arrival_time(destination_id,new_date) # Ná í arrival tíma.

        UpcomingVoyageLogic().make_new_flight(destination_id,new_date,arrival_time)        # Búa til nýtt flug með öllum upplýsingum

        print(('\nNew flight to "{}" has been created!\n').format(destination))

        
