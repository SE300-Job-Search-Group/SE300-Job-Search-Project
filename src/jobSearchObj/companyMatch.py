from user import User
import Keywords

class CompanyMatch:

    # loop to compare user keywords from profile to keywords from company reviews
    def keywordCompare():
        usrKeywords = User.getKeywords() #import user keywords stored in SQL
        numMatches = 0 
        for x in usrKeywords:
            if x in Keywords.rPhrase:
                numMatches + 1 
        return numMatches

    # import user's preference for category weight
    normRank = 1 #placeholder for normalized user ranking
    # import company scores
    catScores = [1, 2, 3, 4, 5]
    # normalize rankings

    # loop through each category rating
    catRanking = []
    for cat in catScores:
        catRanking = (normRank *cat)/5

    # score company
    def scoreCompany():
        keywordCompare()
        Score = (len(numMatches)/len(usrKeywords)) + len(catRating)
