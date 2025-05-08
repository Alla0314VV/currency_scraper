import requests
from bs4 import BeautifulSoup
def fetch_data(url):
    web = requests.get(url)
    web.raise_for_status()
    return BeautifulSoup(web.content, 'html.parser')
def find_table(soup):
    table = soup.find('table', {'class': 'wikitable'})
    data = []
    rows = table.find_all('tr')
    for row in rows:
        mn = row.find_all('td')
        if len(mn) >= 3:
            code = mn[0].text.strip()
            num = mn[1].text.strip()
            r = mn[3].text.strip()
            data.append([code, num, r])
    return data
