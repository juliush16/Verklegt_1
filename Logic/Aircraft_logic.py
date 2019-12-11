from Data.AircraftData import AirCraftData

class AircraftLog:

    def __init__(self):
        self.aircraft_list = []

    def get_all_airplanes(self):
        all_airplanes = AirCraftData().get_aircrafts() 
        return all_airplanes
