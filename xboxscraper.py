#!/usr/bin/python3

# import modules needed with beautiful soup
import time

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests

# URL of the newegg PS5 games
web_results = requests.get(
    'https://www.newegg.com/p/pl?d=PPSSWHQRGMFPUQ&DEPA=0&Order=BESTMATCH&cm_sp=Cat_Xbox-_-games%2f21-1172-_-%2f%2fpromotions.newegg.com%2fgames%2f21-1172%2f1920x360.jpg&icid=631046').text

# getting a list of items by html tags
def get_games():
    # Parse raw HTML data
    soup_results = BeautifulSoup(web_results, 'html.parser')
    # Data results for item info
    games_results = soup_results.find('div', class_='item-info')
    # getting results from item branding after drill down
    game_item = games_results.find('div', class_="item-branding")
    # syntax to parse htmls embbed in a tags
    game_title = game_item.find('a', href=True)["href"]
    game_price = soup_results.find('li', class_='price-current')
    game_pricespan = game_price.find('span', class_="price-current-label")

 #   game_list = game_title.readlines()

    print(games_results)
    print(game_item)
    print(game_title)
    print(game_price)
    print(game_pricespan)
#    print(game_list)

if __name__ == '__main__':
    while True:
        get_games()
        time_sleep = 10
        time.sleep(time_sleep * 10)

