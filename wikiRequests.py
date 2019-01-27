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
    print(result)
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

if __name__ == "__main__":
    createArticleByTitle("Canada")
    createArticleByTitleList(["Ireland", "Iceland"])
    createArticlesByCategory("Classical_studies",10)
    createArticlesByCategory("Classics",10)
