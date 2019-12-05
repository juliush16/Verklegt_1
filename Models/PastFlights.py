#flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2
class PastFlights:
    def __init__(self,flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2):
        self.__flightNumber = flightNumber
        self.__departingFrom = departingFrom
        self.__arrivingAt = arrivingAt
        self.__departure = departure 
        self.__arrival = arrival 
        self.__aircraftID = aircraftID
        self.__captain = captain
        self.__copilot = copilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2

    def __str__(self):
        return ("{}{}{}{}{}{}{}{}{}{}{}".format(self.__flightNumber,self.__departingFrom,self.__arrivingAt,self.__departure,self.__arrival,self.__arrival,self.__aircraftID,self.__captain,self.__copilot,self.__fsm,self.__fa1,self.__fa2))

    def get_flightNumber(self):
        return self.__flightNumber
    
    def get_departingFrom(self):
        return self.__departingFrom

    def get_arrivingAt(self):
        return self.__arrivingAt

    def get_departure(self):
        return self.__departure

    def get_arrival(self):
        return self.__arrival
    
    def get_aircraftID(self):
        return self.__aircraftID
    
    def get_captain(self):
        return self.__captain
    
    def get_copilot(self):
        return self.__copilot
    
    def get_fsm(self):
        return self.__fsm
    
    def get_fa1(self):
        return self.__fa1
        
    def get_fa2(self):
        return self.__fa2
