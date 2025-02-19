from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Employees import Employee


employees= []
employees.append(Employee("a1","Teo","teo","123"))
employees.append(Employee("a2","Minh","minh","123"))
employees.append(Employee("a3","Huy","huy","123"))
employees.append(Employee("a4","Phuc","phuc","123"))
employees.append(Employee("a5","Bao","bao","123"))


for e in employees:
    print(e)
jff = JsonFileFactory()
filename = "../DataSet/employees.json"
jff.write_data(employees,filename)