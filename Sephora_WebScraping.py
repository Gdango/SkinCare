from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.ulta.com/skin-care-moisturizers?N=2796"


uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
prod_containers = page_soup.findAll("div", {"class": "productQvContainer"})
filename = "Moisturizers_All.csv"
headers = "product_name,rating,amount \n"

f = open(filename, "w")
f.write(headers)

for prod_container in prod_containers:
    
    product_name = prod_container.a.img['alt'] # scraping the title
    rating_div = prod_container.find("div", "rating") # finding the rating

    rating = rating_div.div.span["class"] 
    rating = rating[1] #returns the second item on the list since that's the rating


    #write the data set into the cvs file
    f.write(product_name + "," + rating + "\n")

f.close()




