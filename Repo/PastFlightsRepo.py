from Models.PastFlights import PastFlights
import csv
#flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2
class PastFlights:

    def __init__(self):
        self.__voyage =[]

    def get_past_fligt(self,PastFlights):
        if self.__voyage == []:
            with open('./Data/PastFlights2.csv','r',encoding = 'utf-8') as past_file:
                past_flight_reader = csv.reader(past_file)
                for line in past_flight_reader:

                    flight_num = line[0]
                    departed_from = line[1]
                    arrived_at = line[2]
                    departure = line[3]
                    arrival = line[4]
                    voyage_past = PastFlights(flight_num,departed_from,arrived_at,departure,arrival)
                    self.__voyage.append(voyage_past)
        return self.__voyage_past
                #past_file.read("{},{},{},{},{}\n".format(flight_num,departed_from,arrived_at,departure,arrival))

    def all_past_voyage(self):
        all_past_flights_list = []
        all_past_flights = self.get_past_fligt()
        for line in all_past_flights:
            all_past_flights_list.append(line)
        return all_voyage_list

    def print_past_flights(self):
        all_past_flights = self.all_past_voyage()
        for line in all_past_flights:
            print(line)

    def __str__ (self):
        string = "{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}\n".format
        ("Flight Number:", "Departing From:", "Arriving At:", "Departure:", "Arrival:", "Aircraft Id:", 
        "Captain:", "Co pilot:","Flight Service Manager:", "Flight Attendants")
        past_list = self.get_past_fligt()
        for line in past_list:
            string += str(line) + "\n"
        return string

        

