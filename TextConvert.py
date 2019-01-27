from textblob import *

def superlativeFilter(para):
    blob = TextBlob(para)
    retList = []
    for sentence in blob.sentences:
        for word in sentence.tags:
            if word[1] == "JJS" or word[1] == "RBS" or word[0] == "first" or word[0] == "last":
                retList.append(sentence)
    return retList


def sentenceToQuestion(list):
    questionlist = []
    answerlist = []
    result = []

    for sen in list:
        tags = sen.tags
        question = ""
        answer = ""

        # if tags[0][1] == "PRP":
        #     question = createQuestion(tags, 1)

        if tags[0][1] == "DT":
            if tags[1][1][0] == "N" and tags[1][1][1] != "N" and not tags[2][1] == "IN":
                answer = tags[1][0]
                tagindex = 1
                while tags[tagindex][1][0] == "N" and tagindex < len(tags):
                    answer += " " + tags[tagindex][0]
                    tagindex += 1

                tagindex -= 1
                index = sen.find(tags[tagindex][0]) + len(tags[tagindex][0])
                question = createQuestion(sen, index)

        if tags[0][1][0] == "N":
            answer = tags[0][0]
            tagindex = 1
            while tags[tagindex][1][0] == "N" and tagindex < len(tags):
                answer += " " + tags[tagindex][0]
                tagindex += 1

            tagindex -= 1
            index = sen.find(tags[tagindex][0]) + len(tags[tagindex][0])
            question = createQuestion(sen, index)

        if question:
            if question.find(answer) == -1:
                print(sen)
                print(question)
                print(answer)

                questionlist.append(question)
                answerlist.append(answer)

    result.append(questionlist)
    result.append(answerlist)
    return result

def createQuestion(sentence, index):
    question = "What"

    question += " " + str(sentence[index + 1:-1])
    index += 1

    return question
