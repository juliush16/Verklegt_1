from Data.PastFlightsData import PastFlightsData


class PastFlightsLogic:

    def get_all_flights(self):
        all_flights = PastFlightsData().get_past_flight()
        return all_flights
