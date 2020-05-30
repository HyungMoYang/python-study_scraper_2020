import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
# print(format_currency(5000, "COP", locale="ko_KR"))


def create_list(countries):
    url = "https://www.iban.com/currency-codes"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    tb = soup.find("table", {"class": "table"})
    t_body = tb.find("tbody").find_all("tr")

    for c in t_body:
        countries.append({"country": c.findAll('td')[0].get_text(
        ).capitalize(), "currency_code": c.findAll('td')[2].get_text()})

    return countries


def currency_converter(c1_code, c2_code, money):
    urlurl = f"https://transferwise.com/gb/currency-converter/{c1_code.lower()}-to-{c2_code.lower()}-rate?amount={money}"

    result = requests.get(urlurl)
    soup = BeautifulSoup(result.text, "html.parser")
    rst = soup.find("input", {"class": "js-TargetAmount"})['value']

    return rst


countries = []
countries = create_list(countries)
print("Welcome to Currency converter pro 2020:\n")
for idx, c in enumerate(countries):
    print(f"# {idx} {c.get('country')}")

print("\nWhere are u from? Choose a country by number.\n")
c1 = int(input("#: "))
print(countries[c1].get('country'))

print("\nNow choose another country.\n")
c2 = int(input("#: "))
print(countries[c2].get('country'))

c1_code = countries[c1].get('currency_code')
c2_code = countries[c2].get('currency_code')

print(f"\nHow many {c1_code} do you want to convert {c2_code}?")
while True:
    try:
        money = int(input("#: "))
        break
    except:
        print("That wasn't a number.")
        continue


rst = currency_converter(c1_code, c2_code, money)
# print(format_currency(money, c1_code, locale="ko_KR") + " is " + format_currency(rst, c2_code, locale="ko_KR"))
print(f"{format_currency(money, c1_code, locale='ko_KR')} is {format_currency(rst, c2_code, locale='ko_KR')}")
