import requests
import json
from bs4 import BeautifulSoup

API_LINK = 'https://en.wikipedia.org/w/api.php'

class Article:

    def __init__(self, title):
        self.title = title

    def setCorpus(self, text):
        self.corpus = text

    def printCorpus(self):
        print(self.corpus)

    def setSections(self, sections):
        self.sections = sections

    def printSections(self):
        print(self.sections)

    def getSections(self):
        return self.sections

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
    ret.printCorpus()
    return ret

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

def createSectionsByTitle(pageTitle):
    ret = Article(pageTitle)
    sections = createSectionsDictionary(pageTitle)
    i=0;
    sectCorpus = {}
    for section in sections:
        req = {"action":"parse",
                "page": pageTitle,
                "prop":"text",
                "section":i,
                "format":"json",
                "formatversion":2}
        result = requests.get(API_LINK, params=req).json();
        sectCorpus[sections[i]] = BeautifulSoup(result["parse"]["text"]).get_text()
        i+=1
    ret.setSections(sectCorpus)
    ret.printSections()
    return ret

def createSectionsDictionary(pageTitle):
    req = {"action":"parse",
            "format":"json",
            "page":pageTitle,
            "formatversion":2,
            "prop": "sections",
            }
    result = requests.get(API_LINK, params=req).json()
    ret = [None]*len(result["parse"]["sections"])
    for section in result["parse"]["sections"]:
        print(section["line"])
        ret[int(section["index"])-1] = section["line"]
    return ret

if __name__ == "__main__":
    createArticleByTitle("Canada")
    createArticleByTitleList(["Ireland", "Iceland"])
    createArticlesByCategory("Classical_studies",10)
    createArticlesByCategory("Classics",10)
    createSectionsByTitle("Canada")
