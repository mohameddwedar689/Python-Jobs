import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# main lists
job_title = []
company_name = []
locations_name = []
skills = []


# use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# save page content
src = result.content

# create soup object to parse content
soup = BeautifulSoup(src , "lxml")


# find the elements containing info we need -> job title , job skills , company name , location name
job_titles = soup.find_all("h2" , {"class":"css-m604qf"})
company_names = soup.find_all("a" , {"class":"css-17s97q8"})
locations_names = soup.find_all("span" , {"class":"css-5wys0k"})
job_skills = soup.find_all("div" , {"class":"css-y4udm8"})

# loop over returnd lists to extract needed info into other list
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    locations_name.append(locations_names[i].text)
    skills.append(job_skills[i].text)
