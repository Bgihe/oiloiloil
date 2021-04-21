from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from git import Repo
import os
import json

def writeOilDict(writeDict):
    with open("/Users/steven/oiloiloil/upDown.json", "w+") as output:
        output.write(str(writeDict))

def pushJson():
    dirfile = os.path.abspath('/Users/steven/oiloiloil') # code的文件位置，我默认将其存放在根目录下
    repo = Repo(dirfile)
    g = repo.git
    g.push()
    g.add("--all")
    g.commit("-m auto update")
    g.push()
    print("Successful push!")


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.cpc.com.tw/'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.find("b", class_="rate").i.string)
print(soup.find("b", class_="sys").string)

print(soup.find("b", id ="sPrice2"))
print(soup.find("b", id ="sPrice1"))



oilDict = {}
oilDict['rate'] = float(soup.find("b", class_="rate").i.string)
oilDict['sys'] = soup.find("b", class_="sys").string
writeOilDict(json.dumps(oilDict, indent=4))

driver.close()
pushJson()
