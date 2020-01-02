from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.ulta.com/skin-care-moisturizers?N=2796"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
prod_container = page_soup.findAll("div", {"class": "productQvContainer"})

