from Data.destinationsData import DestinationsData
from Data.Destinations2Data import Destinations2Data
from Logic.Destinations2_logic import Destinations2Logic
from Models.Destinations import Destinations
from Data.inputCheck import *
import os
clear = lambda: os.system('cls')

class DestinationsLogic:

    def all_destinations(self):
        all_destinations = DestinationsData().get_destinations()
        return all_destinations

    def print_all_destinations(self):
        all_destinations = self.all_destinations()
        for destination in all_destinations:
            print(destination)

    def get_destination(self,destination):
        all_destinations = self.all_destinations()
        for item in all_destinations:
            if item.get_Airport() == destination:
                return item

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

    def set_phonenumber(self,destination,new_phonenumber):
        return DestinationsData().set_phonenumber(destination,new_phonenumber)

    def create_new_destination(self,location,airport,flight_time,voyage_time,contact,phonenumber):
        new_destination = Destinations(location,airport,flight_time,voyage_time,contact,phonenumber)
        DestinationsData().add_destination(new_destination)
