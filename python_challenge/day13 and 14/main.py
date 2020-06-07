"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, send_file, redirect
import requests
from bs4 import BeautifulSoup
import os
from rOK_scrapper import get_rOK_jobs
from so_scrapper import get_SO_jobs
from wwr_scrapper import get_WWR_jobs
from exporter import save_to_file

os.system('clear')

app = Flask("Last_Scrapper")

fake_DB = {} # db

@app.route("/")
def home():
  return render_template('home.html')


@app.route("/result", methods=['POST'])
def result():
  search_word = request.form['search_term'].lower()
  job_list = []

  # db 처리
  existingJobs = fake_DB.get(search_word)
  if existingJobs:
    job_list = existingJobs
  else:
      job_list = get_rOK_jobs(search_word) + get_SO_jobs(search_word) + get_WWR_jobs(search_word)
      fake_DB[search_word] = job_list  
  
  num_of_jobs = len(job_list)

  return render_template(
    'result.html',
    job_list = job_list,
    search_word = search_word,
    num_of_jobs = num_of_jobs
  )

@app.route("/export")
def export():
  try:
    word = request.args.get("search")
    if not word:
      raise Exception()
    word = word.lower()
    jobs = fake_DB.get(word) # 검색을 하면 fakeDB로 들어가므로 무조건 DB에 있어야함
    if not jobs:
      raise Exception()

    save_to_file(jobs)

    return send_file(
      "jobs.csv",
      mimetype="text/csv",
      attachment_filename=f"{word}.csv",
      as_attachment=True
    )
  except:
    return redirect("/")


app.run(host = "0.0.0.0")
