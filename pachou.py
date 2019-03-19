import requests
from bs4 import BeautifulSoup
import bs4


def getHTML(url):
    try:
        r = requests.get(url,timeout = 200)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        print('错误')


def getINFO(html,ulist):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr.find_all("td")
            ulist.append(tds[0].string+''+tds[1].string+''+tds[2].string)


def main():
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTML(url)
    Uinfo=[]
    getINFO(html,Uinfo)
    for i in Uinfo:
        print(i)
main()
        
        
