
from Models.Destinations2 import Destinations2
import csv

class Destinations2Data:

    def __init__(self):
        self.__destinations = []
        self.get_destinations() #þessi
        

    def add_destination(self, destination):
        with open("./Repo/Destinations2.csv", "a+") as destinations2_file:
            destinations2_id = Destinations2.get_id()
            destinations2_destination = Destinations2.get_destination()
            destinations2_file.write("{},{},\n".format(destinations2_id,destinations2_destination))
            self.__destination.append(destination) #þessi

    def get_destinations(self):
        if self.__destinations == []:
            with open("./Repo/Destinations2.csv", "r", encoding = "utf-8") as destinations_file:
                destinations_reader = csv.reader(destinations_file)
                for line in destinations_reader:
                    id = line[0]
                    destination = line[1]
                    new_destination = Destinations2(id,destination)
                    self.__destinations.append(new_destination)
        return self.__destinations