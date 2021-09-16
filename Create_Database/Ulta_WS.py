
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import threading

class Ulta:
  
    def __init__(self, url, new_url=None):
        self.url = url
        self.new_url = new_url
        #self.file = None

    #filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]filename_skintype = ["dry_skin.csv", "normal.csv", "combination.csv", "oily.csv", "sensitive.csv"]
    def _soup_page(self):
        uClient = uReq(self.new_url)
        page_html = uClient.read()
        uClient.close()
        return soup(page_html, "html.parser")
    
    #looping through the pages
    def pages(self, product_type, skin_type, constant):
        page = 0
        while page <= 1:
            try:
                self.new_url = f'''{self.url}&No={constant*page}&Nrpp=96'''
                self.info(product_type, skin_type)
                page += 1
            except:
                break
        
    def containers(self):
        page_soup = self._soup_page()
        return page_soup.findAll("div", {"class": "productQvContainer"})

    def _product_id(self, prod_container):
        return prod_container["id"]

    def _info_brand(self, prod_container):
        title = prod_container.find("div", "prod-title-desc")
        #get rid of the 'n\t\t\t\t' in the string
        return title.a.text.replace('\n\t\t\t\t','')
    
    def _info_prod_name(self, prod_container):
        title = prod_container.find("div", "prod-title-desc")
        prod_name_temp = title.p.a.text.replace('\n\t\t\t\t','')
        return prod_name_temp.replace(",", "|")         

# scrape out link to product
    def _prod_link(self, prod_container):
        link = prod_container.find("div", "quick-view-prod")
        return f"ulta.com{link.a['href']}"

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

    def info(self, product_type, skin_type):
        f = open(skin_type, "w")
        for container in self.containers():
            brand = self._info_brand(container)
            prod_name = self._info_prod_name(container)
            rating = self._info_rating(container)
            price = self._info_price(container)
            prod_id = self._product_id(container)
            link = self._prod_link(container)

            #not going to store it in a variable.  Took too long to run
            ''' 
            brand.append(self._info_brand(container))
            prod_name.append(self._info_prod_name(container))
            rating.append(self._info_rating(container))
            price.append(self._info_price(container))
            prod_id.append(self._product_id(container))
            link.append(self._prod_link(container))'''

        #return brand, prod_name, rating, price, prod_id, link 
            #file.write(f'''{product_id},{brand},{prod_name},{rating},{price},{link},{product_type},{skin_type}\n''')
            f.write(product_id + "," + brand + "," + prod_name + "," + rating + "," + price + "," + link+"\n")
        f.close()





