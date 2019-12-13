class Upcomingflights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival, airplane = None, captain = None,copilot = None,fsm = None,fa1 = None,fa2 = None):
        self.flight_number = flight_number
        self.departing_from = departing_from
        self.arriving_at = arriving_at
        self.departure = departure
        self.arrival = arrival
        self.airplane = airplane
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2

    def get_flight_number(self):
        return self.flight_number
    
    def get_departing_from(self):
        return self.departing_from

    def get_arriving_at(self):
        return self.arriving_at

    def get_departure(self):
        return self.departure
    
    def get_arrival(self):
        return self.arrival
    
    def get_airplane(self):
        return self.airplane
    
    def get_captain(self):
        return self.captain

    def get_copilot(self):
        return self.copilot
    
    def get_fsm(self):
        return self.fsm

    def get_fa1(self):
        return self.fa1
    
    def get_fa2(self):
        return self.fa2

    def __str__(self):
        return ("{:<15}{:<15}{:<15}{:<25}{:<25}".format(self.flight_number,self.departing_from,self.arriving_at,self.departure,self.arrival))

