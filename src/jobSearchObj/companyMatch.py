from user import User
import Keywords
import company
import views

class CompanyMatch:

    # loop to compare user keywords from profile to keywords from company reviews
    def keywordCompare(company_name):
        usrKeywords = User.getKeywords() #import user keywords stored in SQL
        numMatches = 0 
        for x in usrKeywords:
            if x in company.findCompany(company_name).keywords:
                numMatches + 1 
        return numMatches

    def normalizeRanking(company_name, work_life_balance, compensation, job_security, management, culture):
        # import user's preference for category weight
        normRank = [work_life_balance, compensation, job_security, management, culture] #placeholder for normalized user ranking
        # import company scores
        catScores = company.findCompany(company_name).companyInfo[5:9]

        # loop through each category rating
        catRanking = []
        for cat in catScores:
            catRanking = (normRank *cat)/5

    # score company
    def scoreCompany(company_name, work_life_balance, compensation, job_security, management, culture):
        keywordCompare(company_name)
        normalizeRanking(company_name, work_life_balance, compensation, job_security, management, culture)
        Score = (len(numMatches)/len(usrKeywords)) + len(catRating)
