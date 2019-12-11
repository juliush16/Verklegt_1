from Data.UpcomingVoyageData import VoyageData
from Logic.Destinations_logic import DestinationsLogic
from Logic.Destinations2_logic import Destinations2Logic
from Models.Upcomingflights import Upcomingflights
import datetime
import dateutil.parser
import random

class UpcomingVoyageLogic:

    def all_upcoming_voyage(self):
        all_voyage_list = []
        all_voyage = VoyageData().get_voyage()
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

    def get_arrival_time(self,destination_id, departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        destination = Destinations2Logic().find_destination(destination_id)
        flight_time = int(DestinationsLogic()._get_flight_time(destination))
        hour += flight_time
        if hour >= 23:
            day += 1
            hour -= 23
        new_time = datetime.datetime(year,month,day,hour,minutes).isoformat()
        return new_time

    def get_departure_time_back(self,departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        new_time = datetime.datetime(year,month,day,hour + 1,minutes).isoformat()
        return new_time


    def get_voyage_time(self,destination_id,departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        destination = Destinations2Logic().find_destination(destination_id)
        voyage_time = int(DestinationsLogic()._get_voyage_time(destination))
        hour += voyage_time
        if hour >= 23:
            day += 1
            hour -= 23
        new_time = datetime.datetime(year,month,day,hour,minutes).isoformat()
        return new_time

    def make_new_flight(self, arriving_at, departure, arrival,departing_from = 'KEF'):
        flight_num = self.generate_flight_number()  #bua til flugnumer
        flight_num_back = self.generate_flight_number() #bua til flugnumer
        arrival_time_back = self.get_voyage_time(arriving_at,departure)   #Nær í tíma sem að flug kemur til baka
        new_flight = Upcomingflights(flight_num,departing_from,arriving_at,departure,arrival) #bua til flug út
        flight_back = Upcomingflights(flight_num_back,arriving_at,'KEF',self.get_departure_time_back(arrival),self.get_voyage_time(arriving_at,departure))  #bua til flug til baka
        VoyageData().add_voyage(new_flight)
        VoyageData().add_voyage(flight_back)
            

