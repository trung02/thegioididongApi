
import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI
app = FastAPI()

# cnx = mysql.connector.connect(
#     user='root', 
#     password='psw123', 
#     port='3306',
#     host='127.17.0.2',
#     database='thegioididong_db'
#     )
# cursor = cnx.cursor()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
# Sử dụng User-Agent khác
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"

url = 'https://www.footlocker.com/category/mens.html'
data = []
# @app.get("/getData")
def getData():
    data = []
  
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    products = soup.find_all('li', {'class': 'product-container col'})
    for product in products:
        cate = product.div.a.find('span',class_ = 'ProductName').find('span',class_ = 'ProductName-primary').text()
        print('hello'+cate)
       # img_tag = product.find('div',{'class':'UR-z'}).figure.picture.img
        # price = product.find('div',{'class':'product-info'}).find('h3',{'class':'price-box'}).find('span',{'class':'special-price'}).find('span',{'class':'price'}).text.strip()
        
    #     if 'src' in img_tag.attrs:
    #         image = img_tag['src']
    #     else:
    #         image = img_tag['data-lazyload']
    #     print(image)
    #     data.append({'category':cate ,'image':image}) 
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)   
    # result = [(item['name'], item['price'], item['image']) for item in data]
    # add_data = (f"INSERT INTO product "
    # "(title, price,images) "
    # "VALUES (%s, %s, %s)")
    # cursor.executemany(add_data, result)
    # cnx.commit() 
    return (data)
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
    
products = soup.find_all('li', {'class': 'product-container col'})
for product in products:
    cate = product.div.a.find('span',class_ = 'ProductName').find('span',class_ = 'ProductName-primary').text()
    print('hello'+cate)

