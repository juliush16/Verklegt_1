from Models.AircraftType import Aircraftype
import csv

class AirCraftTypeRepo:

    def __init__(self):
        self.__aircraft = []

    def add_aircrafttype(self, aircraftype):
        with open("./data/AircraftType.csv", "a+") as aircrafttype_file:
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
            aircrafttype_file.write("{},{},{},{},{},{},{},{},{},{},{},\n".format(plane_type_id, 
            plane_type, model, capacity, empty_weight, max_takeoff_weight, unit_thrust, 
            service_ceiling, length, height, wingspan,  ))
    
