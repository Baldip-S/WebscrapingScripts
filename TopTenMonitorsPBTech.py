from bs4 import BeautifulSoup

import requests
import os
from urllib.parse import urlparse

urls = ['https://www.pbtech.co.nz/category/peripherals/monitors/4k-monitors',
        'https://www.pbtech.co.nz/category/peripherals/monitors/business-monitors',
        'https://www.pbtech.co.nz/category/peripherals/monitors/curved-monitors',
        'https://www.pbtech.co.nz/category/peripherals/monitors/home-monitors',
        'https://www.pbtech.co.nz/category/peripherals/monitors/ultrawide-monitors',
        ]
u = -1

for url in urls:
    u += 1
    a = urlparse(url)
    htmlText = requests.get(urls[u]).text
    soup = BeautifulSoup(htmlText, 'lxml')
    productList = []
    prices = []
    products = []
    priceList = []
    n = -1

    os.chdir("C:/Users/baldi/OneDrive/Desktop")
    filename = ("top10-" + (os.path.basename(a.path)) + ".csv")
    f = open(filename, "w")
    headers = "productName, cost\n"
    f.write(headers)

    for pc in soup.findAll('span', class_='price_full'):
        price = pc.text
        priceList.append(price)

    for pd in soup.findAll('a', class_='js-product-link item_line_name'):
        product = pd.get_text().strip()
        productList.append(product)

    for i in range(10):
        n += 2
        products.append(productList[n])
        prices.append(priceList[n])

    for i in range(len(prices)):
        f.write(products[i].replace(",", "|") + "," + prices[i].replace(",", "") + "\n")

    productList.clear()
    priceList.clear()
    prices.clear()
    products.clear()

    f.close()
