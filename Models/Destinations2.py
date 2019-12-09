class Destinations2:

    def __init__(self,id, destination):
        self.id = id
        self.destination = destination

    def get_id(self):
        return self.id

    def get_destination(self):
        return self.destination

    def __str__(self):
        return ("{:<15}{:<15}".format(self.id,self.destination))