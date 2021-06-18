#!/usr/bin/python3

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def is_good_response(resp):
    """
   Returns True if the response seems to be HTML, False otherwise.
   """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def simple_get(url):
    """
   Attempts to get the content at `url` by making an HTTP GET request.
   If the content-type of response is some kind of HTML/XML, return the
   text content, otherwise return None.
   """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def get_games():
    """
   Newegg page with the list of PS5 games
   """
    url = 'https://www.newegg.com/PS5-Video-Games/SubCategory/ID-3763?cm_sp=Cat_PlayStation_2-_-VisNav-_-Games'
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        games = set()
        for gamesli in html.select('div', class_="item-title"):
            for game_name in gamesli.text.split('\n'):
                # check if there's at least 1 character in name, otherwise it's an empty string
                # check if any integers in string- most likely not a name
                # then not including any strings that are likely sentences and not names
                # because they're longer than 4 words
                if len(game_name) > 1 and any(char.isdigit() for char in game_name) == False and len(
                        game_name.split(' ')) < 6:
                    games.add(game_name.strip())
        return list(games)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def main():
    print(get_games())


if __name__ == "__main__":
    main()

