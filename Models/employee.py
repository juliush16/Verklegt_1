class Employee:

    def __init__(self,ssn, name, role,rank,licence = None, adress = None, phonenumber = None, email = None):
        self.ssn = ssn
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
        return ("{:<15}{:<20}{:<15}{:<30}{:<20}{:<15}{:<15}{:<15}".format
        (self.ssn,self.name,self.role,self.rank,self.licence,self.adress,self.phonenumber,self.email))


#Set föll til að updatea starfsmann:

    def set_role(self,role):
        self.__role = role

    def set_rank(self,rank):
        self.__rank = rank

    def set_licence(self, licence):
        self.__licence = licence

    def set_adress(self, adress):
        self.__adress = adress

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def set_email(self, email):
        self.__email = email


if __name__ == "__main__":
    Julius = Employee('030196-2449','Julius','Pilot','Captain','NAFokkerF100','Skólagata 1', '777-0000','julius@nan.is')

    print(Julius.get_name_str())
    print(Julius.get_ssn_str())