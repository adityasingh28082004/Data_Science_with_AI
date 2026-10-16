import urllib.request 
from bs4 import BeautifulSoup
def scrape_mobiles(url):
   request = urllib.request.Request(url,headers={
    "User-Agent": "Mozilla/5.0"
   })
   response = urllib.request.urlopen(request)
   content = response.read()

   soup = BeautifulSoup(content, features="html.parser")
   mobiles = soup.find_all("div", class_="LwDgZ8 eq0K9s tBcEQe")
   # for mobile , moblie in enumerate(mobiles, start=1):
   #    title = mobile.find_all('div', class_='lvJbLV col-12-12')
   print(mobiles)


scrape_mobiles('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

