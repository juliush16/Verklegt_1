from Logic.PastFlights_logic import PastFlightsLogic

class PastFlightsUI:

    def print_past_flights(self):
        all_past_flights = PastFlightsLogic().get_all_flights()
        for line in all_past_flights:
            print(line)