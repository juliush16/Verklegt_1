from Data.AircraftTypeData import AirCraftTypeData
    

class AircraftTypeLogic:

    def __init__(self):
        self.aircraft_type_list = []


    def list_aircraft_types(self):
        return_list = self.get_aircraft()
        return return_list