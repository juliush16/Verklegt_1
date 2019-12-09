
from Models.Upcomingflights import Upcomingflights
from Repo.Destinations2Repo import Destinations2Repo
from Repo.destinationsRepo import DestinationsRepo
import csv
import datetime
import dateutil.parser
import random

class VoyageRepo:

    def __init__(self):
        self.__voyage = []

    def add_voyage(self, voyage):
        with open("./data/UpcomingFlights2.csv", "a+") as voyage_file:
            flight_number = voyage.get_flight_number()
            departing_from = voyage.get_departing_from()
            arriving_at = voyage.get_arriving_at()
            departure = voyage.get_departure()
            arrival = voyage.get_arrival()
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

    def generate_flight_number(self):
        return_str = 'NA'
        number = random.randint(1000,9999)
        return_str += str(number)
        return return_str

    def get_arrival_time(self,destination, departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        flight_time = int(DestinationsRepo()._get_flight_time(destination))
        new_time = datetime.datetime(year,month,day,hour + flight_time,minutes).isoformat()
        return new_time

    def make_new_flight(self, arriving_at, departure, arrival,departing_from = 'KEF'):
        flight_num = self.generate_flight_number()
        new_flight = Upcomingflights(flight_num,departing_from,arriving_at,departure,arrival)
        self.add_voyage(new_flight)

    
    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format
        ("Flight Number:", "Departing From:", "Arriving At:", "Departure:", "Arrival:", "Aircraft Id:", 
        "Captein:", "Copilot:","Flight Service Manager:", "Flight Attendants")
        voyagelist = self.get_voyage()
        for voyage in voyagelist:
            string += str(voyage) + "\n"
        return string

            

