
from Models.AircraftType import Aircraftype
import csv

class AirCraftTypeData:

    def __init__(self):
        self.__aircraft = []
        self.get_aircraft() #þessi

    def add_aircraft_type(self, aircraftype,not_in_delete = True):
        if not_in_delete == True:
            self.__aircraft.append(aircraftype)
        with open("./Repo/AircraftType.csv", "a+") as aircraft_type_file:
            plane_type_id = aircraftype.get_planeTypeId()
            plane_type = aircraftype.get_plane_type()
            model = aircraftype.get_model()
            capacity = aircraftype.get_capacity()
            empty_weight = aircraftype.get_empty_weight()
            max_takeoff_weight = aircraftype.get_max_takeoff_weight()
            unit_thrust = aircraftype.get_unit_thrust()
            service_ceiling = aircraftype.get_service_ceiling()
            length = aircraftype.get_length()
            height = aircraftype.get_height()
            wingspan = aircraftype.get_wingspan()
            aircraft_type_file.write("{},{},{},{},{},{},{},{},{},{},{},\n".format(plane_type_id, 
            plane_type, model, capacity, empty_weight, max_takeoff_weight, unit_thrust, 
            service_ceiling, length, height, wingspan,))
            self.__aircraft.append(aircraftype) #þessi

    def get_aircraft(self):
        if self.__aircraft == []:
            with open("./Repo/AircraftType.csv", "r", encoding = "utf-8") as aircraft_type_file:
                aircraft_type_reader = csv.reader(aircraft_type_file)
                for line in aircraft_type_reader:
                    plane_type_id = line[0]
                    plane_type = line[1]
                    model = line[2]
                    capacity = line[3]
                    empty_weight = line[4]
                    max_takeoff_weight = line[5]
                    unit_thrust = line[6]
                    service_ceiling = line[7]
                    length = line[8]
                    height = line[9]
                    wingspan = line[10]
                    new_aircraft = Aircraftype(plane_type_id, plane_type, model,
                        capacity,empty_weight,max_takeoff_weight, unit_thrust, service_ceiling,
                        length, height, wingspan)
                    self.__aircraft.append(new_aircraft)
        return self.__aircraft
