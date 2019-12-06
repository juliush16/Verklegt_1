
from Models.Upcomingflights import Upcomingflights
import csv

class VoyageRepo:

    def __init__(self):
        self.__voyage = []

    def add_voyage(self, voyage):
        with open("./data/UpcomingFlights2.csv", "a+") as voyage_file:
            flight_number = Upcomingflights.get_flight_number()
            departing_from = Upcomingflights.get_departing_from
            arriving_at = Upcomingflights.get_arriving_at
            departure = Upcomingflights.get_departure
            arrival = Upcomingflights.get_arrival
            voyage_file.write("{},{},{},{},{}\n".format(flight_number,
            departing_from,arriving_at,departure,arrival))


    def get_voyage(self):
        if self.__voyage == []:
            with open("./Data/UpcomingFlights2.csv", "r", encoding = "utf-8") as voyage_file:
                voyage_reader = csv.reader(voyage_file)
                for line in voyage_reader:
                    flight_number = line[0]
                    departing_from = line[1]
                    arriving_at = line[2]
                    departure = line[3]
                    arrival = line[4]
                    new_voyage = Upcomingflights(flight_number, departing_from, arriving_at,
                    departure, arrival)
                    self.__voyage.append(new_voyage)
        return self.__voyage

    def all_upcoming_voyage(self):
        all_voyage_list = []
        all_voyage = self.get_voyage()
        for voyage in all_voyage:
            all_voyage_list.append(voyage)
        return all_voyage_list

    def print_all_upcoming_voyage(self):
        all_voyage = self.all_upcoming_voyage()
        for voyage in all_voyage:
            print(voyage)

    
    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format
        ("Flight Number:", "Departing From:", "Arriving At:", "Departure:", "Arrival:", "Aircraft Id:", 
        "Captein:", "Copilot:","Flight Service Manager:", "Flight Attendants")
        voyagelist = self.get_voyage()
        for voyage in voyagelist:
            string += str(voyage) + "\n"
        return string

            
            
