from rake_nltk import Rake
import rake_nltk
import company
#Here's where we can extract keywords from the employer reviews

def extractKeywords(initial):

    #import
    print(initial)

    #parse words
    r = Rake()
    r.extract_keywords_from_text(initial)
    rPhrase = r.get_ranked_phrases()

    return rPhrase
