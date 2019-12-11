from Repo.destinationsRepo import DestinationsRepo
from Repo.Destinations2Repo import Destinations2Repo
from Logic.Destinations2_logic import Destinations2Logic
from Repo.inputCheck import *
import os
clear = lambda: os.system('cls')

class DestinationsLogic:

    def all_destinations(self):
        return_list = []
        all_destinations = DestinationsRepo().get_destinations()
        for destination in all_destinations:
            return_list.append(destination)
        return return_list

    def print_all_destinations(self):
        all_destinations = self.all_destinations()
        for destination in all_destinations:
            print(destination)

        
        
    def _get_flight_time(self,destination_id):
        all_destinations = DestinationsRepo().get_destinations()
        destination = Destinations2Logic().find_destination(destination_id)
        for dest in all_destinations:
            if dest.get_Airport() == destination:
                return str(dest.get_flight_time())
    
    def _get_voyage_time(self,destination):
        all_destinations = DestinationsRepo().get_destinations()
        for dest in all_destinations:
            if dest.get_Airport() == destination:
                return dest.get_voyage_time()
    
    def set_contact(self,destination,new_contact):
        return DestinationsRepo().set_contact(destination,new_contact)


    def create_new_destination(self,location,airport,flight_time,voyage_time,contact,phonenumber):
        new_destination = Destinations(location,airport,flight_time,voyage_time,contact,phonenumber)
        DestinationsRepo().add_destination(new_destination)
