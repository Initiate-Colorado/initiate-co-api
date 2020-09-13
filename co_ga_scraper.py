from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def coGaScraper():
  results = {}
  url = "https://leg.colorado.gov/content/how-file-initiatives"
  response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
  web_page = urlopen(response).read()
  page_soup = BeautifulSoup(web_page, "html.parser")
  section = page_soup.find('div', 'field-item even')
  titles = section.findAll('h5', text=True)
  list_of_due_dates = section.findAll('p')[1:]
  for title in titles:
    results["step1_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[0].contents[0].get_text())).group(0)
    results["step2_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[1].contents[0].contents[0].contents[0].replace(u'\xa0', ' '))).group(0)
    results["step3_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[3].contents[0].get_text())).group(0)
    results["step4_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[4].contents[0].get_text())).group(0)
    results["step5_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[5].contents[0].get_text())).group(0)
    results["step6_due_date"] = ''
    results["step7_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[6].contents[0].get_text())).group(0)
    results["step8_due_date"] = ''
    results["step9_due_date"] = 'Number of valid signatures required for the 2020 election:  124,632'
    results["step10_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[8].contents[0].get_text())).group(0)
    results["step11_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[9].contents[0].get_text())).group(0)
    results["step12_due_date"] = re.search('(\w{3,}\s\d{1,},\s\d{1,4})',str(list_of_due_dates[10].contents[0].get_text())).group(0)
    results["step13_due_date"] = ''
    results["step14_due_date"] = ''
  return results
  
  