
from Models.Upcomingflights import Upcomingflights
from Data.Destinations2Data import Destinations2Data
from Data.destinationsData import DestinationsData
import random
import csv
from datetime import datetime
import dateutil.parser

class VoyageData:
    def add_voyage(self, voyage):
        with open("./Repo/UpcomingFlights2.csv", "a+") as voyage_file:
            flight_number = voyage.get_flight_number()
            departing_from = voyage.get_departing_from()
            arriving_at = voyage.get_arriving_at()
            departure = voyage.get_departure()
            arrival = voyage.get_arrival()
            airplane = voyage.get_airplane()
            captain = voyage.get_captain()
            copilot = voyage.get_copilot()
            fsm = voyage.get_fsm()
            fa1 = voyage.get_fa1()
            fa2 = voyage.get_fa2()
            voyage_file.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(flight_number,
            departing_from,arriving_at,departure,arrival, airplane,captain,copilot,fsm,fa1,fa2))

#self,flight_number,departing_from,arriving_at,departure,arrival, airplane = None, captain = None,copilot = None,fsm = None,fa1 = None,fa2 = None
    def get_voyage(self):
        retLis = []
        with open("./Repo/UpcomingFlights2.csv", "r", encoding = "utf-8") as voyage_file:
            voyage_reader = csv.reader(voyage_file)
            for line in voyage_reader:
                flight_number = line[0]
                departing_from = line[1]
                arriving_at = line[2]
                departure = line[3]
                arrival = line[4]
                airplane = line[5]
                captain = line[6]
                copilot = line[7]
                fsm = line[8]
                fa1 = line[9]
                fa2 = line[10]
                    
                new_voyage = Upcomingflights(flight_number, departing_from, arriving_at,
                departure, arrival, airplane, captain, copilot, fsm, fa1, fa2)
                retLis.append(new_voyage)
        return retLis

    def all_upcoming_voyage(self):
        all_voyage_list = []
        all_voyage = self.get_voyage()
        for voyage in all_voyage:
            all_voyage_list.append(voyage)
        return all_voyage_list

    def generate_flight_number(self):
        return_str = 'NA'
        number = random.randint(0,9999)
        return_str += str(number)
        return return_str

    def make_new_voyage(self):
        Destinations2 = Destinations2Data()
        Destinations2.print_all_destinations()
        destination = input('Plese select a destination (Type destination id): ').capitalize()
        departure_date_and_time = input('\nPlease choose a departure date and time (DD/MM/YYYY/HH/MM) :')
        departure_list = departure_date_and_time.split('/')
        departure_date_iso = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()
        arrival_date_iso = departure_date_iso
        parsed_date = dateutil.parser.parse(arrival_date_iso)
        destinations_ = DestinationsData()
        parsed_date.hour += destinations_.get_flight_time()
        self.make_new_flight(destination,departure_date_iso,arrival_date_iso)

    def make_new_flight(self, arriving_at, departure, arrival,departing_from = 'KEF'):
        flight_num = self.generate_flight_number()
        new_flight = Upcomingflights(flight_num,departing_from,arriving_at,departure,arrival)
        self.add_voyage(new_flight)

    def __str__(self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format
        ("Flight Number:", "Departing From:", "Arriving At:", "Departure:", "Arrival:", "Aircraft Id:", 
        "Captain:", "Co pilot:","Flight Service Manager:", "Flight Attendants")
        voyagelist = self.get_voyage()
        for voyage in voyagelist:
            string += str(voyage) + "\n"
        return string

    def _update_voyage(self, updatedvoyage):
        allvoyage = self.get_voyage()
        with open("./Repo/UpcomingFlights2.csv", "w+", newline="") as voyage_file:
            fieldnames = ["flightNumber","departingFrom","arrivingAt","departure","arrival","airplane","captain","copilot","fsm","fa1","fa2"]
            writer = csv.DictWriter(voyage_file, fieldnames=fieldnames)
            writer.writeheader()

        i = 1
        while(i < len(allvoyage)):
            if updatedvoyage.flight_number == allvoyage[i].flight_number:
                self.add_voyage(updatedvoyage)
                allvoyage[i+1].airplane = updatedvoyage.airplane
                allvoyage[i+1].captain = updatedvoyage.captain
                allvoyage[i+1].copilot = updatedvoyage.copilot
                allvoyage[i+1].fsm = updatedvoyage.fsm
                allvoyage[i+1].fa1 = updatedvoyage.fa1
                allvoyage[i+1].fa2 = updatedvoyage.fa2
                self.add_voyage(allvoyage[i+1])
            else:
                self.add_voyage(allvoyage[i])
                self.add_voyage(allvoyage[i+1])
            i += 2
