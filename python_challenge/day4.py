import requests
import os

# URLs valid checking function
def valid_check(temp_list):
  for check in temp_list:
    if("." not in check):
      print(f"{check} is not a valid URL")
      return False

def formatting_URLs(temp_list):
  check_list = [] # empty list
  for check in temp_list:
    temp = check.strip()
    temp = temp.lower()
    if("http://" not in temp and "https://" not in temp):
      check_list.append("http://" + temp)
    else:
      check_list.append(temp)
  return check_list

def url_check(temp_list):
  for url in temp_list:
    try:
      r = requests.get(url)
    except requests.ConnectionError:
      print(f"{url} is down!")
      continue
    check_urls = r.status_code
    if(check_urls != 200):
      print(f"{url} is down!")
    else:
      print(f"{url} is up!")

def check_restart():
  while True:
    judge = input("Do you want to start over? y/n ")
    if(judge == "y"):
      return True
    elif(judge == "n"):
      return False
    else:
      print("That's not a valid answer")
      continue

#### main ####
check_list = [] # create empty list 

while True:
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  # input URLs text
  temp = input()
  check_list = temp.split(",")

  check_valid = valid_check(check_list)
  if(check_valid == False):
      if(check_restart() == True):
        os.system('cls') # clear console error ㅠㅠ 
        continue
      else:
        print("k. bye!")
        break

  check_list = formatting_URLs(check_list)
  url_check(check_list)
  if(check_restart() == True):
    os.system('cls') # clear console error ㅠㅠ 
    continue
  else:
    print("k. bye!")
    break
    
