#robot code taken from https://docs.python.org/2/library/robotparser.html
#crawler code taken from http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/
#index code from https://mydevelopedworld.wordpress.com/2012/08/30/want-it-faster-hash-table-is-the-answer/
from urllib import robotparser
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from urllib.parse import urlparse
from urllib.parse import urljoin
from url_normalize import url_normalize

class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]


    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url) 
	
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

def checkRobots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urljoin(url, 'robots.txt'))
    rp.read()
    return rp.can_fetch("*", url)

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def spider(url, maxPages):
    pagesToVisit = [url]
    numberVisited = 0
    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = url_normalize(pagesToVisit[0])
        robot_url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
            if checkRobots(robot_url):
                print(numberVisited, "Visiting:", url)
                parser = LinkParser()
                data, links = parser.getLinks(url)
                pagesToVisit = pagesToVisit + links
                print(" **Success!**")
            else:
                print ("Robot exclusion forbids crawling this page")
        except:
            print(" **Failed!**")

