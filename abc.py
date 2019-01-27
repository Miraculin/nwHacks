from textblob import TextBlob
from bs4 import BeautifulSoup
import wikipedia
import random as rand

topic = input("\nChoose a topic for the trivia question: \n")
strn = wikipedia.summary(topic)

def paragraph(para):
    soup = BeautifulSoup(para)
    blob = TextBlob(soup.get_text(strip=True))
    retList = []
    for sentence in blob.sentences:
        for word in sentence.tags:
            if word[1] == "JJS" or word[1] == "RBS" or word[0] == "first" or word[0] == "last":
                retList.append([sentence.replace(word[0], "_", 1), word[0]])

    return retList

def convertSentenceToQuestion(sentences):
    randSentenceNum = rand.randint(0,len(sentences)-1)
    randSentence = sentences[randSentenceNum]
    print(randSentence[0])
    answer = input("\nThe correct superlative is : \n")

    if (answer == randSentence[1]):
        print("Correct Answer")
    else:
        print("Incorrect Answer, The correct superlative is %s" % randSentence[1])

convertSentenceToQuestion(paragraph(strn))
