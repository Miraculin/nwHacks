import wikiRequests
import abc

def main():
    canada = wikiRequests.createSectionsByTitle("Canada")
    print(canada.getSections()["Demographics"])
    abc.convertSentenceToQuestion(paragraph(canada.getSections()["Demographics"]))

if __name__ == "__main__":
    main()
