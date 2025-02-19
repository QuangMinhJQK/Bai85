class Employee:
    def __init__(self, Employeeid = None,Employeename = None,UserName = None,Password =None):
        self.Employeeid =Employeeid
        self.Employeename = Employeename
        self.UserName = UserName
        self.Password = Password
    def __str__(self):
        return f"{self.Employeeid}\t{self.Employeename}\t{self.UserName}\t{self.Password}"