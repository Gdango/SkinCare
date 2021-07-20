import Ulta_WS
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading

def Ulta_info():
    url_base = "https://www.ulta.com/skin-care-moisturizers?N=2796"
    url_parts = {"url_dry": "Z1z13p3o", "url_normal": "Z1z13p3l", "url_combination": "Z1z13p3l", "url_oily": "Z1z13p3j", "url_sensitive": "Z1z13p3m"}
    constant = 96

    url = url_base + url_parts["url_dry"]

    print(type(Ulta_WS.Parse.soup_result(url)))
    page_soup = Ulta_WS.Parse.soup_result(url)
    print(type(page_soup.findAll("div", {"class": "productQvContainer"})))

    
Ulta_info()
