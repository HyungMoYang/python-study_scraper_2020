### Stack Overflow Job Scrapper ###
import requests
from bs4 import BeautifulSoup

def get_SO_jobs(search_word):
  url_SO = "https://stackoverflow.com/jobs?r=true&q={search_word}"

  so_list = []
  rq = requests.get(url_SO)
  soup = BeautifulSoup(rq.text, "html.parser")
  
  job_cards = soup.find("div", {"class":"container"}).find("div", {"class":"js-search-container"}).find("div", {"class":"listResults"}).find_all("div", {"class":"js-result"})

  for card in job_cards:
    title = card.find("h2", {"class":"mb4"}).find("a", {"class":"s-link"}).get_text()
    company =  card.find("h3", {"class":"fc-black-700"}).find("span").get_text().strip()
    link = card.find("h2", {"class":"mb4"}).find("a", {"class":"s-link"})['href']
    link = "https://stackoverflow.com" + link
    so_list.append({"title":title, "company":company, "link":link})

  return so_list