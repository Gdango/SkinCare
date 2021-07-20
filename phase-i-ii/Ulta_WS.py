from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading

class Parse:
  
    def __init__(self,url):
        self.url_base = url

    #filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]filename_skintype = ["dry_skin.csv", "normal.csv", "combination.csv", "oily.csv", "sensitive.csv"]

    def create_url(self, url_parts, url_base, constant):        
        page = 0

        for urlpart in urlparts:

            url = url_base + urlparts[urlpart]
            #headers = "brand,product_name,rating,price \n" #min_amount,max_amount \n"
            f = open(urlpart, "w")  #write in cvs file
            #f.write(headers)
            info(url)
            
            while True:
                try: 
                    url = url_base + url_parts[i] + '&No=' + str(constant*page) + '&Nrpp=96'
                    info(url)
                    page += 1
                except:
                    break
            f.close()
        return url

    def soup_result(url):
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        return page_soup
        
    
    def containers(self):
        prod_containers = self.page_soup.findAll("div", {"class": "productQvContainer"})
        return prod_containers

    def info_brand(self, prod_container):
        title = prod_container.find("div", "prod-title-desc")
        #get rid of the 'n\t\t\t\t' in the string
        self.brand = title.a.text.replace('\n\t\t\t\t','')
    
    def info_prod_name(self, prod_container):
        prod_name_temp = title.p.a.text.replace('\n\t\t\t\t','')
        self.prod_name = prod_name_temp.replace(",", "|")         


    def info_price(self, prod_container):
        price_class = prod_container.find("p", "price")
        price_dollar = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')
        price = price_dollar.replace('$','') #get red of dollar sign
        if '-' not in price:
            self.price = price + ',' + price
        else:
            self.price = price.replace('-', ',')


    def info_rating(self, prod_container):
        #use try and except statement since some do not have a rating
        try:  #some doesn't have rating so need to use try & except 
            # finding the rating
            rating_div = prod_container.find("div", "rating") 
            rating = rating_div.div.span["class"] 
            #returns the second item on the list since that's the rating
            rating = rating[1].replace('rating-','')
            self.rating = rating.replace('-', '.')
        except:
            self.rating = 0
            
            #write the data set into the cvs file

    def info(self):
        for container in self.prod_containers:
            self.brand = info_branch(container)
            self.prod_name = info_prod_name(container)
            self.rating = info_rating(container)
            self.price = info_price(container)
            f.write(self.branch + "," + self.prod_name + "," + self.rating + "," + self.price + "\n")






