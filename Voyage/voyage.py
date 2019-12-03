class Voyage:

    def __init__(self,flight_number, departingFrom, ArrivingAt, departure, arrival, aircraftID,captain = None, copilot = None, flight_service_manager = None, flight_attendants = None):
        self.flight_number = flight_number
        self.departing_From = departing_from
        self.arrivingAt = Arriving_at
        self.departure = departure
        self.arrival = arrival
        self.aircraft_ID = aircraftID
        self.captain = captain
        self.copilot = copilot
        self.fsm = flight_service_manager
        self.flight_attendants = flight_attendants


    def get_flight_number(self):
        return str(self.flight_number)

    def get_departingFrom(self):
        return str(self.departing_from)

    def get_arrivingAT(self):
        return str(self.arriving_at)

    def get_departure(self):
        return str(self.departure)
    
    def get_arrival(self):
        return str(self.arrival)
        
    def get_aircraftID(self):
        return str(self.aircraft_ID)

    def get_captain(self):
        return str(self.captain)

    def get_copilot(self):
        return str(self.copilot)

    def get_fsm(self):
        return str(self.fsm)

    def get_flight_attendants(self):
        return str(self.flight_attendants)