from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def info(filename, url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    prod_containers = page_soup.findAll("div", {"class": "productQvContainer"})

    for prod_container in prod_containers:
        title = prod_container.find("div", "prod-title-desc")
        #get rid of the 'n\t\t\t\t' in the string
        brand = title.a.text.replace('\n\t\t\t\t','')
        prod_name_temp = title.p.a.text.replace('\n\t\t\t\t','')
        prod_name = prod_name_temp.replace(",", "|")
        
        #grab the section for price

        price_class = prod_container.find("p", "price")
        price_dollar = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')
        price = price_dollar.replace('$','') #get red of dollar sign
        price = price.replace('-', ',')

        #use try and except statement since some do not have a rating
        try:  #some doesn't have rating so need to use try & except 
            # finding the rating
            rating_div = prod_container.find("div", "rating") 
            rating = rating_div.div.span["class"] 
            #returns the second item on the list since that's the rating
            rating = rating[1].replace('rating-','')
            rating = rating.replace('-','.') 
        except:
            rating = "Null"
        
        #write the data set into the cvs file
        f.write(brand + "," + prod_name + "," + rating + "," + price + "\n")


url_base = "https://www.ulta.com/skin-care-moisturizers?N=2796"


url_dry = "Z1z13p3o" #6 pages
url_normal = "Z1z13p3l" #6 pages
url_combination = "Z1z13p3l" #6 pages
url_oily = "Z1z13p3j" #5 pages
url_sensitive = "Z1z13p3m" #4 pages


#filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]
filename_skintype = ["dry.csv", "normal.csv", "combination.csv", "oily.csv", "sensitive.csv"]
url_parts = [url_dry] # url_normal, url_combination, url_oily, url_sensitive]

pages = 6


for i in range(0, len(url_parts)):
    url = url_base + url_parts[i]
    headers = "brand,product_name,rating,amount \n"
    f = open(filename_skintype[i], "w")  #write in cvs file
    f.write(headers)
    info(filename_skintype[i], url)
    for page in range(1, pages):
        try:
            url = url_base + url_parts[i] + '&No=' + str(96*page) + '&Nrpp=96'
            info(filename_skintype[i] + str(page+1), url)
        except:
            break
    f.close()


