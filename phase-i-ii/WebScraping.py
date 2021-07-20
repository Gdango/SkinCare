from Ulta_WS import Parse
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading

def Ulta_info():
    url_base = "https://www.ulta.com/skin-care-moisturizers?N=2796"
    url_parts = {"url_dry": "Z1z13p3o", "url_normal": "Z1z13p3l", "url_combination": "Z1z13p3l", "url_oily": "Z1z13p3j", "url_sensitive": "Z1z13p3m"}
    constant = 96

    url = url_base + url_parts["url_dry"]
    P = Parse(url)
    print(P.info())

    
Ulta_info()
