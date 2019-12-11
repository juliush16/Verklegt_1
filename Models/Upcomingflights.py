#flightNumber,departingFrom,arrivingAt,departure,arrival 
class Upcomingflights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival, airplane = None, captain = None,copilot = None,fsm = None,fa1 = None,fa2 = None):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival
        self.__airplane = airplane
        self.__capatain = captain
        self.__copilot = copilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2

    def get_flight_number(self):
        return self.__flight_number
    
    def get_departing_from(self):
        return self.__departing_from

    def get_arriving_at(self):
        return self.__arriving_at

    def get_departure(self):
        return self.__departure
    
    def get_arrival(self):
        return self.__arrival
    
    def get_airplane(self):
        return self.__airplane
    
    def get_captain(self):
        return self.__capatain

    def get_copilot(self):
        return self.__copilot
    
    def get_fsm(self):
        return self.__fsm

    def get_fa1(self):
        return self.__fa1
    
    def get_fa2(self):
        return self.__fa2

    def __str__(self):
        return ("{:<15}{:<15}{:<15}{:<25}{:<25}".format(self.__flight_number,self.__departing_from,self.__arriving_at,self.__departure,self.__arrival))

