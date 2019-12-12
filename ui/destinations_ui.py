from Logic.Destinations_logic import DestinationsLogic
from Models.Destinations import Destinations
from Models.Destinations2 import Destinations2
from Data.Destinations2Data import Destinations2Data
from Logic.Destinations_logic import DestinationsLogic

import os
clear = lambda: os.system('cls')

class DestinationsUI:
    def selectin_dest(self):
        print('\nDestination Menu\n')
        choice = ''
        while choice != 'b':
            print('Select "1" to create a new destination')
            print('Select "2" to view all destinations')
            print('Select "3" to change contact for destination')
            print('press "b" to go back to Main Menu')
            choice = input("select action: ").lower()
            if choice == 'b':
                choice = 'b'
            elif choice == '1':
                choice = self.destinations_menu()
                print('\n')
                break
            elif choice == '2':
                choice = self.print_all_destinations()
                print('\n')
                break
            elif choice == '3':
                DestinationsLogic().print_all_destinations()
                airport = input("select airport: ")
                choice = self.update_contact(airport)
                break
                
        


    def destinations_menu(self):
        print('\n-----Create new destination-----\n')
        choice_str = input('You can type "b" to go back to the main menu or press enter to continue: ')
        if choice_str == 'b':
            return
        new_location = input('Please type new destination country: ').capitalize()
        new_airport = input('Please type new airport name: ').capitalize()
        new_loc_id = new_airport[:3].upper()
        new_flight_time = input('Please type new destination flight time (integer): ')
        new_voyage_time = (int(new_flight_time) * 2) + 1
        new_contact = input('Please type new destinations contact name: ').capitalize()
        new_phonenumber = input('Please type new contacts phone number: ')
        DestinationsLogic().create_new_destination(str(new_location),str(new_airport),new_flight_time,new_voyage_time,str(new_contact),str(new_phonenumber))
        new_dest2 = Destinations2(new_loc_id,new_location)
        Destinations2Data().add_destination(new_dest2)
        print('\nOverview :')
        print('\nAirport location: {} \nAirport name: {} \nContact name: {} \nContacts phonenumber: {}'.format(str(new_location),str(new_airport),str(new_contact),new_phonenumber))
        print('\nDestination has been created!\n')



    def print_all_destinations(self):
        all_destinations = DestinationsLogic().all_destinations()
        for destination in all_destinations:
            print(destination)

    def update_contact(self, airport):
        # self.print_all_destinations()

        # DestinationsLogic().all_destinations(airport)

        # if airport == None:
        #     print("Invalid Destination")
        #     return
        edit_contact = DestinationsLogic().get_destination(airport)
        destination = edit_contact
        print('\n')
        print(edit_contact)
        print('\n')
        choice = ''
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
                edit_contact.contact = new_contact
                DestinationsLogic().set_contact(destination,new_contact)
                break
            if choice == 2:
                print("Current phonenumber: {}".format(edit_contact.get_phonenumber()))
                new_phonenumber = input("Enter new phonenumber: ")
                edit_contact.phonenumber = new_phonenumber
                DestinationsLogic().set_phonenumber(destination,new_phonenumber)
                break
            if choice == 3:
                break

