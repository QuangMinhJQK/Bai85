from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Employees import Employee


jff = JsonFileFactory()
filename = "../DataSet/employees.json"
employees = jff.read_data(filename,Employee)
print("danh sach Employee sau khi doc file")
for e in employees:
    print(e)