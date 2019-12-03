
from Models.Destinations import Destinations
import csv

class DestinationsRepo:

    def __init__(self):
        self.__destination = []

    def add_destination(self, destination):
        with open("./data/Destinations.csv", "a+") as destinations_file:
            location = destination.get_location()
            airport = destination.get_airport()
            flight_time = destination.get_flight_time()
            voyage_time = destination.get_voyage_time()
            contact = destination.get_contact()
            phonenumber  = destination.get_phonenumber()
            destinations_file.write("{},{},{},{},{},{},\n".format(location,
            airport,flight_time,voyage_time,contact,phonenumber))

    def get_destinations(self):
        if self.__aircraft == []:
            with open("./Data/destinations.csv", "r", encoding = "utf-8") as destinations_file:
                destination_reader = csv.reader(destinations_file)
                for line in destination_reader:
                    location = line[0]
                    airport = line[1]
                    flight_time = line[2]
                    voyage_time = line[3]
                    contact = line[4]
                    phonenumber = line[5]
                
                    new_destination = Destinations(location, airport, 
                    flight_time, voyage_time, contact, phonenumber)
                    self.__destination.append(new_destination)
        return self.__destination

    def all_destinations(self):
        return_list = []
        all_destinations = self.get_destinations()
        for car in all_destinations:
            return_list.append(Destinations)
        return return_list