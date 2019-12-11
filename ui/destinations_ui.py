from Logic.Destinations_logic import DestinationsLogic
from Models.Destinations import Destinations

class DestinationsUI:

    def print_all_destinations(self):
        all_destinations = DestinationsLogic.all_destinations()
        for destination in all_destinations:
            print(destination)


    def update_contact(self, location):
        all_location = DestinationsLogic().all_destinations()
        for contact in all_location:
            if Destinations().get_Location() == location:
                edit_contact = contact

                contact_string = ("\n{}{}\n{}{}\n".format('Contact Name: ',destinations.contact,'Phonenumber: ',destinations.phonenumber))
        for destination in all_location:
            if destination.get_Location() == location:
                edit_contact = destination
                contact_string = ("\n{}{}\n{}{}\n".format('Contact Name: ',destination.get_contact(),'Phonenumber: ',destination.get_phonenumber()))
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
                        print(DestinationsLogic().set_contact(edit_contact,new_contact))
                        break
                    if choice == 2:
                        print("Current phonenumber: {}".format(edit_contact.get_phonenumber()))
                        new_phonenumber = input("Enter new phonenumber: ")
                        edit_contact.set_phonenumber(new_phonenumber)
                        break
                    if choice == 3:
                        break