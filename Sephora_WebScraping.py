from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.ulta.com/skin-care-moisturizers?N=2796"


uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
prod_containers = page_soup.findAll("div", {"class": "productQvContainer"})
filename = "Moisturizers_All.csv"
headers = "brand,product_name,rating,amount \n"

f = open(filename, "w")
f.write(headers)
i = 0
for prod_container in prod_containers:
    title = prod_container.find("div", "prod-title-desc")
    #get rid of the 'n\t\t\t\t' in the string
    brand = title.a.text.replace('\n\t\t\t\t','')
    prod_name = title.p.a.text.replace('\n\t\t\t\t','')
    #grab the section for price
    i +=1
    print(i)
    price_class = prod_container.find("p", "price")
    price = price_class.div.span.text.replace('\r\n\t\t\t\t\t\t','')

    #use try and except statement since some do not have a rating
    try:
        # finding the rating
        rating_div = prod_container.find("div", "rating") 
        rating = rating_div.div.span["class"] 
        #returns the second item on the list since that's the rating
        rating = rating[1] 
    except:
        rating = None
    
    #write the data set into the cvs file
    f.write(brand + "," + prod_name + "," + rating + "," + price + "\n")

f.close()



