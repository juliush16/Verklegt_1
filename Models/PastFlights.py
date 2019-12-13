class PastFlights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival,aircraft_id,captain,copilot,flight_service_manager,fa1,fa2):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure 
        self.__arrival = arrival 
        self.__aircraft_id = aircraft_id
        self.__captain = captain
        self.__copilot = copilot
        self.__flight_service_manager = flight_service_manager
        self.__fa1 = fa1
        self.__fa2 = fa2

    def __str__(self):
        return ("{:^15}{:^15}{:^10}{:^22}{:^22}{:^10}{:^14}{:^14}{:^14}{:^14}".format
        (self.__flight_number,self.__departing_from,self.__arriving_at,self.__departure,
        self.__arrival,self.__aircraft_id,self.__captain,self.__copilot,self.__flight_service_manager,self.__fa1,self.__fa2))

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
    
    def get_aircraft_id(self):
        return self.__aircraft_id
    
    def get_captain(self):
        return self.__captain
    
    def get_copilot(self):
        return self.__copilot
    
    def get_flight_service_manager(self):
        return self.__flight_service_manager
    
    def get_fa1(self):
        return self.__fa1
        
    def get_fa2(self):
        return self.__fa2
