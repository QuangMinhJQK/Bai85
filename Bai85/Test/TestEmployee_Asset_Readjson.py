from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Employee_Asset import Employee_Asset

jff = JsonFileFactory()
filename = "../DataSet/employees_assets.json"
employees_assets = jff.read_data(filename,Employee_Asset)
print("danh sach Asset sau khi doc file")
for ea in employees_assets:
    print(ea)