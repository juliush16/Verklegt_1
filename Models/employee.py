class Employee:

    def __init__(self,ssn, name, role,rank,licence, address, phonenumber, email):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence
        self.address = address
        self.phonenumber = phonenumber
        self.email = email


    def get_ssn_str(self):
        return self.ssn

    def get_name_str(self):
        return self.name

    def get_role(self):
        return self.role

    def get_rank(self):
        return self.rank

    def get_licence(self):
        return self.licence
    
    def get_address(self):
        return self.address
    
    def get_phonenumber(self):
        return self.phonenumber

    def get_email(self):
        return self.email

    def __str__(self):
        return ("{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}".format
        (self.ssn,self.name,self.role,self.rank,self.licence,self.address,self.phonenumber,self.email))


#Set föll til að updatea starfsmann:

    def set_role(self,role):
        self.role = role

    def set_rank(self,rank):
        self.rank = rank

    def set_licence(self, licence):
        self.licence = licence

    def set_address(self, address):
        self.address = address

    def set_phonenumber(self, phonenumber):
        self.phonenumber = phonenumber

    def set_email(self, email):
        self.email = email


if __name__ == "__main__":
    Julius = Employee('030196-2449','Julius','Pilot','Captain','NAFokkerF100','Skólagata 1', '777-0000','julius@nan.is')

    print(Julius.get_name_str())
    print(Julius.get_ssn_str())