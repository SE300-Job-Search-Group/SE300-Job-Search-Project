from jobSearchObj import GenericDatabaseHandler

#Here's where we can extract keywords from the employer reviews

#import
dbh = GenericDatabaseHandler("./database/test.db")
initial = dbh.getTable("keywords")
print(initial)

#parse words
Keywords = []
Keywords = initial.split()
dbh.close()

#create dictionary
Dictionary = dict()

#remove common words from list
criteria = [ e for e in Keywords if len(e) > 4] #this just filters out short words
# will try a criteria that filters out any articles, maybe there's a library I can use

#count frequency of words
for x in criteria:
    if x in Dictionary:
        Dictionary[x] = Dictionary.get(x) + 1
    else:
        Dictionary[x] = 1

#show top 10 most frequent- maybe we can switch to storing top ten somewhere?
TopWords = sorted(Dictionary.items(), key=lambda x:x[1], reverse=True)
TopSorted= dict(TopWords)
TopTen=TopWords[:10]
print(*TopTen, sep = "\n") 
