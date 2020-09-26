import requests
from bs4 import BeautifulSoup

# webpage to be scraped
URL = 'https://www.ebgames.ca/PS5/Games/877523/playstation-5-digital-edition#'
# set headers as if we are a browser
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

# fetches the webpage
page = requests.get(URL, headers=headers)
# parses the webpage in order to be able to fetch individual items
soup = BeautifulSoup(page.content, 'html.parser')