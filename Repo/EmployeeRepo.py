
from Models.employee import Employee
import csv

class EmployeeRepo:

    def __init__(self):
        self.__employee = []

    def add_employee(self, employee):

        with open("./data/Employee.csv", "a+") as employee_file:
            SSN = employee.get_SSN()
            name = employee.get_name()
            role = employee.get_role()
            rank = employee.get_rank()
            licence = employee.get_licence()
            adress =  employee.get_adress()
            phonenumber = employee.get_phonenumber()
            email = employee.get_email()
            employee_file.write("{},{},{},{},{},{},{},{},\n".format(SSN,name,
            role,rank,licence,adress,phonenumber,email))

    def get_employee(self):
        if self.__employee == []:
            with open("./Data/Employee.csv", "r", encoding = "utf-8") as employee_file:
                employee_reader = csv.reader(employee_file)
                for line in employee_reader:
                    SSN = line[0]
                    name = line[1]
                    role = line[2]
                    rank = line[3]
                    licence = line[4]
                    adress = line[5]
                    phonenumber = line[6]
                    email = line[7]
                    new_employee = Employee(SSN, name, role, rank,licence,
                    adress, phonenumber, email)
                    self.__employee.append(new_employee)
        return self.__employee

    def all_employees(self):
        all_employee_list = []
        all_employees = self.get_employee()
        for employee in all_employees:
            all_employee_list.append(Employee)
        return all_employee_list


    

            
            

