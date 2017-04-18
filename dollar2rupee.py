import requests
from bs4 import BeautifulSoup
page = requests.get('http://www.dollar2rupee.net/')
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    rate = soup.find_all('tr')[3].find_all('td')[3].get_text()
    print "Todays rate : %s" %rate
else:
    print "Unable to parse website"

