



'''
# Basic commands for feeds
# 
# import feedparser
# from bs4 import BeautifulSoup as bs
# d = feedparser.parse('link')
# d['entries'][1] 
# soup = bs(d['entries'][1].get('summary'),'html.parser')
# print(soup.prettify()) 
# print(soup.get_text()) 
# 
# Returns the Science news
# d = feedparser.parse('http://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms')
# for post in d.entries:
#     summary = post.get('summary')
#     soup = bs(summary,'html.parser')
#     print(post.title+': '+soup.get_text())
#     
'''


'''
# from facepy import GraphAPI 
# https://developers.facebook.com/tools/explorer/2060180224225613?method=GET&path=post-id&version=v2.12
# AT = 'EAAdRuRZAwMU0BAMOnuuIkgrx6SZAPHpkqHnWWWyvsESZBdQGS5dhbFoUSAbX5VqwwLZAcAwmMtA1ZBWHawR7TwHZCsLDIyMNlz4nfb2ub1PzCt16xEsgB8ge8wpAXABXkSkxagrvmc6nyfBMMCZBK29pOsPy9gZAFcXPKgEtuqBpt7pV8p8keiKSC4fmyy9KxMFZCrmSraZBpbcgZDZD'
# graph = GraphAPI(AT) 
# words = "Always bear in mind that your own resolution to succeed is more important than any one thing. -Abraham Lincoln" 
# graph.post('me/feed', message=words)
'''

'''

# link = d['entries'][1].get('link')
# data = "Title => "+post.title+'\nSummary => '+soup.get_text()+'\nLink => '+link
# graph.post('me/feed', message=data)


'''