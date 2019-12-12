
from Models.Destinations import Destinations
import csv

class DestinationsData:

    def __init__(self):
        self.__destination = []
        #self.get_destinations() #þessi
        pass

    def add_destination(self, destination):
        with open("./Repo/Destinations.csv", "a+") as destinations_file:
            location = destination.get_location()
            airport = destination.get_airport()
            flight_time = destination.get_flight_time()
            voyage_time = destination.get_voyage_time()
            contact = destination.get_contact()
            phonenumber  = destination.get_phonenumber()
            destinations_file.write("{},{},{},{},{},{},\n".format(location,
            airport,flight_time,voyage_time,contact,phonenumber))
            self.__destination.append(destination) #þessi

    def get_destinations(self):
        if self.__destination == []:
            with open("./Repo/destinations.csv", "r", encoding = "utf-8") as destinations_file:
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

    def set_contact(self,destination,new_contact):
        all_destinations = self.get_destinations()  
        r = csv.reader(open('./Repo/destinations.csv'))
        lines = list(r)
        destination_num = 0
        for line in all_destinations:
            if line == destination:
                destination_num = line
        
            lines[destination_num][4] = new_contact
            writer = csv.writer(open('./Repo/destinations.csv', 'w'))
            writer.writerows(lines)
        if destination_num != 0:
            return '\nContact has been changed to "' + str(new_contact) + '"'
        else:
            return '\nError: contact could not be edited'



