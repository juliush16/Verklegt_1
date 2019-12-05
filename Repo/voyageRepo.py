
from Models.voyage import Voyage
import csv

class VoyageRepo:

    def __init__(self):
        self.__voyage = []

    def add_voyage(self, voyage):
        with open("./data/Destinations2.csv", "a+") as voyage_file:
            flight_number = voyage.get_flight_number()
            departing_from = voyage.get_departing_from()
            arriving_at = voyage.get_arriving_at()
            departure = voyage.get_departure()
            arrival = voyage.get_arrival()
            aircraft_id = voyage.get_aircraft_id()
            captain = voyage.get_captain()
            copilot = voyage.get_copilot()
            flight_service_manager = voyage.get_flight_service_manager()
            flight_attendants = voyage.get_flight_attendants()
            voyage_file.write("{},{},{},{},{},{},{},{},{},{}\n".format(flight_number,
            departing_from,arriving_at,departure,arrival,aircraft_id,captain,
            copilot,flight_service_manager,flight_attendants))

    def get_voyage(self):
        if self.__voyage == []:
            with open("./Data/Destinations2.csv", "r", encoding = "utf-8") as voyage_file:
                voyage_reader = csv.reader(voyage_file)
                for line in voyage_reader:
                    flight_number = line[0]
                    departing_from = line[1]
                    arriving_at = line[2]
                    departure = line[3]
                    arrival = line[4]
                    aircraft_id = line[5]
                    captein = line[6]
                    copilot = line[7]
                    flight_service_manager = line[8]
                    flight_attendants = line[9]
                    new_voyage = Voyage(flight_number, departing_from, arriving_at,
                    departure, arrival, aircraft_id, captein, copilot, 
                    flight_service_manager, flight_attendants)
                    self.__voyage.append(new_voyage)
        return self.__voyage

    def all_voyage(self):
        all_voyage_list = []
        all_voyage = self.get_voyage()
        for employee in all_voyage:
            all_voyage_list.append(Voyage)
        return all_voyage_list

    
    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format
        ("Flight Number:", "Departing From:", "Arriving At:", "Departure:", "Arrival:", "Aircraft Id:", 
        "Captein:", "Copilot:","Flight Service Manager:", "Flight Attendants")
        voyagelist = self.get_voyage()
        for car in voyagelist:
            string += str(Voyage) + "\n"
        return string

            
            

