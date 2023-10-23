from company import Company

#example case of how to use job Object
tempComp = Company(1) # ID = 1
print("Company ID: ", tempComp.getId(), type(tempComp.getId()))
print("Company Name: ", tempComp.getName(),type(tempComp.getName()))
print("Industry: ", tempComp.getIndustry(),type(tempComp.getIndustry()))
print("Keywords: ", tempComp.getKeywords(),type(tempComp.getKeywords()))
print("Rating(Overall, Work-life, Pay/Benefits, Career, Management, Culture): ", tempComp.getRating(),type(tempComp.getRating()))