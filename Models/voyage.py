class Voyage:

    def __init__(self,flight_number, departing_from, arriving_at, departure, arrival, aircraft_id,captain = None, copilot = None, flight_service_manager = None, flight_attendants = None):
        self.flight_number = flight_number
        self.departing_from = departing_from
        self.arriving_at = arriving_at
        self.departure = departure
        self.arrival = arrival
        self.aircraft_id = aircraft_id
        self.captain = captain
        self.copilot = copilot
        self.flight_service_manager = flight_service_manager
        self.flight_attendants = flight_attendants


    def get_flight_number(self):
        return str(self.flight_number)

    def get_departing_from(self):
        return str(self.departing_from)

    def get_arriving_at(self):
        return str(self.arriving_at)

    def get_departure(self):
        return str(self.departure)
    
    def get_arrival(self):
        return str(self.arrival)
        
    def get_aircraft_id(self):
        return str(self.aircraft_id)

    def get_captain(self):
        return str(self.captain)

    def get_copilot(self):
        return str(self.copilot)

    def get_flight_service_manager(self):
        return str(self.flight_service_manager)

    def get_flight_attendants(self):
        return str(self.flight_attendants)

    def __str__(self):
        return ("{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}{:<15}{:<15}".format
        (self.flight_number,self.departing_from,self.arriving_at,
        self.departure,self.arrival,self.aircraft_id,self.captain,self.copilot,
        self.flight_service_manager,self.flight_attendants))
