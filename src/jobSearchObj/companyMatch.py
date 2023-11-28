from user import User
import Keywords
import company
#import views

class CompanyMatch:

    # loop to compare user keywords from profile to keywords from company reviews
    def keywordCompare(self, company_name1, company_name2):
        avgJoe = User()
        usrKeywords = avgJoe.getKeywords() #import user keywords stored in SQL
        # usrKeywords = ["good", "nice"] # test
        numMatches1 = 0 
        numMatches2 = 0
        com = company.Company()
        for x in usrKeywords:
            if x in com.findCompany(company_name1).keywords:
                numMatches1 += 1 
            if x in com.findCompany(company_name2).keywords:
                numMatches2 += 1 
        return usrKeywords, numMatches1, numMatches2

    def normalizeRanking(self, company_name1, company_name2,work_life_balance, compensation, job_security, management, culture):
        # import company scores
        catScores1 = [company.Company().findCompany(company_name1).rating_wl, company.Company().findCompany(company_name1).rating_pb,company.Company().findCompany(company_name1).rating_career,company.Company().findCompany(company_name1).rating_management,company.Company().findCompany(company_name1).rating_culture]
        catScores2 = [company.Company().findCompany(company_name2).rating_wl, company.Company().findCompany(company_name2).rating_pb,company.Company().findCompany(company_name2).rating_career,company.Company().findCompany(company_name2).rating_management,company.Company().findCompany(company_name2).rating_culture]
        # loop through each category rating
        normRank = [work_life_balance, compensation, job_security, management, culture]
        catRanking1 = []
        catRanking2 = []
        for index, cat in enumerate(catScores1):
            catRanking1.append((normRank[index] * catScores1[index]) / 5)

        for index, cat in enumerate(catScores2):
            catRanking2.append((normRank[index] * catScores2[index]) / 5)

        return catRanking1, catRanking2

    # score company
    def scoreCompany(self, company_name1, company_name2, work_life_balance, compensation, job_security, management, culture):
        usrKeywords, numMatches1, numMatches2 = self.keywordCompare(company_name1, company_name2)
        catRanking1, catRanking2 = self.normalizeRanking(company_name1, company_name2,work_life_balance, compensation, job_security, management, culture) #can pass in userRanking stuff as well as two companies to compare
        if len(usrKeywords)<1:
            usrKeywords = "word"
        Score1 = (numMatches1/len(usrKeywords)) + sum(catRanking1)/5
        Score2 = (numMatches2/len(usrKeywords)) + sum(catRanking2)/5
        #sort by score:
        matches = []
        if Score1>Score2:
            matches = [company_name1,company_name2]
        else:
            matches = [company_name2,company_name1]

        return matches
        
# test:
cm = CompanyMatch()
matches = cm.scoreCompany("Northrop Grumman", "Lockheed Martin", 1, 3, 5, 7, 9)
print(matches)