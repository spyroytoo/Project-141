from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_proper_names_of_stars"
browser = webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)
stars_data = []

def scrape():
    temp_list = []
    soup = BeautifulSoup(browser.page_source,"html")
    star_tabel = soup.find("table",attrs={"class","wikitable sortable jquery-tablesorter"})
    star_body = star_tabel.find("tbody")
    for tr_tag in star_body.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        for td_tag in td_tags:
            a_tags = td_tag.find_all("a")
            for a_tag in a_tags:
                temp_list.append(a_tag.contents[0])
    stars_data.append(temp_list)
scrape()
print(stars_data[0])
