#flightNumber,departingFrom,arrivingAt,departure,arrival 
class Upcomingflights:
    def __init__(self,flight_number,departing_from,arriving_at,departure,arrival):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival

    def __str__(self):
        return ("{}{}{}{}{}".format(self.__flight_number,self.__departing_from,self.__arriving_at,self.__departure,self.__arrival))


    def get_flightNumber(self):
        return self.__flight_number
    
    def get_departingFrom(self):
        return self.__departing_from

    def get_arrivingAt(self):
        return self.__arriving_at

    def get_departure(self):
        return self.__departure
    
    def get_arrival(self):
        return self.__arrival

