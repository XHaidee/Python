import requests
from bs4 import BeautifulSoup
result=requests.get("https://merolagani.com/")
# print(result.status_code)
# print(result.headers)
source=result.content
# print(source)
soup=BeautifulSoup(source,"html.parser")
title=soup.find_all("iframe")
print(title)
print("\n")