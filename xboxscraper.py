#!/usr/bin/env python3

# import modules needed with beautiful soup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests

web_results = requests.get(
    'https://www.newegg.com/p/pl?d=PPSSWHQRGMFPUQ&DEPA=0&Order=BESTMATCH&cm_sp=Cat_Xbox-_-games%2f21-1172-_-%2f%2fpromotions.newegg.com%2fgames%2f21-1172%2f1920x360.jpg&icid=631046').text

soup_results = BeautifulSoup(web_results, 'html.parser')
games_results = soup_results.find('div', class_='item-info')
game_item = games_results.find_all('div', class_="item-branding")
game_title = games_results.find_all('a', {"class":"item-title"})

print(games_results)
print(game_item)
print(game_title)
