from Ulta_WS import Ulta
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def Ulta_info():
    url_base = {"moisturizer": "https://www.ulta.com/skin-care-moisturizers?N=2796",
                "cleanser": "https://www.ulta.com/skin-care-cleansers?N=2794"}
    url_parts = {"url_dry": "Z1z13p3o", "url_normal": "Z1z13p3l", "url_combination": "Z1z13p3k", "url_oily": "Z1z13p3j", "url_sensitive": "Z1z13p3m"}
    constant = 96
    url = f"{url_base["moisturizer"]}{url_parts["url_dry"]}
    U = Ulta(url_parts, url_base, constant)
    P = U.containers(url)
    
    return P[0]

print(Ulta_info())