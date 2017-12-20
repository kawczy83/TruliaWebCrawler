"""
Web Scraper to gather Trulia real estate data
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

state = input("Enter a 2 letter state abbreivation.")
town = input("Enter a town name.")
town = town.replace(" ", "_")

l = []
base_url = "https://www.trulia.com/" + state + "/" + town + "/"
for page in range(0,1):
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
        
# Used to convert data into a csv file
import pandas as pd
import os 
df = pd.DataFrame(l)
#df.to_csv("trulia_Moorestown_NJ.csv")
convert = "trulia_" + town + "_" + state + ".csv"
df.to_csv(convert)
print("Saved to " + os.getcwd() + " as " + convert)
