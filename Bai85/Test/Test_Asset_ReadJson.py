from Baitap.Bai85.Libs.JsonFileFactory import JsonFileFactory
from Baitap.Bai85.Models.Asset import Asset


jff = JsonFileFactory()
filename = "../DataSet/assets.json"
assets = jff.read_data(filename,Asset)
print("danh sach Employee sau khi doc file")
for a in assets:
    print(a)