
from Models.employee import Employee
import csv

class EmployeeRepo:

    def __init__(self):
        self.__employee_list = []

    def add_employee(self, employee, not_in_delete = True):
        if not_in_delete == True:
            self.__employee_list.append(employee)

        with open("./data/Employee.csv", "a+") as employee_file:
            pass
            

