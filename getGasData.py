import csv
import os
import json
import requests
import time
from git import Repo


def writeStockCodeDict(writeDict):
    with open("gasCompany.json", "w") as output:
        output.write(str(writeDict))


def pushJson():
    dirfile = os.path.abspath('')
    repo = Repo(dirfile)
    g = repo.git
    g.push()
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    print("Successful push!")


dataList = []
data = csv.reader(open('C:/Users/user/Downloads/data.csv', encoding="utf-8"))
for row in data:
    if "加油站" in row[3]:
        print(str(row[0]))

        address = str(row[0])
        rq = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyCYxLMPG2xHPaSasv9cDfx1LayaR9n35eo")
        data = rq.json()
        if data['status'] == "OK":
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']

            gasDict = {'companyName': str(row[3]),
                       'companyAddress': str(row[0]),
                       'latitude': str(lat),
                       'longitude': str(lng)}
            dataList.append(gasDict)
        time.sleep(0.5)

writeStockCodeDict(json.dumps(dataList, indent=2))
pushJson()
