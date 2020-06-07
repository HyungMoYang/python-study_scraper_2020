### Remote OK Job Scrapper ###
import requests
from bs4 import BeautifulSoup

def get_rOK_jobs(search_word):
  url_rOk = f"https://remoteok.io/remote-{search_word}-jobs"

  rOK_list = []
  rq = requests.get(url_rOk)
  soup = BeautifulSoup(rq.text, "html.parser")

  job_cards = soup.find("div", {"class":"page"}).find("div", {"class":"container"}).find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})


  for card in job_cards:
    title = card.find("h2", {"itemprop":"title"}).get_text()
    company = card.find("h3", {"itemprop":"name"}).get_text()
    link = card.find("a", {"itemprop":"url"})['href']
    link = "https://remoteok.io" + link
    rOK_list.append({"title":title, "company":company, "link":link})

  return rOK_list
    