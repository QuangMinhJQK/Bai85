from Baitap.Bai85.Models.Employees import Employee
from Baitap.Bai85.Models.Asset import Asset
from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Employee_Asset import Employee_Asset

class DataConnector:
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../DataSet/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def get_all_assets(self):
        jff = JsonFileFactory()
        filename = "../DataSet/assets.json"
        assets = jff.read_data(filename, Asset)
        return assets
    def get_all_employees_asset(self):
        jff = JsonFileFactory()
        filename = "../DataSet/employees_assets.json"
        eas = jff.read_data(filename, Employee_Asset)
        return eas
    def login(self,username,password):
        employees = self.get_all_employees()
        for e in employees:
            if e.UserName == username and e.Password==password:
                return e
        return None
