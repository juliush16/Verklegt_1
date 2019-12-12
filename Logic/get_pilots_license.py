from Data.AircraftData import AirCraftData
from Logic.Employee_logic import EmployeeLogic


class PilotLicence():


    def get_all_airplanes(self):
        all_airplanes = AirCraftData().get_aircrafts() 
        return all_airplanes

    def get_pilots_wLicence(self,plane):
        pilots = EmployeeLogic().get_all_pilots()
        with_leicende = []
        for p in pilots:
            if(p.licence == plane):
                print(p)
                      #  if(str(str(up).split()[3]).strip() == new_date.strip()):