from Repo.Destinations2Repo import Destinations2Repo

class Destinations2Logic:

    def __init__(self):
        self.destinations = []

    def all_destinations(self):
        all_destinations = Destinations2Repo().get_destinations()
        for destination in all_destinations:
            self.destinations.append(destination)
        return self.destinations

    def find_destination(self,dest_id):
        all_destinations = self.all_destinations()
        for destination in all_destinations:
            if destination.id == dest_id:
                return destination

