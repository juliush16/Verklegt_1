#flightNumber,departingFrom,arrivingAt,departure,arrival 
class Upcomingflights:
    def __init__(self,flightNumber,departingFrom,arrivingAt,departure,arrival):
        self.__flightNumber = flightNumber
        self.__departingFrom = departingFrom
        self.__arrivingAt = arrivingAt
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

