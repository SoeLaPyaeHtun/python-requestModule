import requests
import re
from bs4 import BeautifulSoup

result = requests.get("https://roadtoburmatravel.com/")


test = result.text
soup = BeautifulSoup(test, 'html.parser')
for i in soup.find_all('a'):
    print(i.get('href'))
    
#searchresult = re.findall("<img src=\"(.*)\" alt=\"(.*)\">", test)
#searchlink = re.findall("src=\'(.*)\'", test)

#for i in searchresult:
 #   print(i[0])

# for i  in searchlink:
#     print(i)