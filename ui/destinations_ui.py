from Logic.Destinations_logic import DestinationsLogic
from Models.Destinations import Destinations
from Models.Destinations2 import Destinations2
from Data.Destinations2Data import Destinations2Data
import os
clear = lambda: os.system('cls')

class DestinationsUI:

    def destinations_menu(self):
        print('\n-----Create new destination-----\n')
        choice_str = input('You can type "b" to go back to the main menu or press enter to continue :')
        if choice_str == 'b':
            return
        new_location = input('Please type new destination country :').capitalize()
        new_airport = input('Please type new airport name :').capitalize()
        new_loc_id = new_airport[:3].upper()
        new_flight_time = input('Please type new destination flight time (integer) :')
        new_voyage_time = (int(new_flight_time) * 2) + 1
        new_contact = input('Please type new destinations contact name :').capitalize()
        new_phonenumber = input('Please type new contacts phone number :')
        DestinationsLogic().create_new_destination(str(new_location),str(new_airport),new_flight_time,new_voyage_time,str(new_contact),str(new_phonenumber))
        new_dest2 = Destinations2(new_loc_id,new_location)
        Destinations2Data().add_destination(new_dest2)
        print('\nOverview :')
        print('\nAirport location : {} \nAirport name : {} \nContact name : {} \nContacts phonenumber : {}'.format(str(new_location),str(new_airport),str(new_contact),new_phonenumber))
        print('\nDestination has been created!\n')



    def print_all_destinations(self):
        all_destinations = DestinationsLogic().all_destinations()
        for destination in all_destinations:
            print(destination)


    def update_contact(self, airport):
        choice = ''
        while choice != '3':
            print("1. Edit Contact\n2. Edit Phonenumber\n3. Return to Main Menu\n")
            choice = int(input("Choose :"))
            


            



        #select_dest = input("Please select destination to edit: ")
        all_location = DestinationsLogic().all_destinations()
        if all_location == None:
            print("Invalid Destination")
            return
        for contact in all_location:
            if contact.get_Airport() == airport:
                edit_contact = contact
                contact_string = ("\n{}{}\n{}{}\n".format('Contact Name: ',edit_contact.get_contact(),'Phonenumber: ',edit_contact.get_phonenumber()))
        for destination in all_location:
            if destination.get_Airport() == airport:
                edit_contact = destination
                contact_string = ("\n{}{}\n{}{}\n".format('Contact Name: ',destination.get_contact(),'Phonenumber: ',destination.get_phonenumber()))
                print(contact_string)
                print("1. Edit Contact\n2. Edit Phonenumber\n3. Return to Main Menu\n")

                #while True:
                    #choice = int(input("What do you want to edit? "))
                    #if choice < 1 or choice > 3:
                      #  print("Choice invalid! Try again")
                      #  clear()
                   # else:
                    #    break
                choice = ''
                while choice != '3':
                    choice = int(input("What do you want to edit? "))
                    if choice == '1':
                        print("Current contact name: {}".format(edit_contact.get_contact()))
                        new_contact = input("Enter new contact name: ")
                        edit_contact.contact = new_contact
                        break
                    if choice == '2':
                        print("Current phonenumber: {}".format(edit_contact.get_phonenumber()))
                        new_phonenumber = input("Enter new phonenumber: ")
                        edit_contact.phonenumber = new_phonenumber
                        break
                    if choice == '3':
                        break