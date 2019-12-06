from datetime import datetime
#Ætlaði að byrja á að gera svona input check
def check_ssn():
    entername = str(input("Enter customers SSN: "))
    while entername.isnumeric() != True or len(entername) != 10:
        print("Social security number has to be all numbers and with length 10\nPlease try again.")
        entername = str(input("Enter customers SSN: "))
    return entername