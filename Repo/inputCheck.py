from datetime import datetime
#Ætlaði að byrja á að gera svona input check

def check_ssn():
    new_emp_SSN = input('Enter employee social security number :')
    while new_emp_SSN.isdigit() != True or len(new_emp_SSN) != 10:
        print('Invalid employee social security number Try again!')
        new_emp_SSN = input('Enter employee social security number: ')
    return new_emp_SSN

def check_phonenumber():
    new_emp_phonenumber = input('Enter employee phone number :')
    while new_emp_phonenumber.isdigit() != True or len(new_emp_phonenumber) != 7:
        print('Invalid employee phone number Try again!')
        new_emp_phonenumber = input('Enter employee phone number :')
    return new_emp_phonenumber
    
def check_role():
    new_emp_role = ""
    while new_emp_role != '1' or '2':
        new_emp_role = input('Choose an option for employee role\n1:Pilot\n2:Cabincrew\n')
        if new_emp_role == '1':
            new_emp_role = "Pilot"
            break
        elif new_emp_role == '2': #cabincrew 
            new_emp_role = "Cabincrew"
            break
        print("Invalid employee role try again!")
    return new_emp_role

def check_rank(new_emp_role):
    new_emp_rank = ""
    while new_emp_role == "Pilot" or "Cabincrew":
        if new_emp_role == "Pilot":
            new_emp_rank = input('Choose an option for employee rank\n1:Captain\n2:Copilot\n')
            if new_emp_rank == '1':
                new_emp_rank = 'Captain'
                break
            elif new_emp_rank == '2':
                new_emp_rank = "Copilot"
                break
            print("Invalid option for employee rank try again!")
        if new_emp_role == "Cabincrew":
            new_emp_rank = input('Choose an option for employee rank\n1:Flight Service Manager\n2:Flight Attendant\n')
            if new_emp_rank == '1':
                new_emp_rank = "Flight Service Manager"
                break
            elif new_emp_rank == '2':
                new_emp_rank = "Flight Attendant"
                break
            print("Invalid option for employee rank try again!")
    return new_emp_rank

def check_licence(new_emp_role):
    new_emp_licence = ""
    if new_emp_role == "Cabincrew":
        new_emp_licence = "N/A"
        return new_emp_licence
    if new_emp_role == "Pilot":
        while new_emp_licence != '1' or '2' or '3': #licence
            new_emp_licence = input('Choose an option for employee licence\n1:NABAE146\n2:NAFokkerF28\n3:NAFokkerF100\n')
            if new_emp_licence == '1':
                new_emp_licence = "NABAE146"
                break
            elif new_emp_licence == '2':
                new_emp_licence = "NAFokkerF28"
                break
            elif new_emp_licence == '3':
                new_emp_licence = "NAFokkerF100"
                break
            print("Invalid employe licence try again!")
        return new_emp_licence

def check_email():
    new_emp_email = ""
    while new_emp_email[-7:] != "@nan.is":
        new_emp_email =  input('Enter employee email :')
        if new_emp_email[-7:] == "@nan.is":
            return new_emp_email
        print("Invalid email try again!")
