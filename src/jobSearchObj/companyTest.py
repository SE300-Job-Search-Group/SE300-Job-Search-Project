from company import Company

#example case of how to use job Object
tempComp = Company(1) # ID = 1
print("Company ID: ", tempComp.getId())
print("Company Name: ", tempComp.getName())
print("Industry: ", tempComp.getIndustry())
print("Keywords: ", tempComp.getKeywords())
print("Rating: ", tempComp.getRating())