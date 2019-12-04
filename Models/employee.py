class Employee:

    def __init__(self,SSN, name, role,rank,licence = None, adress = None, phonenumber = None, email = None):
        self.ssn = SSN
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.adress = adress
        self.phonenumber = phonenumber
        self.email = email


    def get_ssn_str(self):
        return str(self.ssn)

    def get_name_str(self):
        return str(self.name)

    def get_role(self):
        return str(self.role)

    def get_rank(self):
        return str(self.rank)

    def get_licence(self):
        return str(self.licence)
    
    def get_adress(self):
        return str(self.adress)
    
    def get_phonenumber(self):
        return str(self.phonenumber)

    def get_email(self):
        return str(self.email)

    def __str__(self):
        return ("{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}".format(self.ssn,self.name,self.role,self.rank,self.licence,self.adress,self.phonenumber,self.email))

if __name__ == "__main__":
    Julius = Employee('030196-2449','Julius','Pilot','Captain','NAFokkerF100','Skólagata 1', '777-0000','julius@nan.is')

    print(Julius.get_name_str())
    print(Julius.get_ssn_str())