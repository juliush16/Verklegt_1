
from Models.Upcomingflights import Upcomingflights
import csv

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

