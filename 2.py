from bs4 import BeautifulSoup
import requests

urltest = requests.get('https://coreyms.com/page/3').text
soup = BeautifulSoup(urltest, 'html.parser')

# with open('simple.html') as htmlfile:
#     htext = BeautifulSoup(htmlfile, 'lxml')

# result = htext.link

# print(result)


# resultwo = htext.find_all('link')
# for i in resultwo:
#     print(i.get('href'))

# print(htext.h1)
# print(htext.h1)

for i in soup.find_all('iframe'):
    print(i.get('src'))