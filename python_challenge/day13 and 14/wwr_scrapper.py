### We Work Remotely Job Scrapper ###
import requests
from bs4 import BeautifulSoup

def get_WWR_jobs(search_word):
  url_WWR = f"https://weworkremotely.com/remote-jobs/search?term={search_word}"

  wwr_list = []
  rq = requests.get(url_WWR)
  soup = BeautifulSoup(rq.text, "html.parser")
  
  job_cards = soup.find("div", {"class":"content"}).find("div", {"class":"jobs-container"}).find("section", {"class":"jobs"}).find_all("li", {"class":"feature"})

  for card in job_cards:
    title = card.find("span", {"class":"title"}).get_text()
    company = card.find("span", {"class":"company"}).get_text()
    link = card.find("span", {"class":"title"}).parent['href']
    link = "https://weworkremotely.com" + link
    wwr_list.append({"title":title, "company":company, "link":link})

  return wwr_list