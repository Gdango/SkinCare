from Ulta_WS import Ulta
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def Ulta_info():
    url_bases = {"moisturizer": "https://www.ulta.com/skin-care-moisturizers?N=2796",
                "cleanser": "https://www.ulta.com/skin-care-cleansers?N=2794"}
    url_parts = {"url_dry": "Z1z13p3o", "url_normal": "Z1z13p3l", "url_combination": "Z1z13p3k", "url_oily": "Z1z13p3j", "url_sensitive": "Z1z13p3m"}
    constant = 96

    url = f"{url_bases['moisturizer']}{url_parts['url_dry']}"
    P = Ulta(url)
    data = P.info()
    '''for url_base in url_bases:
        for url_part in url_parts:
            
            page = 0
            while True:
                try:
                    url = f"{url_bases[url_base]}{url_parts[url_part]}'&No='{str(constant*page)}'&Nrpp=96'"
                    print(url)
                    P = Ulta(url)
                    data = P.info()
                    print(data)
                    page += 1
                except:
                    break

    return data'''
    return data

print(Ulta_info())