from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def webScraper():
  url = "https://www.sos.state.co.us/pubs/elections/Initiatives/titleBoard/index.html"
  response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
  web_page = urlopen(response).read()
  page_soup = BeautifulSoup(web_page, "html.parser")
  result = []
  onBallot = page_soup.find("div", "w3-toppad")
  ballotTitle = onBallot.findAll('button', 'w3-btn-block1 w3-left-align w3-white w3-large w3-margin-top w3-hover-fog')
  representatives = onBallot.findAll('div', 'w3-col m12 l6')
  for content in ballotTitle:
      resultDict = {}
      ballotNumber = re.search("\d+", str(content.contents[0])).group(0)
      resultDict['ballotNumber'] = ballotNumber
      ballotTitle = re.search('[a-zA-z].+', str(content.contents[0])).group(0)
      resultDict['ballotTitle'] = ballotTitle 
      result.append(resultDict)
  for content in representatives:
      nameHash= {}
      if(len(content.contents[1].contents) == 5):
          nameHash['representative1'] = content.contents[1].contents[0]
          nameHash['representative1Address'] = content.contents[1].contents[2] + content.contents[1].contents[4]
      if(len(content.contents[1].contents) == 1):
          nameHash['representative1'] = content.contents[1].contents[0]
      if(len(content.contents[1].contents) == 7):
          nameHash['representative1'] = content.contents[1].contents[0]
          if(list(content.contents[1].contents[2].split()[0].split()[0])[0].isdigit()):
              nameHash['representative1Address'] = content.contents[1].contents[2] + content.contents[1].contents[4]
          else:
              nameHash['representative2'] = content.contents[1].contents[2]
              nameHash['representative1Address'] = content.contents[1].contents[4] + content.contents[1].contents[6]
      result.append(nameHash) 
  return result 