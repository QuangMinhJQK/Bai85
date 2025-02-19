from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Asset import Asset

assets = []
assets.append(Asset("b1","Maychieu",2018,2000))
assets.append(Asset("b2","Chuot",2019,3000))
assets.append(Asset("b3","BanPhim",2020,4000))
assets.append(Asset("b4","Man hinh",2021,5000))
assets.append(Asset("b5","Micro",2022,6000))
print("danh sach")
for a in assets:
    print(a)
jff = JsonFileFactory()
filename = "../DataSet/assets.json"
jff.write_data(assets,filename)