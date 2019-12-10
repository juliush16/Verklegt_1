class Destinations:
    def __init__(self,location,airport,flight_time,voyage_time,contact,phonenumber):
        self.__location = location
        self.__airport = airport
        self.__flight_time = flight_time 
        self.__voyage_time = voyage_time
        self.__contact = contact #nafn
        self.__phonenumber = phonenumber 

    
    def get_Location(self):
        return self.__location
    
    def get_Airport(self):
        return self.__airport
    
    def get_flight_time(self):
        return self.__flight_time

    def get_voyage_time(self):
        return self.__voyage_time

    def get_contact(self):
        return self.__contact

    def get_phonenumber(self):
        return self.__phonenumber

    def __str__(self): #
        return ("{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}".format
        (self.__location,self.__airport,self.__flight_time,self.__voyage_time,self.__contact,self.__phonenumber))

    def set_contact(self,contact):
        self.__contact = contact

    def set_phonenumber(self,phonenumber):
        self.__phonenumber = phonenumber