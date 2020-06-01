import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


brands = []
rq = requests.get(alba_url)
soup = BeautifulSoup(rq.text, "html.parser")
super_brands = soup.find("div", {"id": "MainSuperBrand"}).find(
    "ul", {"class": "goodsBox"}).find_all("a", {"class": "goodsBox-info"})

# scrapping brand name and link
for sb in super_brands:
    brands.append(
        {"b_name": sb.find("span", {"class": "company"}).get_text(),
         "b_link": sb.get("href")
         }
    )

# detail info scrapping and save files
for brand in brands:
    url = brand.get('b_link')
    file = open(brand.get('b_name')+".csv", mode="w",
                encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerow(["local", "title", "data", "pay", "last"])

    rq = requests.get(url)
    soup = BeautifulSoup(rq.text, "html.parser")
    t_body = soup.find("tbody").find_all("tr", {"class": ""})

    for tb in t_body:
        writer.writerow(
            [tb.find("td", {"class": "local"}).get_text(),
             tb.find("td", {"class": "title"}).get_text(),
             tb.find("td", {"class": "data"}).get_text(),
             tb.find("td", {"class": "pay"}).get_text(),
             tb.find("td", {"class": "last"}).get_text()]
        )
