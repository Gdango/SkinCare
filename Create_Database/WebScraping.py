from Ulta_WS import Ulta
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def Ulta_info():
    url_bases = {"moisturizer": "https://www.ulta.com/skin-care-moisturizers?N=2796",
                "cleanser": "https://www.ulta.com/skin-care-cleansers?N=2794"}
    url_parts = {"url_dry": "Z1z13p3o", "url_normal": "Z1z13p3l", "url_combination": "Z1z13p3k", "url_oily": "Z1z13p3j", "url_sensitive": "Z1z13p3m"}
    constant = 96

    url = f"{url_bases['moisturizer']}{url_parts['url_dry']}"

    # returned data in order of brand, prod_name, rating, price, prod_id, link
    P = Ulta(url)
    data = P.info()

    return data


print(Ulta_info())