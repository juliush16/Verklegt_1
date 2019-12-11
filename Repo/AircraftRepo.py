from Models.Aircraft import Aircraft
import csv

class AirCraftRepo:

    def __init__(self):
        self.__aircraft = []

    def add_aircraft_type(self, aircraftype):
        with open("./data/Aircraft.csv", "a+") as aircraft_file:
            plane_insignia = Aircraft.get_planInsignia()
            plane_type_id = Aircraft.get_planeTypeId()
            aircraft_type_file.write("{},{},\n".format(plane_insignia,plane_type_id))

    def get_aircrafts(self):
        if self.__aircraft == []:
            with open("./Data/Aircraft.csv", "r", encoding = "utf-8") as aircraft_type_file:
                aircraft_type_reader = csv.reader(aircraft_type_file)
                for line in aircraft_type_reader:
                    plane_insignia = line[0]
                    plane_type_id = line[1]
                    new_aircraft = Aircraft(plane_insignia,plane_type_id)
                    self.__aircraft.append(new_aircraft)
        return self.__aircraft
