class CompanyMatch:

    # loop to compare user keywords from profile to keywords from company reviews
    def keywordCompare():
        usrKeywords = 1 #import user keywords stored in SQL
        numMatches = 1 #placeholder
        return numMatches, usrKeywords

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
        Score = (numMatches/usrKeywords) + catRating
