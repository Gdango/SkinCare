from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.ulta.com/skin-care-moisturizers?N=2796"

url_dry = "https://www.ulta.com/skin-care-moisturizers?N=2796Z1z13p3o" #6 pages
url_normal = "https://www.ulta.com/skin-care-moisturizers?N=2796Z1z13p3l" #6 pages
url_combination = "https://www.ulta.com/skin-care-moisturizers?N=2796Z1z13p3l" #6 pages
url_oily = "https://www.ulta.com/skin-care-moisturizers?N=2796Z1z13p3j" #5 pages
url_sensitive = "https://www.ulta.com/skin-care-moisturizers?N=2796Z1z13p3m" #4 pages




#filename_concern = ["dryness", "anti_aging", "dark_spots", "tone", "redness", "oiliness", "acne", "blackhead", "finelines", "darkcircles"]
filename_skintype = ["dry", "normal", "combination", "oily", "sensitive"]
urls = [url_dry, url_normal, url_combination, url_oily, url_sensitive]

#for each url, need access to every page
url = url_dry + '&No=' + str(96*2) + '&Nrpp=96'

def info(file_name, url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    prod_containers = page_soup.findAll("div", {"class": "productQvContainer"})
    filename = file_name
    headers = "brand,product_name,rating,amount \n"
    f = open(filename, "w")
    f.write(headers)

    for prod_container in prod_containers:
        title = prod_container.find("div", "prod-title-desc")
        #get rid of the 'n\t\t\t\t' in the string
        brand = title.a.text.replace('\n\t\t\t\t','')
        prod_name = title.p.a.text.replace('\n\t\t\t\t','')
        #grab the section for price

        price_class = prod_container.find("p", "price")
        price = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')

        #use try and except statement since some do not have a rating
        try:
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
    f.close()


