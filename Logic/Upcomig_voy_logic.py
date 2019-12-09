from Repo.UpcomingVoyageRepo import VoyageRepo
from Logic.Destinations_logic import DestinationsLogic
from Models.Upcomingflights import Upcomingflights
import datetime
import dateutil.parser
import random

class UpcomingVoyageLogic:

    def all_upcoming_voyage(self):
        all_voyage_list = []
        all_voyage = VoyageRepo().get_voyage()
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
        flight_time = int(DestinationsLogic()._get_flight_time(destination))
        new_time = datetime.datetime(year,month,day,hour + flight_time,minutes).isoformat()
        return new_time

    def make_new_flight(self, arriving_at, departure, arrival,departing_from = 'KEF'):
        flight_num = self.generate_flight_number()
        new_flight = Upcomingflights(flight_num,departing_from,arriving_at,departure,arrival)
        VoyageRepo().add_voyage(new_flight)
            

