"""
Web Crawler to gather Trulia real estate data
"""

import requests
from bs4 import BeautifulSoup

#r = requests.get("https://www.trulia.com/NJ/Moorestown/")
#c = r.content
#
#soup = BeautifulSoup(c, "html.parser")
#
#all = soup.find_all("div", {"class": "cardContainer"})
#
#all[0].find("span", {"class":"cardPrice"}).text.replace("+","") # Price
#all[0].find("li", {"data-auto-test":"beds"}).text.replace('bd',"") # Number of beds
#all[0].find("li", {"data-auto-test":"baths"}).text.replace('ba',"") # Number of baths
#all[0].find("li", {"data-auto-test":"sqft"}).text.replace(' sqft',"") # Square footage
#all[0].find("div", {"class":"mvn"}).text # Address
#all[0].find("div", {"class":"typeTruncate typeLowlight"}).text # Town, State

l = []
# for the url: https://www.trulia.com/(2 Letter State Abbvr.)/(Town_Name)
# Ex. https://www.trulia.com/NJ/Mount_Holly/
base_url = "https://www.trulia.com/NJ/Mount_Laurel/"
for page in range(0,30,10):
    r = requests.get(base_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "cardContainer"})
    for item in all:
        d = {}
        try:
            d["Address"] = (item.find("div", {"class":"mvn"}).text)
            d["Town, State"] = (item.find("div", {"class":"typeTruncate typeLowlight"}).text)
            d["Price"] = (item.find("span", {"class":"cardPrice"}).text.replace("+",""))
            d["Beds"] = (item.find("li", {"data-auto-test":"beds"}).text.replace('bd',""))
            d["Sqft"] = (item.find("li", {"data-auto-test":"sqft"}).text.replace(' sqft',""))
            d["Baths"] = (item.find("li", {"data-auto-test":"baths"}).text.replace('ba',""))
        except:
            pass
        l.append(d)
        
import pandas as pd
df = pd.DataFrame(l)
df
df.to_csv("trulia_moorestown_nj.csv")