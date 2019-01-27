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
    print(result["query"]["pages"][0]["revisions"][0]["content"])
    ret.setCorpus(result["query"]["pages"][0]["revisions"][0]["content"])
    ret.printCorpus()
    return ret

if __name__ == "__main__":
    createArticleByTitle("Canada")
