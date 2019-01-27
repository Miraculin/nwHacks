from textblob import *

def paragraph(para):
    blob = TextBlob(para)
    retList = []
    for sentence in blob.sentences:
        for word in sentence.tags:
            if word[1] == "JJS" or word[1] == "RBS" or word[0] == "first" or word[0] == "last":
                retList.append(sentence)
    return retList

def sentenceToQuestion(list):
    nouns = []
    questionlist = []
    for sen in list:
        index = 1
        question = ""

        tags = sen.tags
        #print(tags)

        if tags[0][1] == "PRP":
            question = "What"
            while index < len(tags):
                question += " " + tags[index][0]
                index += 1
        print(question)

        if not question:
            questionlist.append(question)
    return questionlist

asdf = "Aaron is the first man on Earth."

sentenceToQuestion(paragraph(asdf))
