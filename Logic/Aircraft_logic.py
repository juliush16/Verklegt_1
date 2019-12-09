from Repo.AircraftRepo import AirCraftRepo

class AircraftLog:

    def __init__(self):
        self.aircraft_list = []

    def get_all_airplanes(self):
        all_airplanes = AirCraftRepo().get_aircrafts()
        for airplane in all_airplanes:
            self.aircraft_list.append(airplane)
        return self.aircraft_list

    def print_all_airplanes(self):
        all_airplanes = self.get_all_airplanes()
        for airplane in all_airplanes:
            print(airplane)