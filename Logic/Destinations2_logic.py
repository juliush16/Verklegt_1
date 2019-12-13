from Data.Destinations2Data import Destinations2Data
from Models.Destinations2 import Destinations2

class Destinations2Logic:
    destinations = []
    def all_destinations(self):
        all_destinations = Destinations2Data().get_destinations()
        return all_destinations

    def find_destination(self,dest_id):
        all_destinations = Destinations2Data().get_destinations()
        for destination in all_destinations:
            if destination.id == dest_id:
                return str(destination.get_destination())

    def find_destination_id(self,destination):
        all_destinations = Destinations2Data().get_destinations()
        for line in all_destinations:
            if line.destination == destination:
                return line.get_id()



