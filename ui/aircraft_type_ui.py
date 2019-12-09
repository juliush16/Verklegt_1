from Logic.Aircraft_type_logic import AircraftTypeLogic


class AircraftTypeUI:

    def print_aircraft_type(self):
        for i in range(len(self.__aircraft)):
            print(self.__aircraft[i])