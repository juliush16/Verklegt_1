from Data.UpcomingVoyageData import VoyageData
from Logic.Destinations_logic import DestinationsLogic
from Logic.Destinations2_logic import Destinations2Logic
from Logic.Employee_logic import EmployeeLogic
from Models.Upcomingflights import Upcomingflights
import datetime
import dateutil.parser
import random
import csv

class UpcomingVoyageLogic:

    def all_upcoming_voyage(self):
        all_voyage = VoyageData().get_voyage()
        return all_voyage
    
    def all_other_upcoming_voyage(self):
        all_voyage = VoyageData().other

    def get_from_kef(self):
        all_voyage = self.all_upcoming_voyage()
        flightsFromKefOnly = []
        for i in range(0, len(all_voyage)):
            if i % 2 == 1:
                flightsFromKefOnly.append(all_voyage[i])
        return flightsFromKefOnly

    def get_not_working(self,date):
        staff_list = []
        all_employee = EmployeeLogic().all_employees()
        working_employees = self.get_staff_by_date(date)
        for employee in all_employee:
            if employee.ssn in working_employees:
                pass
            else:
                staff_list.append(employee)

        return staff_list

    def get_staff_by_date(self,date):
        staff_list = []
        all_voyage = self.get_from_kef()
        for voyage in all_voyage[1:]:
            d = voyage.departure.replace("T", "-").replace(":", "-").split("-")
            voyage_date_dept = datetime(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]))
            if voyage_date_dept.date() == date.date():
                
                if voyage.captain != "":
                    staff_list.append(voyage.captain)
                if voyage.copilot != "":
                    staff_list.append(voyage.copilot)
                if voyage.fsm != "":
                    staff_list.append(voyage.fsm)
                if voyage.fa1 != "":
                    staff_list.append(voyage.fa1)
                if voyage.fa2 != "":
                    staff_list.append(voyage.fa2)
        return staff_list



    def generate_flight_number(self):
        return_str = 'NA'
        number = random.randint(1000,9999)
        return_str += str(number)
        return return_str

    def get_arrival_time(self,destination_id, departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        destination = Destinations2Logic().find_destination(destination_id.upper())
        flight_time = DestinationsLogic()._get_flight_time(destination)
        hour += flight_time
        if hour >= 23:
            day += 1
            hour -= 23
        new_time = datetime.datetime(year,month,day,hour,minutes).isoformat()
        return new_time

    def get_departure_time_back(self,departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        new_time = datetime.datetime(year,month,day,hour + 1,minutes).isoformat()
        return new_time

    def get_voyage_time(self,destination_id,departure):
        parsed_date = dateutil.parser.parse(departure)
        year = int(parsed_date.year)
        month = int(parsed_date.month)
        day = int(parsed_date.day)
        hour = int(parsed_date.hour)
        minutes = int(parsed_date.minute)
        destination = Destinations2Logic().find_destination(destination_id)
        voyage_time = int(DestinationsLogic()._get_voyage_time(destination))
        hour += voyage_time
        if hour >= 23:
            day += 1
            hour -= 23
        new_time = datetime.datetime(year,month,day,hour,minutes).isoformat()
        return new_time

    def make_new_flight(self, arriving_at, departure, arrival,departing_from = 'KEF'):
        flight_num = self.generate_flight_number()  #bua til flugnumer
        flight_num_back = self.generate_flight_number() #bua til flugnumer
        arrival_time_back = self.get_voyage_time(arriving_at,departure)   #Nær í tíma sem að flug kemur til baka
        new_flight = Upcomingflights(flight_num,departing_from,arriving_at,departure,arrival) #bua til flug út
        flight_back = Upcomingflights(flight_num_back,arriving_at,'KEF',self.get_departure_time_back(arrival),self.get_voyage_time(arriving_at,departure))  #bua til flug til baka
        VoyageData().add_voyage(new_flight)
        VoyageData().add_voyage(flight_back)

    def get_by_voyage(self, flight_number):#sækja flight_number
        allvoyage = self.all_upcoming_voyage()
        for voyage in allvoyage:
            if voyage.flight_number == flight_number.flight_number:
                return voyage
        return None

    def update_voyage(self, updatedvoyage):  
        VoyageData()._update_voyage(updatedvoyage)

    # def get_next_flight(self, flight_number):
    #     all_voyage = VoyageData().get_voyage()
    #     with open("./Repo/UpcomingFlights2.csv", "r", newline="") as employee_file:
    #         line = Upcomingflights('ekkert','ekkert','ekkert','ekkert','ekkert')
    #     for voy in all_voyage:
    #         if voy.flight_number == flight_number:
    #             line = next(voy)
    #             flight_number = line[0]
    #             departing_from = line[1]
    #             arriving_at = line[2]
    #             departure = line[3]
    #             arrival = line[4]
    #             try:
    #                 airplane = line[5]
    #             except:
    #                 airplane = None
    #             try:
    #                 captain = line[6]
    #             except:
    #                 captain = None
    #             try:
    #                 copilot = line[7]
    #             except:
    #                 copilot = None
    #             try:
    #                 fsm = line[8]
    #             except:
    #                 fsm = None 
    #             try:
    #                 fa1 = line[8]
    #             except:
    #                 fa1 = None
    #             new_voyage = Upcomingflights(flight_number, departing_from, arriving_at,
    #             departure, arrival)
                
    #     new_voyage = Upcomingflights(line.flight_number, line.departing_from, line.arriving_at,
    #     line.departure, line.arrival)

    #     return new_voyage
            

