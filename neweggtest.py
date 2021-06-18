#!/usr/bin/env python3

from bs4 import BeautifulSoup
import lxml
import pandas
import requests,re

#webscrape prices off of newegg
r_newegg=requests.get('https://www.newegg.com/PS5-Video-Games/SubCategory/ID-3763?cm_sp=Cat_PlayStation_2-_-VisNav-_-Games&recaptcha=pass')
c_newegg=r_newegg.content

soup_newegg=BeautifulSoup(c_newegg,"html.parser")
print(soup_newegg)
newegg_price=soup_newegg.find_all("div",{"class":"item-action"})
#newegg_price[0].find("span").next_sibling.next_sibling.text ## this is the way to find the price
newegg_name=soup_newegg.find_all("a",{"class":"item-title"})
print(newegg_name.find("a").text)
print(newegg_name[0].find("a"))
newegg=[]

for price,name in zip(newegg_price,newegg_name):#don't forget to use zip to iterate through two lists
    d={}
    try:
        d["Price"]=price.find("span").next_sibling.next_sibling.text
    except:
        pass
