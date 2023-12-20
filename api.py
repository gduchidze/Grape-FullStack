import requests
import sqlite3
from bs4 import BeautifulSoup

url = "https://topgeorgian.wine/product-category/thethri-ghvino/thethri-mshrali-ghvino/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

wine_items = soup.find_all('h2', class_='woocommerce-loop-product__title')

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS winess
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT 
                  )''')

for wine in wine_items:
    name = wine.get_text(strip=True)

    cursor.execute("INSERT INTO winess (name) VALUES (?)", (name,))

conn.commit()
conn.close()
#########
