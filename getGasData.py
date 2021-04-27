import csv
import os
import json
from git import Repo

data = open('C:/Users/user/Downloads/data.csv', encoding="utf-8")
rows = csv.reader(data)

def writeStockCodeDict(writeDict):
    with open("gasCompany.json", "w+") as output:
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
for row in rows:
    if "加油站" in row[3]:
        gasDict = {"companyName": str(row[3]), "companyAddress": str(row[0])}
        dataList.append(gasDict)

writeStockCodeDict(json.dumps(dataList, indent=4))
pushJson()
