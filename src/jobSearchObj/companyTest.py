from company import Company

#example case of how to use job Object
tempComp = Company().fillByID(1) # ID = 1
print("Company ID: ", tempComp.getID(), type(tempComp.getID()))
print("Company Name: ", tempComp.getName(),type(tempComp.getName()))
print("Industry: ", tempComp.getIndustry(),type(tempComp.getIndustry()))
print("Keywords: ", tempComp.getKeywords(),type(tempComp.getKeywords()))
print("Description: ",tempComp.getDesc(),type(tempComp.getDesc()))
print("Rating(Overall, Work-life, Pay/Benefits, Career, Management, Culture): ", tempComp.getRating(),type(tempComp.getRating()))

tempName = 'MacroHard'
tempIndustry = 'Technology'
tempKwds = ['MacroHard','Technology','Macros','Hardness']
tempDesc = "We are very Macro and very Hard?????"
#ratings order [overall, work-life, pay&benefits, career, management, culture]
tempRatings = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]

tempComp = Company().newCompany(tempName,tempIndustry,tempKwds,tempDesc,tempRatings)

print("Company ID: ", tempComp.getID(), type(tempComp.getID()))
print("Company Name: ", tempComp.getName(),type(tempComp.getName()))
print("Industry: ", tempComp.getIndustry(),type(tempComp.getIndustry()))
print("Keywords: ", tempComp.getKeywords(),type(tempComp.getKeywords()))
print("Description: ",tempComp.getDesc(),type(tempComp.getDesc()))
print("Rating(Overall, Work-life, Pay/Benefits, Career, Management, Culture): ", tempComp.getRating(),type(tempComp.getRating()))


# adding & viewing reviews
tempReviews = ["""I hate this company!!! Shitty worklife balance ANNNND Im not even getting paid WTF!""","REVIEW NUMBER 2 (Im LAZY)"]

returnReviews = tempComp.addReviews(tempReviews)

print(tempComp.getReviewContents())