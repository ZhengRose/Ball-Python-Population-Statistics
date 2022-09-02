from email import header
from optparse import Values
from wsgiref import headers
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib
import lxml
import numpy
import pandas as pd
import csv
import os
import os.path
import time

#set up soup
page = 1
url_lists = [ ]
#loop through pages
try: 
    for page in range(1,287863):
        req = Request('https://www.morphmarket.com/_us/c/reptiles/pythons/ball-pythons?sort=nfs&has_id=1&page={page}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        html = webpage.decode("utf-8")
        soup = BeautifulSoup(html,'html.parser')
#Loop through each page to find individual links
        div_container = soup.find_all('div', {'class','col-lg-3 col-md-4 col-sm-4 col-6 item-col move-up'})
        for each in div_container:
            lnk = each.a.get('href')
            url_lists.append("https://morphmarket.com" + lnk)
        page = page + 1
        time.sleep(1)
        print([page])
except: print('error', [page])

finally: 
    for link in url_lists:
        req2 = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        webpage2 = urlopen(req2).read()
        html2 = webpage2.decode("utf-8")
        soup2 = BeautifulSoup(html2, 'html.parser')

        meta_tag = soup2.find("meta", attrs= {'name':'description'})
        content = meta_tag.get('content')

    #Variables pulled and defined
        new= (content.split(':')[2])
        gender = (new.replace(', Maturity', '').replace(', Weight', '').replace(', Prey', ''))

        new2 = (content.split(':')[3])
        age = (new2.replace(', Prey', '').replace(', Weight', '').replace(', Birth', '').replace(', Price','').replace('Proven', ''))

        new3 = (content.split(':'))
        id = new3[-1]

        combo = str(gender) + str(age) + str(id)
        variables = combo.split()
        print(variables)

        data = pd.DataFrame([variables])
        data.to_csv('BallPyData.csv', mode = 'a', header = False)
        time.sleep(1)