from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading


class parse_html:
    def __init__(self, url):
        self.base_url = "https://www.ulta.com/skin-care-moisturizers?N=2796"


    #filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]filename_skintype = ["dry_skin.csv", "normal.csv", "combination.csv", "oily.csv", "sensitive.csv"]

    def create_url(self):
        url_dry = "Z1z13p3o" #6 pages
        url_normal = "Z1z13p3l" #6 pages
        url_combination = "Z1z13p3l" #6 pages
        url_oily = "Z1z13p3j" #5 pages
        url_sensitive = "Z1z13p3m" #4 pages
        url_parts = [url_dry, url_normal, url_combination, url_oily, url_sensitive]
        page = 0

        for i in range(0, len(url_parts)):

            url = url_base + url_parts[i]
            #headers = "brand,product_name,rating,price \n" #min_amount,max_amount \n"
            f = open(filename_skintype[i], "w")  #write in cvs file
            #f.write(headers)
            info(url)
            

            while True:
                try: 
                    url = url_base + url_parts[i] + '&No=' + str(96*page) + '&Nrpp=96'
                    info(url)
                    page += 1
                except:
                    break
            f.close()
        return url

class info(parse_html):
    def soup_result(self, url):
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        
        return page_soup
    
    def containers(self, page_soup):
        self.prod_containers = page_soup.findAll("div", {"class": "productQvContainer"})

    def info_brand(self, prod_containers):
        for prod_container in prod_containers:
            title = prod_container.find("div", "prod-title-desc")
            #get rid of the 'n\t\t\t\t' in the string
            brand = title.a.text.replace('\n\t\t\t\t','')
        return brand
    
    def info_prod_name(self, prod_containers):
        for prod_container in prod_containers:
            prod_name_temp = title.p.a.text.replace('\n\t\t\t\t','')
            prod_name = prod_name_temp.replace(",", "|")
            
        return prod_name

    def info_price(self, prod_containers):
            #grab the section for price
        for prod_container in prod_containers:
            price_class = prod_container.find("p", "price")
            price_dollar = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')
            price = price_dollar.replace('$','') #get red of dollar sign
            if '-' not in price:
                price = price + ',' + price
            else:
                price = price.replace('-', ',')
        return price

    def info_rating(self, prod_containers):
        for prod_container in prod_containers:
            #use try and except statement since some do not have a rating
            try:  #some doesn't have rating so need to use try & except 
                # finding the rating
                rating_div = prod_container.find("div", "rating") 
                rating = rating_div.div.span["class"] 
                #returns the second item on the list since that's the rating
                rating = rating[1].replace('rating-','')
                rating = rating.replace('-', '.')
            except:
                rating = 0
        return rating
            
            #write the data set into the cvs file
    f.write(brand + "," + prod_name + "," + rating + "," + price + "\n")





