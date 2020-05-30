import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
# test1 = soup.select("table.table > tbody > tr")
tb = soup.find("table", {"class": "table"})
t_body = tb.find("tbody").find_all("tr")

country = []  # empty list

for c in t_body:
    country.append({"country": c.findAll('td')[0].get_text(
    ).capitalize(), "currency_code": c.findAll('td')[2].get_text()})


print("Hello! Please Choose Select a Country by Number:")
for idx, c in enumerate(country):
    print(f"# {idx} {c.get('country')}")


while True:
    try:
        answer = int(input("#: "))
        if(answer < 0 or answer > len(country)-1):
            print("Choose a number from the list.")
            continue
        else:
            print(f"You choose {country[answer].get('country')}")
            print(
                f"The currency code is {country[answer].get('currency_code')}")
            break
    except:
        print("That wasn't a number.")
        continue
