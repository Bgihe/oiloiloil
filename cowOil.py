import json
import os

import pandas as pd
import requests
from git import Repo


def pushJson():
    dirfile = os.path.abspath('/Users/steven/oiloiloil')  # code的文件位置，我默认将其存放在根目录下
    repo = Repo(dirfile)
    g = repo.git
    g.push()
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    print("Successful push!")
    print("N")
    print("M")
    print("P")

def writeStockCodeDict(writeDict):
    with open("/Users/steven/oiloiloil/oil.json", "w+") as output:
        output.write(str(writeDict))


def updateStockCode():
    res = requests.get("https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp")
    res.encoding = 'big5'
    df = pd.read_html(res.text)[0]
    df = df.iloc[1:]
    # df.columns = ['油品供應商', '98無鉛汽油', '95無鉛汽油', '92無鉛汽油', '超(高)級柴油', '計價單位', '施行日期']
    df.columns = ['supplier', 'octane98', 'octane95', 'octane92', 'dieselOil', 'unit', 'date']
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    print(json.dumps(parsed, indent=4))
    writeStockCodeDict(json.dumps(parsed, indent=4))


updateStockCode()
pushJson()
