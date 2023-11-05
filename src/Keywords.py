from rake_nltk import Rake
import rake_nltk
#Here's where we can extract keywords from the employer reviews

#import
initial = "This is a test until we can successfully import the company reviews from the SQL database."
print(initial)

#parse words
r = Rake()
r.extract_keywords_from_text(initial)
rPhrase = r.get_ranked_phrases()
print(rPhrase)
