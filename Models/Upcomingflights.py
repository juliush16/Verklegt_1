#flightNumber,departingFrom,arrivingAt,departure,arrival 
class Upcomingflights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival, airplane, ):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival
        self.airplane = airplane
        #

    

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

    def __str__(self):
        return ("{:<15}{:<15}{:<15}{:<25}{:<25}".format(self.__flight_number,self.__departing_from,self.__arriving_at,self.__departure,self.__arrival))

