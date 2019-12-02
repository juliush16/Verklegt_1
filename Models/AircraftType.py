class Aircraftype:
    def __init__(self,planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.__planeTypeId = planeTypeId
        self.__planeType = planeType
        self.__model = model
        self.__capacity = capacity
        self.__emptyWeight = emptyWeight
        self.__maxTakeoffWeight = maxTakeoffWeight
        self.__unitThrust = unitThrust
        self.__serviceCeiling = serviceCeiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan
    
    def __str__(self): #hvað viljum við birta 
            pass

    def get_planeTypeId(self):
        return self.__planeTypeId
    
    def get_planeType(self):
        return self.__planeType

    def get_model(self):
        return self.__model
    
    def get_capacity(self):
        return self.__capacity
    
    def get_emptyWeight(self):
        return self.__emptyWeight
    
    def get_maxTakeoffWeight(self):
        return self.__maxTakeoffWeight
    
    def get_unitThrust(self):
        return self.__unitThrust
    
    def get_serviceCeiling(self):
        return self.__serviceCeiling
    
    def get_length(self):
        return self.__length
    
    def get_height(self):
        return self.__height

    def get_wingspan(self):
        return self.__wingspan
