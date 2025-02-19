from Baitap.Bai85.Libs.DataConnector import DataConnector


dc = DataConnector()
employees = dc.get_all_employees()
print("danh sach nhan vien")
for e in employees:
    print(e)
assets = dc.get_all_assets()
print("danh sach san pham")
for a in assets:
    print(a)
eas = dc.get_all_employees_asset()
print("danh sach phan cong quan li tai san ")
for ea in eas:
    print(ea)
uid= str(input())
pwd= str(input())
emp=dc.login(uid,pwd)
if emp!=None:
    print("Đăng nhập thành công")
else:
    print("Đăng nhập thất bại")


