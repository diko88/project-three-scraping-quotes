# Use the BeautifulSoup and requests Python packages to print out a list of all the quotes in http://quotes.toscrape.com/tag/humor/

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://quotes.toscrape.com/tag/humor/'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each quote
containers = page_soup.findAll("span", {"class": "text"})

for element in containers:
    print(element.contents)
