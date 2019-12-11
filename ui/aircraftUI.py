from Logic.Aircraft_logic import AircraftLog

class Aircraft_UI:

    def print_all_airplanes(self):
        all_airplanes = AircraftLog().get_all_airplanes()
        for airplane in all_airplanes:
            print(airplane)