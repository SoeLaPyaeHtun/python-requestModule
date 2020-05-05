import requests
import re

result = requests.get("http://creatigon.com/")


test = result.text
searchresult = re.findall("<img src=\"(.*)\" alt=\"(.*)\">", test)

for i in searchresult:
    print(i[0])

