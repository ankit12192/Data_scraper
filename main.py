#Simple script which fetches links from a website and prints it , will be building on this script

import urllib2
from bs4 import BeautifulSoup
url = "http://newtonhq.com"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
#print soup.prettify()
all_link = soup.find_all("a")
for link in all_link:
    print link.get("href")