import requests
import json

API_LINK = 'https://en.wikipedia.org/w/api.php'

class Article:

    def __init__(self, title):
        self.title = title

    def setCorpus(self, text):
        self.corpus = text

    def printCorpus(self):
        print(self.corpus)

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

def createArticleByCategory(category, limit):
    return None

if __name__ == "__main__":
    createArticleByTitle("Canada")
    createArticleByTitleList(["Ireland", "Iceland"])
