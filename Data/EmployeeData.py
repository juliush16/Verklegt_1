
from Models.employee import Employee
from Data.inputCheck import InputCheck
import os
import csv
clear = lambda: os.system('cls')

class EmployeeData:

    def __init__(self):
        pass

    def add_employee(self, employee):
        with open("./Repo/Employee.csv", "a") as employee_file:
            ssn = employee.get_ssn_str()
            name = employee.get_name_str()
            role = employee.get_role()
            rank = employee.get_rank()
            licence = employee.get_licence()
            address =  employee.get_address()
            phonenumber = employee.get_phonenumber()
            email = employee.get_email()
            employee_file.write("{},{},{},{},{},{},{},{}\n".format(ssn,name,
            role,rank,licence,address,phonenumber,email))

    def get_employee(self):
        emps = []
        with open("./Repo/Employee.csv", "r", encoding = "utf-8", newline="") as employee_file:
            employee_reader = csv.reader(employee_file)
            for line in employee_reader:
                ssn = line[0]
                name = line[1]
                role = line[2]
                rank = line[3]
                licence = line[4]
                address = line[5]
                phonenumber = line[6]
                email = line[7].strip()
                new_employee = Employee(ssn, name, role, rank,licence,
                address, phonenumber, email)
                emps.append(new_employee)
        return emps
    
    def update_employee(self, updatedEmp):
        allEmps = self.get_employee()
        with open("./Repo/Employee.csv", "w+", newline="") as employee_file:
            fieldnames = ["ssn","name","role","rank","licence","address","phonenumber","email"]
            writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
            writer.writeheader()
        for emp in allEmps:
            if emp.ssn == updatedEmp.ssn:
                self.add_employee(updatedEmp)
            else:
                self.add_employee(emp)