
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading

class Ulta:
  
    def __init__(self, url_parts, url_base, constant):
        self.url_parts = url_parts
        self.url_base = url_base
        self.constant = constant
        self.file = None

    #filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]filename_skintype = ["dry_skin.csv", "normal.csv", "combination.csv", "oily.csv", "sensitive.csv"]
    def _soup_page(self, url):
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        return soup(page_html, "html.parser")

    def Parse(self):      
        page = 0

        for urlpart in self.url_parts:
            url = f"{self.url_base}{self.url_parts[urlpart]}"
            #headers = "brand,product_name,rating,price \n" #min_amount,max_amount \n"
            self.file = open(urlpart, "w")  #write in cvs file
            #f.write(headers)
            self.info(url)
            
            while True:
                try: 
                    url = f"{url_base}{urlpart}'&No='{str(constant*page)}'&Nrpp=96'"
                    self.info(url)
                    page += 1
                except:
                    break
            self.file.close()
        
    def containers(self, url):
        page_soup = self._soup_page(url)
        return page_soup.findAll("div", {"class": "productQvContainer"})

    def _info_brand(self, prod_container):
        title = prod_container.find("div", "prod-title-desc")
        #get rid of the 'n\t\t\t\t' in the string
        return title.a.text.replace('\n\t\t\t\t','')
    
    def _info_prod_name(self, prod_container):
        title = prod_container.find("div", "prod-title-desc")
        prod_name_temp = title.p.a.text.replace('\n\t\t\t\t','')
        return prod_name_temp.replace(",", "|")         


    def _info_price(self, prod_container):
        price_class = prod_container.find("p", "price")
        price_dollar = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')
        price = price_dollar.replace('$','') #get red of dollar sign
        if '-' not in price:
            return price + ',' + price
        else:
            return price.replace('-', ',')


    def _info_rating(self, prod_container):
        #use try and except statement since some do not have a rating
        try:  #some doesn't have rating so need to use try & except 
            # finding the rating
            rating_div = prod_container.find("div", "rating") 
            rating = rating_div.div.span["class"] 
            #returns the second item on the list since that's the rating
            rating = rating[1].replace('rating-','')
            return rating.replace('-', '.')
        except:
            return 0
            
            #write the data set into the cvs file

    def info(self, url):
        for container in self.containers(url):
            brand = self._info_brand(container)
            prod_name = self._info_prod_name(container)
            rating = self._info_rating(container)
            price = self._info_price(container)
            self.file.write(brand + "," + prod_name + "," + rating + "," + price + "\n")






