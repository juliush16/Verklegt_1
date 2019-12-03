class Destinations:
    def __init__(self,Location,Airport,flight_time,voyage_time,contact,phonenumber):
        self.__Location = Location
        self.__Airport = Airport
        self.__flight_time = flight_time 
        self.__voyage_time = voyage_time
        self.__contact = contact #nafn
        self.__phonenumber = phonenumber 

    def __str__(self): #
        pass

    def get_Location(self):
        return self.__Location
    
    def get_Airport(self):
        return self.__Airport
    
    def get_flight_time(self):
        return self.__flight_time

    def get_voyage_time(self):
        return self.__voyage_time

    def get_contact(self):
        return self.__contact

    def get_phonenumber(self):
        return self.__phonenumber

