class Employee:

    def __init__(self,SSN, name, role,rank,licence = None):
        self.ssn = SSN
        self.name = name
        self.role = role
        self.rank = rank
        self.licence = licence


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




if __name__ == "__main__":
    Julius = Employee('030196-2449','Julius','Pilot','Captain','NAFokkerF100')

    print(Julius.get_name_str())
    print(Julius.get_ssn_str())