
from Models.Destinations import Destinations
import csv
clear = lambda: os.system('cls')

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
        if self.__destination == []:
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
        for destination in all_destinations:
            return_list.append(destination)
        return return_list

    def print_all_destinations(self):
        all_destinations = self.all_destinations()
        for destination in all_destinations:
            print(destination)

    def get_flight_time(self,destination):
        all_destinations = self.all_destinations()
        for dest in all_destinations:
            if dest.__location == destination:
                return int(dest.__flight_time)
        

    def create_new_destination(self,location,airport,flight_time,voyage_time,contact,phonenumber):
        new_destination = Destinations(location,airport,flight_time,voyage_time,contact,phonenumber)
        self.add_employee(new_destination)

    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}\n".format
        ("Location:","Airport","Flight Time","Voyage Time","Contact","Phonenumber")
        destinationslist = self.get_destinations()
        for destination in destinationslist:
            string += str(destination) + "\n"
        return string

    def update_contact(self, location):
        all_location = self.get_destinations()
        for contact in all_location:
            if destinations.get_Location() == location:
                edit_contact = contact

                contact_string = ("\n{}{}\n{}{}\n".format('Contact Name: ',destinations.contact,'Phonenumber: ',destinations.phonenumber))
                print(contact_string)
                print("1. Edit Contact\n2. Edit Phonenumber\n3. Return to Main Menu\n")

                while True:
                    choice = int(input("What do you want to edit?"))
                    if choice < 1 or choice > 3:
                        print("Choice invalid! Try again")
                        clear()
                    else:
                        break
                while True:
                    if choice == 1:
                        print("Current contact name: {}".format(edit_contact.get_contact()))
                        new_contact = input("Enter new contact name: ")
                        edit_contact.set_contact(new_contact)
                        break
                    if choice == 2:
                        print("Current phonenumber: {}".format(edit_contact.get_phonenumber()))
                        new_phonenumber = input("Enter new phonenumber: ")
                        edit_contact.set_phonenumber(new_phonenumber)
                        break
                    if choice == 3:
                        break