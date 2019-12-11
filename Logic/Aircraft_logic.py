from Repo.AircraftRepo import AirCraftRepo

class AircraftLog:

    def __init__(self):
        self.aircraft_list = []

    def get_all_airplanes(self):
        all_airplanes = AirCraftRepo().get_aircrafts() 
        return all_airplanes
