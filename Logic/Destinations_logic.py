from Data.destinationsData import DestinationsData
from Data.Destinations2Data import Destinations2Data
from Logic.Destinations2_logic import Destinations2Logic
from Data.inputCheck import *
import os
clear = lambda: os.system('cls')

class DestinationsLogic:

    def all_destinations(self):
        return_list = []
        all_destinations = DestinationsData().get_destinations()
        for destination in all_destinations:
            return_list.append(destination)
        return return_list

    def print_all_destinations(self):
        all_destinations = self.all_destinations()
        for destination in all_destinations:
            print(destination)

        
    def _get_flight_time(self,destination):
        all_destinations = DestinationsData().get_destinations()
        for dest in all_destinations:     
            if dest.get_Airport() == destination:
                return int(dest.get_flight_time())
    
    def _get_voyage_time(self,destination):
        all_destinations = DestinationsData().get_destinations()
        for dest in all_destinations:
            if dest.get_Airport() == destination: # Hvar er fallið get airport og hvað á það að gera
                return dest.get_voyage_time()
    
    def set_contact(self,destination,new_contact):
        return DestinationsData().set_contact(destination,new_contact)


    def create_new_destination(self,location,airport,flight_time,voyage_time,contact,phonenumber):
        new_destination = DestinationsData(location,airport,flight_time,voyage_time,contact,phonenumber)
        DestinationsData().add_destination(new_destination)
