
from Models.Destinations import Destinations
import csv

class DestinationsData:

    def add_destination(self, destination):
        with open("./Repo/Destinations.csv", "a+") as destinations_file:
            location = destination.get_Location()
            airport = destination.get_Airport()
            flight_time = destination.get_flight_time()
            voyage_time = destination.get_voyage_time()
            contact = destination.get_contact()
            phonenumber  = destination.get_phonenumber()
            destinations_file.write("{},{},{},{},{},{},\n".format(location,
            airport,flight_time,voyage_time,contact,phonenumber))
            self.__destination.append(destination) #þessi

    def get_destinations(self):
        destinations = []
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
                destinations.append(new_destination)
        return destinations

    def set_contact(self,destination,new_contact):
        all_destinations = self.get_destinations()  
        r = csv.reader(open('./Repo/destinations.csv'))
        lines = list(r)
        counter = 0
        for line in all_destinations:
            counter += 1
            if line.get_Airport() == destination.get_Airport():
                lines[counter][4] = new_contact
            writer = csv.writer(open('./Repo/destinations.csv', 'w'))
            writer.writerows(lines)
        return '\nContact has been changed to "' + str(new_contact) + '"'

    def set_phonenumber(self,destination,new_phonenumber):
        all_destinations = self.get_destinations()  
        r = csv.reader(open('./Repo/destinations.csv'))
        lines = list(r)
        counter = 0
        for line in all_destinations:
            counter += 1
            if line.get_Airport() == destination.get_Airport():
                lines[counter][5] = new_phonenumber
            writer = csv.writer(open('./Repo/destinations.csv', 'w'))
            writer.writerows(lines)
        return '\nPhonenumber has been changed to "' + str(new_phonenumber) + '"'



