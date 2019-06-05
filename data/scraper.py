from requests import get
from bs4 import BeautifulSoup

url = 'https://www.boxofficemojo.com/movies/?id=superman2015.htm'
response = get(url)
parsed = BeautifulSoup(response.text, 'html.parser')


dom = parsed.find_all('font', size=4)
for i in dom:
    domestic = i.b.text
    print(domestic)


rows = parsed.findAll('tr')
getNext = False
for row in rows:
    if row.td != None:
        if row.td.b != None:
            if row.td.b.text == 'Worldwide:':
                print(row.td.b.next_sibling.text)
            elif getNext:
                worldwide = row.td.b.text
                print(worldwide)
                getNext = False
