from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/global/in-en/p/pl?d=graphics+card'

uclient=ureq(my_url)
page_html=uclient.read()
uclient.close()

page_soup=soup(page_html,"html.parser")


containers=page_soup.findAll("div",{"class":"item-container"})


filename = "products.csv"
f=open(filename,"w")

headers="brand,product_name\n"

f.write(headers)

for container in containers:
  	  brand=container.a.img["title"]
  	  
  	  title_container=container.findAll("a",{"class":"item-title"})
  	  product_name= title_container[0].text

  	  print("brand:" +brand)
  	  print("product_name:" +product_name)

  	  f.write(brand + "," + product_name.replace(",","|") + "\n")
f.close()