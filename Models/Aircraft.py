class Aircraft:
    def __init__(self,planeInsignia,planeTypeId):
        self.__planeInsignia = planeInsignia
        self.__planeTypeId = planeTypeId 

    def __str__(self):
        return ("{:<15}{:<15}".format(self.__planeInsignia,self.__planeTypeId))

    def get_planInsignia(self):
        return self.__planeInsignia
    
    def get_planeTypeId(self):
        return self.__planeTypeId



if __name__ == "__main__":
    d = Aircraft('Dagur','TF-943')
    print(d)