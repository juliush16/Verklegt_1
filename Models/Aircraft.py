class Aircraft:
    def __init__(self,planeInsignia,planeTypeId):
        self.__planeInsignia = planeInsignia
        self.__planeTypeId = planeTypeId 

    def __str__(self):
        return ("{}".format(self.__planeInsignia))

    def get_planInsignia(self):
        return self.__planeInsignia
    
    def get_planeTypeId(self):
        return self.__planeTypeId