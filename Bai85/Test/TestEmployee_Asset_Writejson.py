from Baitap.Bai85.Libs.DataConnector import DataConnector
from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Employee_Asset import Employee_Asset

eas = []
eas.append(Employee_Asset("a1","b1","Main"))
eas.append(Employee_Asset("a2","b2","Main"))
eas.append(Employee_Asset("a3","b3","Main"))
eas.append(Employee_Asset("a4","b4","Main"))
eas.append(Employee_Asset("a5","b5","Main"))
for ea in eas:
    print(ea)
jff = JsonFileFactory()
filename = "../DataSet/employees_assets.json"
jff.write_data(eas,filename)

