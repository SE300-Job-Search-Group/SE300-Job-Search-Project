from rake_nltk import Rake
import rake_nltk
#Here's where we can extract keywords from the employer reviews

#import
initial = "Everything from the work to working with your co-workers. The Management team there are amazing. I have not experience anything stressful there. The environment and culture are wonderful. I have no complaints about L3 Harris. My day was like any other day at the job. Go in and perform your duties as required. Do the work by following your work procedures and standards and you will be great."
print(initial)

#parse words
r = Rake()
r.extract_keywords_from_text(initial)
rPhrase = r.get_ranked_phrases()
print(rPhrase)
