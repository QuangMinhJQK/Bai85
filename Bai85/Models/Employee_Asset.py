class Employee_Asset:
    def __init__(self,Employeeid,AssetId,Role):
        self.Employeeid = Employeeid
        self.AssetId = AssetId
        self.Role = Role
    def __str__(self):
        return f"{self.Employeeid}\t{self.AssetId}\t{self.Role}"
