import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"
brands = []

# scrap super brands link


def get_super_brands(brands):
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
    return brands


def get_brand_detail_infomation(brands):
    for brand in brands:
        url = brand.get('b_link')
        print(brand.get('b_name') + " scrapping.....")

        rq = requests.get(url)
        soup = BeautifulSoup(rq.text, "html.parser")

        try:
            nomal_info = soup.find("div", {"id": "NormalInfo"})
            t_body = nomal_info.find("tbody")
            tr1 = t_body.find_all("tr", {"class": ""})
            tr2 = t_body.find_all("tr", {"class": "divide"})
            tr = tr1 + tr2
            if len(tr) <= 1:  # no jobs
                raise Exception()
        except:
            print(f"{brand.get('b_name')} No jobs Infomation")
        else:
            save_csv_file(tr, brand)


def save_csv_file(tr, brand):
    # file open
    file = open(f"./jobs/{brand.get('b_name')}.csv",
                mode="w", encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "last"])

    for tb in tr:
        place = tb.find("td", {"class": "local"}).text.strip()
        company = tb.find("span", {"class": "company"}).get_text().strip()
        time = tb.find("td", {"class": "data"}).get_text().strip()
        pay = tb.find("td", {"class": "pay"}).get_text().strip()
        last = tb.find("td", {"class": "regDate"}).get_text().strip()

        writer.writerow([place, company, time, pay, last])

    print(brand.get('b_name') + " done.")

    file.close()


brands = get_super_brands(brands)
get_brand_detail_infomation(brands)
