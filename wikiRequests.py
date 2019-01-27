import requests
import json
from bs4 import BeautifulSoup

API_LINK = 'https://en.wikipedia.org/w/api.php'
BAD_SECTIONS = ["See Also", "External Links", "References", "Further Reading", "Notes"]

class Article:

    def __init__(self, title):
        self.title = title
        self.corpus = None
        self.sections = None

    def setCorpus(self, text):
        self.corpus = text

    def printCorpus(self):
        print(self.corpus)

    def getCorpus(self):
        return self.corpus

    def setSections(self, sections):
        self.sections = sections

    def printSections(self):
        print(self.sections)

    def getSections(self):
        return self.sections

    def serialize(self):
        return {
            "title":self.title,
            "corpus":self.corpus,
            "sections":self.sections
        }

def createArticleByTitle(pageTitle):
    ret = Article(pageTitle)
    req = {"action":"query",
            "format":"json",
            "titles":pageTitle,
            "formatversion":2,
            "prop": "revisions",
            "rvprop": "content"}
    result = requests.get(API_LINK, params=req).json();
    ret.setCorpus(result["query"]["pages"][0]["revisions"][0]["content"])
    #ret.printCorpus()
    return ret

def addCorpus(Article, pageTitle):
    req = {"action":"query",
            "format":"json",
            "titles":pageTitle,
            "formatversion":2,
            "prop": "revisions",
            "rvprop": "content"}
    result = requests.get(API_LINK, params=req).json();
    Article.setCorpus(BeautifulSoup(result["query"]["pages"][0]["revisions"][0]["content"]).get_text())
    return Article

def createArticleByTitleList(pageTitles):
    retList=[]
    req = {"action":"query",
            "format":"json",
            "titles":pageTitles,
            "formatversion":2,
            "prop": "revisions",
            "rvprop": "content"}
    result = requests.get(API_LINK, params=req).json();
    for page in result["query"]["pages"]:
        temp = Article(page["title"])
        temp.setCorpus(page["revisions"][0]["content"])
        retList.append(temp)
    return retList

def createArticlesByCategory(category, limit):
    retList=[]
    req = {"action":"query",
            "list":"categorymembers",
            "cmtitle":"Category:"+category,
            "cmlimit":limit,
            "format":"json",
            "formatversion":2}
    result = requests.get(API_LINK, params=req).json();
    titles = []
    for member in result["query"]["categorymembers"]:
        titles.append(member["title"])
    if len(titles) == 0:
        return []
    return createArticleByTitleList(titles)

def createSectionsByCategory(category, limit):
    retList=[]
    req = {"action":"query",
            "list":"categorymembers",
            "cmtitle":"Category:"+category,
            "cmlimit":limit,
            "format":"json",
            "formatversion":2}
    result = requests.get(API_LINK, params=req).json();
    titles = []
    for member in result["query"]["categorymembers"]:
        titles.append(member["title"])
    if len(titles) == 0:
        return []
    for title in titles:
        retList.append(createSectionsByTitle(title))
    return retList

def createSectionsByTitle(pageTitle):
    ret = Article(pageTitle)
    sections = createSectionsDictionary(pageTitle)
    i=0;
    sectCorpus = {}
    req = {"action":"parse",
            "page": pageTitle,
            "prop":"text",
            "section":i,
            "format":"json",
            "formatversion":2}
    result = requests.get(API_LINK, params=req).json();
    sectCorpus["Section0"] = BeautifulSoup(result["parse"]["text"]).get_text()
    i+=1
    for section in sections:
        req = {"action":"parse",
                "page": pageTitle,
                "prop":"text",
                "section":i,
                "format":"json",
                "formatversion":2}
        result = requests.get(API_LINK, params=req).json();
        #print(result)
        sectCorpus[sections[i-1]] = BeautifulSoup(result["parse"]["text"]).get_text()
        i+=1
    ret.setSections(sectCorpus)
    ret.setCorpus(parseWikiHMTL(pageTitle))
    #addCorpus(ret, pageTitle)
    return ret

def createSectionsDictionary(pageTitle):
    req = {"action":"parse",
            "format":"json",
            "page":pageTitle,
            "formatversion":2,
            "prop": "sections",
            }
    result = requests.get(API_LINK, params=req).json()
    #print(result)
    ret = [None]*(len(result["parse"]["sections"]))
    #print(ret)
    for section in result["parse"]["sections"]:
        if (not section["line"] in BAD_SECTIONS):
            ret[int(section["index"])-1] = section["line"]
    return ret

def getRandomPages():
    req = {"action":"query",
            "format":"json",
            "list":"random",
            "rnlimit":5,
            "formatversion":2,
            "rnnamespace":0
            }
    result = requests.get(API_LINK, params=req).json()
    #print(result["query"]["random"])
    return result["query"]["random"]

def getRandomCategories():
    pages = getRandomPages()
    titles = list(map(lambda x: x["title"],pages))
    retList=[]
    for title in titles:
        req = {"action":"query",
                "format":"json",
                "titles":title,
                "formatversion":2,
                "prop": "categories"
                }
        result = requests.get(API_LINK, params=req).json()
        retList.extend(result["query"]["pages"][0]["categories"])
    return retList

def parseWikiHMTL(pageTitle):
    req = {"action":"parse",
            "format":"json",
            "page":pageTitle,
            "formatversion":2,
            "prop": "text"}
    result = requests.get(API_LINK, params=req).json();
    page = result["parse"]["text"]
    soup = BeautifulSoup(page)
    for elem in soup.find_all("img"):
        elem.decompose()
    for elem in soup.find_all(class_="navbox"):
        elem.decompose()
    for elem in soup.find_all(class_="reflist"):
        elem.decompose()
    for elem in soup.find_all("table"):
        elem.decompose()
    for elem in soup.find_all(class_="refbegin"):
        elem.decompose()
    for elem in soup.find_all(class_="reference"):
        elem.decompose()
    for elem in soup.find_all(class_="external"):
        elem.decompose()
    for elem in soup.find_all(class_="image"):
        elem.decompose()
    for elem in soup.find_all(class_="mw-editsection"):
        elem.decompose()
    for elem in soup.find_all(class_="mw-headline"):
        elem.decompose()
    for elem in soup.find_all(class_="toc"):
        elem.decompose()
    #print(soup.get_text())
    return soup.get_text()


if __name__ == "__main__":
    #createArticleByTitle("Canada")
    #createArticleByTitleList(["Ireland", "Iceland"])
    #createArticlesByCategory("Classical_studies",10)
    #createArticlesByCategory("Classics",10)
    #createSectionsByTitle("Canada")
    parseWikiHMTL("Airbus_A310")
