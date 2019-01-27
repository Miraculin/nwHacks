import wikiRequests
import TextConvert

def main():
    canada = wikiRequests.createSectionsByTitle("Canada")
    # print(canada.getSections()["Demographics"])
    result = TextConvert.sentenceToQuestion(TextConvert.superlativeFilter(canada.getCorpus()))

    print(result[0])
    print(result[1])
if __name__ == "__main__":
    main()
