#import httplib2
#from bs4 import BeautifulSoup, SoupStrainer

#http = httplib2.Http()
#status, response = http.request('http://www.greaterkashmir.com')

#for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
#    if link.has_attr('href'):
#        print(link['href'])



#from bs4 import BeautifulSoup
#import urllib.request

#parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
#resp = urllib.request.urlopen("http://www.gpsbasecamp.com/national-parks")
#soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

#for link in soup.find_all('a', href=True):
#    print(link['href'])



from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import datetime

def ndtv_latest(link):
    parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    resp = requests.get(link)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, parser, from_encoding=encoding)
    news = soup.find_all('a' ,href=True)
    news=news[46:90]
    title=[]
    url = []
    for text in news:
        title.append(text.text)
    
    for links in news:
        url.append(links['href'])
    
    gk = dict(zip(title,url))
    save_file(gk)
    for title,url in gk.items():
       print(title," : ",url)


def save_file(filename):
    file=open('downloads/ndtv'+str(datetime.datetime.now())+'.txt','w')
    file.write(str(filename))
    file.close()

ndtv_latest("https://ndtv.com")