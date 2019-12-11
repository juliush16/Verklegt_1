
from Models.Upcomingflights import Upcomingflights
import csv

class VoyageRepo:

    def __init__(self):
        self.__voyage = []
        self.get_voyage #þessi

    def add_voyage(self, voyage):
        with open("./data/UpcomingFlights2.csv", "a+") as voyage_file:
            flight_number = voyage.get_flight_number()
            departing_from = voyage.get_departing_from()
            arriving_at = voyage.get_arriving_at()
            departure = voyage.get_departure()
            arrival = voyage.get_arrival()
            voyage_file.write("{},{},{},{},{}\n".format(flight_number,
            departing_from,arriving_at,departure,arrival))
            self.__voyage(voyage) #þessi


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
        number = random.randint(0,9999)
        return_str += str(number)
        return return_str

    def make_new_voyage(self):
        Destinations2 = Destinations2Repo()
        Destinations2.print_all_destinations()
        destination = input('Plese select a destination (Type destination id): ').capitalize()
        departure_date_and_time = input('\nPlease choose a departure date and time (DD/MM/YYYY/HH/MM) :')
        departure_list = departure_date_and_time.split('/')
        departure_date_iso = datetime.datetime(int(departure_list[2]),int(departure_list[1]),int(departure_list[0]),int(departure_list[3]),int(departure_list[4])).isoformat()
        arrival_date_iso = departure_date_iso
        parsed_date = dateutil.parser.parse(arrival_date_iso)
        destinations_ = DestinationsRepo()
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

            
            
