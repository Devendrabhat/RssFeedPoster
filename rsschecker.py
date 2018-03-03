'''Basic commands

import feedparser
from bs4 import BeautifulSoup as bs

d['entries'][1] 
soup = bs(d['entries'][1].get('summary'),'html.parser')
print(soup.prettify()) 
print(soup.get_text()) 



'''
