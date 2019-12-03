class Aircraftype:
    def __init__(self,plane_type_id,plane_type,model,capacity,empty_weight,max_takeoff_weight,unit_thrust,service_ceiling,length,height,wingspan):
        self.__plane_type_id = plane_type_id
        self.__plane_type = plane_type
        self.__model = model
        self.__capacity = capacity
        self.__empty_weight = empty_weight
        self.__max_takeoff_weight = max_takeoff_weight
        self.__unit_thrust = unit_thrust
        self.__service_ceiling = service_ceiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan
    
    def __str__(self): #hvað viljum við birta 
            return ("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(self.__plane_type_id,self.__plane_type,self.__model,self.__capacity,self.__empty_weight,self.__max_takeoff_weight,self.__unit_thrust,self.__service_ceiling,self.__length,self.__height,self.__wingspan))

    def get_plane_type_id(self):
        return self.__planeTypeId
    
    def get_plane_type(self):
        return self.__planeType

    def get_model(self):
        return self.__model
    
    def get_capacity(self):
        return self.__capacity
    
    def get_empty_weight(self):
        return self.__emptyWeight
    
    def get_max_takeoff_weight(self):
        return self.__maxTakeoffWeight
    
    def get_unit_thrust(self):
        return self.__unitThrust
    
    def get_service_ceiling(self):
        return self.__serviceCeiling
    
    def get_length(self):
        return self.__length
    
    def get_height(self):
        return self.__height

    def get_wingspan(self):
        return self.__wingspan
