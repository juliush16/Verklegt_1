#flightNumber,departingFrom,arrivingAt,departure,arrival 
class Upcomingflights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival

    def __str__(self): #hafa str fall eða returna öllum function með str
        pass


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

