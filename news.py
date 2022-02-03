import requests
from bs4 import BeautifulSoup

#laTimes = requests.get("http://www.waronnetworks.com")
#soup = BeautifulSoup(laTimes.content)
#headings = soup.findAll('div', attrs={'class':'podcasts'})
#heading = soup.find_all("a" ,class_="podcasts")
#print(heading)
# for i in heading:
#     print(i.text)
# for div in soup.findAll('a', attrs={'class':'link'}):
#     print(div.find('a')['href'])
#     print(div.find('a').contents[0])
#     print(div.find('img')['src'])
toi_r = requests.get("https://greaterkashmir.com")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.find_all('a', class_="m-article-wide")
toi_headings = toi_headings[0:11]
toi_news=[]

for h in toi_headings:
    toi_news.append(h.text)
print(toi_news)


# ht_r = requests.get("https://www.hindustantimes.com/india-news/")
# ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
# ht_headings = ht_soup.findAll("div", {"class":"headingfour"})
# ht_headings = ht_headings[2:11]
# ht_news = []

# for n in ht_headings:
#     ht_news.append(n.text)
# print(ht_news)

# gk_r = requests.get("https://www.greaterkashmir.com/latest/")
# gk_soup = BeautifulSoup(gk_r.content, 'html5lib')
# gk_headings = gk_soup.find_all('h2')
# gk_headings = gk_headings[0:10]
# gk_news=[]

# for g in gk_headings:
#     gk_news.append(g.text)
# print(ht_news)