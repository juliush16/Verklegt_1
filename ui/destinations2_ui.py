from Logic.Destinations2_logic import Destinations2Logic

class Destinations2UI:

    def print_all_destinations(self):
        all_destinations = Destinations2Logic().all_destinations()
        for destination in all_destinations:
            print(destination)

    