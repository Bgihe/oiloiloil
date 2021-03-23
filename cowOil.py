import pandas as pd
import requests
import re
import ast
from git import Repo
import os
import json

def pushJson():
    dirfile = os.path.abspath('/Users/steven/oiloiloil') # code的文件位置，我默认将其存放在根目录下
    repo = Repo(dirfile)

    g = repo.git
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    print("Successful push!")
 
# def updateStockCode():
#     res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
#     df = pd.read_html(res.text)[0]
#     df.columns = df.iloc[0]
#     df = df.iloc[1:]
#     df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)
#     df.columns = ['有價證券代號及名稱', '國際證券辨識號碼(ISIN Code)', '上市日', '市場別', '產業別', 'CFICode', '備註']
#     print(df)
#     print(df['有價證券代號及名稱'])

#     stackCodeDict = {}
#     for code in df['有價證券代號及名稱']:
#         pattern = "[0-9]"
#         stackCode = code.split('　')
#         if stackCode[0] and re.search(pattern, stackCode[0]) and len(stackCode[0]) == 4:
#             print(str(stackCode[0])+stackCode[1])
#             stackCodeDict[stackCode[0]] = stackCode[1]
#     print(stackCodeDict)
    # writeStockCodeDict(stackCodeDict)


def writeStockCodeDict(writeDict):
    with open("/Users/steven/oiloiloil/oil.json", "w+") as output:
        output.write(str(writeDict))

def updateStockCode():
    res = requests.get("https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp")
    res.encoding='big5'
    df = pd.read_html(res.text)[0]

    # print(res)
    # df.columns = df.iloc[0]
    df = df.iloc[1:]

    # df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)

    # print(df)

    # df.columns = ['有價證券代號及名稱', '國際證券辨識號碼(ISIN Code)', '上市日', '市場別', '產業別', 'CFICode', '備註']
    df.columns = ['油品供應商', '98無鉛汽油', '95無鉛汽油', '92無鉛汽油', '超(高)級柴油', '計價單位', '施行日期']

    result = df.to_json(orient="records")
    parsed = json.loads(result)
    print(json.dumps(parsed, indent=4))  

    writeStockCodeDict(json.dumps(parsed, indent=4))
    pushJson()
    # print(type(df))
    # print(df['98無鉛汽油']))
    # print(json.dumps({"name": "John", "age": 30}))
    # y = json.dumps(df
    # print(y)
    # stackCodeDict = {}
    # for code in df['有價證券代號及名稱']:
    #     pattern = "[0-9]"
    #     stackCode = code.split('　')
    #     if stackCode[0] and re.search(pattern, stackCode[0]) and len(stackCode[0]) == 4:
    #         print(str(stackCode[0])+stackCode[1])
    #         stackCodeDict[stackCode[0]] = stackCode[1]
    # print(stackCodeDict)


updateStockCode()