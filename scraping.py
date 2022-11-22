import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


# use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# save page content
src = result.content

# create soup object to parse content
soup = BeautifulSoup(src , "lxml")