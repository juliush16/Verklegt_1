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

