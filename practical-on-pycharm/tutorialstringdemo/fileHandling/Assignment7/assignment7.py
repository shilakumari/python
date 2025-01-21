import json
import  csv
import re

product_in_json=0
total_price=0
with open("products.json", "r") as f:
    datas = json.load(f)
    for data in datas:
        product_in_json += 1
        total_price += data["Price"]
average_price_json=total_price/product_in_json
print("Total products in JSON:",product_in_json)
print("Average price in JSON:",round(average_price_json, 2))

l=[]
product_in_csv=0
total_price_csv=0
with open("products.csv","r") as f:
    reader = csv.reader(f)
    for line in reader:
        l.append(line)

for i in range(1,len(l)):
    #print(l[i][1])
    total_price_csv += int(l[i][1])
    product_in_csv += 1
average_price_csv=total_price_csv/product_in_csv
print("Total products in CSV:",product_in_csv)
print("Average price in CSV:",round(average_price_json,2))