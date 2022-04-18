import json


# ==================================================================================
# Load analyzed repos from file
# ==================================================================================
file = "all_analyzed_repos.json"
allRepos = {}
with open(file, "r") as fromFile:
	allRepos = json.load(fromFile)
	print(str(len(allRepos['repos'])) + " repos was loaded from the file")

usedLambda = []
usedSmartPointer = []
usedBoth = []

for repo in allRepos["repos"]:
	if repo["total_lambdas"] > 0:
		usedLambda.append(repo)
	if repo["total_smartpointers"] > 0:
		usedSmartPointer.append(repo)
	if repo["total_lambdas"] > 0 and repo["total_smartpointers"] > 0:
		usedBoth.append(repo)

print("")
print("Total repos:                    " + str(len(allRepos["repos"])))
print("Repos that used Lambdas:        " + str(len(usedLambda)))
print("Repos that used Smart Pointers: " + str(len(usedSmartPointer)))
print("Repos that used Both of them:   " + str(len(usedBoth)))


"""
# Remove repos that has less than 500 MRE 
for repo in allRepos["repos"]:
	if repo["MRE"] >= 500:
		allRepos["repos"].remove(repo)

print("\nAnalyzing repos with atleast 500 MRE")
print("Repos that has atleast 500 MRE: " + str(len(allRepos["repos"])))
"""


# ==================================================================================
# Diagram 1
# ==================================================================================
URE_0_10 = 0
URE_10_20 = 0
URE_20_30 = 0
URE_30_40 = 0
URE_40_50 = 0
URE_50_60 = 0
URE_60_70 = 0
URE_70_80 = 0
URE_80_90 = 0
URE_90_100 = 0

for repo in allRepos["repos"]:
	usedLambda_0_10 = False
	usedLambda_10_20 = False
	usedLambda_20_30 = False
	usedLambda_30_40 = False
	usedLambda_40_50 = False
	usedLambda_50_60 = False
	usedLambda_60_70 = False
	usedLambda_70_80 = False
	usedLambda_80_90 = False
	usedLambda_90_100 = False

	for user in repo["contributors"]:
		if user["URE"] >= 0.0 and user["URE"] <= 0.10 and user["lambdas"] > 0:
			usedLambda_0_10 = True
		if user["URE"] > 0.10 and user["URE"] <= 0.20 and user["lambdas"] > 0:
			usedLambda_10_20 = True
		if user["URE"] > 0.20 and user["URE"] <= 0.30 and user["lambdas"] > 0:
			usedLambda_20_30 = True
		if user["URE"] > 0.30 and user["URE"] <= 0.40 and user["lambdas"] > 0:
			usedLambda_30_40 = True
		if user["URE"] > 0.40 and user["URE"] <= 0.50 and user["lambdas"] > 0:
			usedLambda_40_50 = True
		if user["URE"] > 0.50 and user["URE"] <= 0.60 and user["lambdas"] > 0:
			usedLambda_50_60 = True
		if user["URE"] > 0.60 and user["URE"] <= 0.70 and user["lambdas"] > 0:
			usedLambda_60_70 = True
		if user["URE"] > 0.70 and user["URE"] <= 0.80 and user["lambdas"] > 0:
			usedLambda_70_80 = True
		if user["URE"] > 0.80 and user["URE"] <= 0.90 and user["lambdas"] > 0:
			usedLambda_80_90 = True
		if user["URE"] > 0.90  and user["lambdas"] > 0:
			usedLambda_90_100 = True

	if usedLambda_0_10 == True:
		URE_0_10 += 1
	if usedLambda_10_20 == True:
		URE_10_20 += 1
	if usedLambda_20_30 == True:
		URE_20_30 += 1
	if usedLambda_30_40 == True:
		URE_30_40 += 1
	if usedLambda_40_50 == True:
		URE_40_50 += 1
	if usedLambda_50_60 == True:
		URE_50_60 += 1
	if usedLambda_60_70 == True:
		URE_60_70 += 1
	if usedLambda_70_80 == True:
		URE_70_80 += 1
	if usedLambda_80_90 == True:
		URE_80_90 += 1
	if usedLambda_90_100 == True:
		URE_90_100 += 1


URE_0_10_SmartPointers = 0
URE_10_20_SmartPointers = 0
URE_20_30_SmartPointers = 0
URE_30_40_SmartPointers = 0
URE_40_50_SmartPointers = 0
URE_50_60_SmartPointers = 0
URE_60_70_SmartPointers = 0
URE_70_80_SmartPointers = 0
URE_80_90_SmartPointers = 0
URE_90_100_SmartPointers = 0

for repo in allRepos["repos"]:
	usedLambda_0_10 = False
	usedLambda_10_20 = False
	usedLambda_20_30 = False
	usedLambda_30_40 = False
	usedLambda_40_50 = False
	usedLambda_50_60 = False
	usedLambda_60_70 = False
	usedLambda_70_80 = False
	usedLambda_80_90 = False
	usedLambda_90_100 = False

	for user in repo["contributors"]:
		if user["URE"] > 0.0 and user["URE"] <= 0.10 and user["smartpointers"] > 0:
			usedLambda_0_10 = True
		if user["URE"] > 0.10 and user["URE"] <= 0.20 and user["smartpointers"] > 0:
			usedLambda_10_20 = True
		if user["URE"] > 0.20 and user["URE"] <= 0.30 and user["smartpointers"] > 0:
			usedLambda_20_30 = True
		if user["URE"] > 0.30 and user["URE"] <= 0.40 and user["smartpointers"] > 0:
			usedLambda_30_40 = True
		if user["URE"] > 0.40 and user["URE"] <= 0.50 and user["smartpointers"] > 0:
			usedLambda_40_50 = True
		if user["URE"] > 0.50 and user["URE"] <= 0.60 and user["smartpointers"] > 0:
			usedLambda_50_60 = True
		if user["URE"] > 0.60 and user["URE"] <= 0.70 and user["smartpointers"] > 0:
			usedLambda_60_70 = True
		if user["URE"] > 0.70 and user["URE"] <= 0.80 and user["smartpointers"] > 0:
			usedLambda_70_80 = True
		if user["URE"] > 0.80 and user["URE"] <= 0.90 and user["smartpointers"] > 0:
			usedLambda_80_90 = True
		if user["URE"] > 0.90 and user["smartpointers"] > 0:
			usedLambda_90_100 = True

	if usedLambda_0_10 == True:
		URE_0_10_SmartPointers += 1
	if usedLambda_10_20 == True:
		URE_10_20_SmartPointers += 1
	if usedLambda_20_30 == True:
		URE_20_30_SmartPointers += 1
	if usedLambda_30_40 == True:
		URE_30_40_SmartPointers += 1
	if usedLambda_40_50 == True:
		URE_40_50_SmartPointers += 1
	if usedLambda_50_60 == True:
		URE_50_60_SmartPointers += 1
	if usedLambda_60_70 == True:
		URE_60_70_SmartPointers += 1
	if usedLambda_70_80 == True:
		URE_70_80_SmartPointers += 1
	if usedLambda_80_90 == True:
		URE_80_90_SmartPointers += 1
	if usedLambda_90_100 == True:
		URE_90_100_SmartPointers += 1




reposUsingLambdas = [0, 0, 0, 0, 0]
reposUsingSmartPointers = [0, 0, 0, 0, 0]
for repo in allRepos["repos"]:
	alreadyFoundLambda_0_20 = False
	alreadyFoundLambda_20_40 = False
	alreadyFoundLambda_40_60 = False
	alreadyFoundLambda_60_80 = False
	alreadyFoundLambda_80_100 = False
	alreadyFoundSmartpointer_0_20 = False
	alreadyFoundSmartpointer_20_40 = False
	alreadyFoundSmartpointer_40_60 = False
	alreadyFoundSmartpointer_60_80 = False
	alreadyFoundSmartpointer_80_100 = False

	for user in repo["contributors"]:
		if user["URE"] > 0.0 and user["URE"] <= 0.20:
			if user["lambdas"] > 0 and alreadyFoundLambda_0_20 == False:
				reposUsingLambdas[0] += 1
				alreadyFoundLambda_0_20 = True
			if user["smartpointers"] > 0 and alreadyFoundSmartpointer_0_20 == False:
				reposUsingSmartPointers[0] += 1
				alreadyFoundSmartpointer_0_20 = True

		if user["URE"] > 0.20 and user["URE"] <= 0.40:
			if user["lambdas"] > 0 and alreadyFoundLambda_20_40 == False:
				reposUsingLambdas[1] += 1
				alreadyFoundLambda_20_40 = True
			if user["smartpointers"] > 0 and alreadyFoundSmartpointer_20_40 == False:
				reposUsingSmartPointers[1] += 1
				alreadyFoundSmartpointer_20_40 = True

		if user["URE"] > 0.40 and user["URE"] <= 0.60:
			if user["lambdas"] > 0 and alreadyFoundLambda_40_60 == False:
				reposUsingLambdas[2] += 1
				alreadyFoundLambda_40_60 = True
			if user["smartpointers"] > 0 and alreadyFoundSmartpointer_40_60 == False:
				reposUsingSmartPointers[2] += 1
				alreadyFoundSmartpointer_40_60 = True

		if user["URE"] > 0.60 and user["URE"] <= 0.80:
			if user["lambdas"] > 0 and alreadyFoundLambda_60_80 == False:
				reposUsingLambdas[3] += 1
				alreadyFoundLambda_60_80 = True
			if user["smartpointers"] > 0 and alreadyFoundSmartpointer_60_80 == False:
				reposUsingSmartPointers[3] += 1
				alreadyFoundSmartpointer_60_80 = True

		if user["URE"] > 0.80:
			if user["lambdas"] > 0 and alreadyFoundLambda_80_100 == False:
				reposUsingLambdas[4] += 1
				alreadyFoundLambda_80_100 = True
			if user["smartpointers"] > 0 and alreadyFoundSmartpointer_80_100 == False:
				reposUsingSmartPointers[4] += 1
				alreadyFoundSmartpointer_80_100 = True



print("\nDiagram 1: Number of repos where atleast one contributor used atleast one lambda/smartpointer")
print("URE       Lambda    Smart Pointer")
print("0.10      " + str(URE_0_10) + "          " + str(URE_0_10_SmartPointers))
print("0.20      " + str(URE_10_20) + "          " + str(URE_10_20_SmartPointers))
print("0.30      " + str(URE_20_30) + "          " + str(URE_20_30_SmartPointers))
print("0.40      " + str(URE_30_40) + "          " + str(URE_30_40_SmartPointers))
print("0.50      " + str(URE_40_50) + "          " + str(URE_40_50_SmartPointers))
print("0.60      " + str(URE_50_60) + "          " + str(URE_50_60_SmartPointers))
print("0.70      " + str(URE_60_70) + "          " + str(URE_60_70_SmartPointers))
print("0.80      " + str(URE_70_80) + "         " + str(URE_70_80_SmartPointers))
print("0.90      " + str(URE_80_90) + "         " + str(URE_80_90_SmartPointers))
print("0.100     " + str(URE_90_100) + "         " + str(URE_90_100_SmartPointers))
print("")
print("0.20      " + str(reposUsingLambdas[0]) + "           " + str(reposUsingSmartPointers[0]))
print("0.40      " + str(reposUsingLambdas[1]) + "           " + str(reposUsingSmartPointers[1]))
print("0.60      " + str(reposUsingLambdas[2]) + "          " + str(reposUsingSmartPointers[2]))
print("0.80      " + str(reposUsingLambdas[3]) + "          " + str(reposUsingSmartPointers[3]))
print("1.00      " + str(reposUsingLambdas[4]) + "          " + str(reposUsingSmartPointers[4]))







# ==================================================================================
# Diagram 2
# ==================================================================================
totalLambdas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalSmartpointers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totalLambdas_2 = [0, 0, 0, 0, 0]
totalSmartpointers_2 = [0, 0, 0, 0, 0]

for repo in allRepos["repos"]:
	for user in repo["contributors"]:
		if user["URE"] > 0.0 and user["URE"] <= 0.10:
			totalLambdas[0] += user["lambdas"]
			totalSmartpointers[0] += user["smartpointers"]

		if user["URE"] > 0.10 and user["URE"] <= 0.20:
			totalLambdas[1] += user["lambdas"]
			totalSmartpointers[1] += user["smartpointers"]

		if user["URE"] > 0.20 and user["URE"] <= 0.30:
			totalLambdas[2] += user["lambdas"]
			totalSmartpointers[2] += user["smartpointers"]

		if user["URE"] > 0.30 and user["URE"] <= 0.40:
			totalLambdas[3] += user["lambdas"]
			totalSmartpointers[3] += user["smartpointers"]

		if user["URE"] > 0.40 and user["URE"] <= 0.50:
			totalLambdas[4] += user["lambdas"]
			totalSmartpointers[4] += user["smartpointers"]

		if user["URE"] > 0.50 and user["URE"] <= 0.60:
			totalLambdas[5] += user["lambdas"]
			totalSmartpointers[5] += user["smartpointers"]

		if user["URE"] > 0.60 and user["URE"] <= 0.70:
			totalLambdas[6] += user["lambdas"]
			totalSmartpointers[6] += user["smartpointers"]

		if user["URE"] > 0.70 and user["URE"] <= 0.80:
			totalLambdas[7] += user["lambdas"]
			totalSmartpointers[7] += user["smartpointers"]

		if user["URE"] > 0.80 and user["URE"] <= 0.90:
			totalLambdas[8] += user["lambdas"]
			totalSmartpointers[8] += user["smartpointers"]

		if user["URE"] > 0.90:
			totalLambdas[9] += user["lambdas"]
			totalSmartpointers[9] += user["smartpointers"]

		# -------------------------------------------------
		if user["URE"] > 0.0 and user["URE"] <= 0.20:
			totalLambdas_2[0] += user["lambdas"]
			totalSmartpointers_2[0] += user["smartpointers"]

		if user["URE"] > 0.20 and user["URE"] <= 0.40:
			totalLambdas_2[1] += user["lambdas"]
			totalSmartpointers_2[1] += user["smartpointers"]

		if user["URE"] > 0.40 and user["URE"] <= 0.60:
			totalLambdas_2[2] += user["lambdas"]
			totalSmartpointers_2[2] += user["smartpointers"]

		if user["URE"] > 0.60 and user["URE"] <= 0.80:
			totalLambdas_2[3] += user["lambdas"]
			totalSmartpointers_2[3] += user["smartpointers"]

		if user["URE"] > 0.80:
			totalLambdas_2[4] += user["lambdas"]
			totalSmartpointers_2[4] += user["smartpointers"]



print("\n\nDiagram 2: Total number of lambdas / smartpointers used in all repos")
print("URE       Lambdas    Smart Pointers")
print("0.10      " + str(totalLambdas[0]) + "           " + str(totalSmartpointers[0]))
print("0.20      " + str(totalLambdas[1]) + "          " + str(totalSmartpointers[1]))
print("0.30      " + str(totalLambdas[2]) + "          " + str(totalSmartpointers[2]))
print("0.40      " + str(totalLambdas[3]) + "          " + str(totalSmartpointers[3]))
print("0.50      " + str(totalLambdas[4]) + "          " + str(totalSmartpointers[4]))
print("0.60      " + str(totalLambdas[5]) + "          " + str(totalSmartpointers[5]))
print("0.70      " + str(totalLambdas[6]) + "          " + str(totalSmartpointers[6]))
print("0.80      " + str(totalLambdas[7]) + "         " + str(totalSmartpointers[7]))
print("0.90      " + str(totalLambdas[8]) + "         " + str(totalSmartpointers[8]))
print("0.100     " + str(totalLambdas[9]) + "        " + str(totalSmartpointers[9]))
print("")
print("0.20      " + str(totalLambdas_2[0]) + "          " + str(totalSmartpointers_2[0]))
print("0.40      " + str(totalLambdas_2[1]) + "          " + str(totalSmartpointers_2[1]))
print("0.60      " + str(totalLambdas_2[2]) + "         " + str(totalSmartpointers_2[2]))
print("0.80      " + str(totalLambdas_2[3]) + "         " + str(totalSmartpointers_2[3]))
print("1.00      " + str(totalLambdas_2[4]) + "        " + str(totalSmartpointers_2[4]))






# ==================================================================================
# Diagram 3
# ==================================================================================
lambdas_percentages = {
	"URE_0_10": [],
	"URE_10_20": [],
	"URE_20_30": [],
	"URE_30_40": [],
	"URE_40_50": [],
	"URE_50_60": [],
	"URE_60_70": [],
	"URE_70_80": [],
	"URE_80_90": [],
	"URE_90_100": [],

	"URE_0_20": [],
	"URE_20_40": [],
	"URE_40_60": [],
	"URE_60_80": [],
	"URE_80_100": []
}
smartpointers_percentages = {
	"URE_0_10": [],
	"URE_10_20": [],
	"URE_20_30": [],
	"URE_30_40": [],
	"URE_40_50": [],
	"URE_50_60": [],
	"URE_60_70": [],
	"URE_70_80": [],
	"URE_80_90": [],
	"URE_90_100": [],

	"URE_0_20": [],
	"URE_20_40": [],
	"URE_40_60": [],
	"URE_60_80": [],
	"URE_80_100": []
}

for repo in allRepos["repos"]:
	lambdas = repo["total_lambdas"]
	smartpointers = repo["total_smartpointers"]

	for user in repo["contributors"]:
		if user["URE"] > 0.0 and user["URE"] <= 0.10:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_0_10"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_0_10"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.10 and user["URE"] <= 0.20:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_10_20"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_10_20"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.20 and user["URE"] <= 0.30:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_20_30"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_20_30"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.30 and user["URE"] <= 0.40:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_30_40"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_30_40"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.40 and user["URE"] <= 0.50:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_40_50"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_40_50"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.50 and user["URE"] <= 0.60:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_50_60"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_50_60"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.60 and user["URE"] <= 0.70:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_60_70"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_60_70"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.70 and user["URE"] <= 0.80:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_70_80"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_70_80"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.80 and user["URE"] <= 0.90:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_80_90"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_80_90"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.90:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_90_100"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_90_100"].append(user["smartpointers"] / smartpointers)

		# ---------------------------------------------------
		if user["URE"] > 0.0 and user["URE"] <= 0.20:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_0_20"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_0_20"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.20 and user["URE"] <= 0.40:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_20_40"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_20_40"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.40 and user["URE"] <= 0.60:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_40_60"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_40_60"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.60 and user["URE"] <= 0.80:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_60_80"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_60_80"].append(user["smartpointers"] / smartpointers)

		if user["URE"] > 0.80:
			if user["lambdas"] > 0 and lambdas > 0:
				lambdas_percentages["URE_80_100"].append(user["lambdas"] / lambdas)
			if user["smartpointers"] > 0 and smartpointers > 0:
				smartpointers_percentages["URE_80_100"].append(user["smartpointers"] / smartpointers)



SUM = 0
for percantage in lambdas_percentages["URE_0_10"]:
	SUM += percantage
AVG_lambdas_URE_0_10 = SUM / len(lambdas_percentages["URE_0_10"])
SUM = 0
for percantage in lambdas_percentages["URE_10_20"]:
	SUM += percantage
AVG_lambdas_URE_10_20 = SUM / len(lambdas_percentages["URE_10_20"])
SUM = 0
for percantage in lambdas_percentages["URE_20_30"]:
	SUM += percantage
AVG_lambdas_URE_20_30 = SUM / len(lambdas_percentages["URE_20_30"])
SUM = 0
for percantage in lambdas_percentages["URE_30_40"]:
	SUM += percantage
AVG_lambdas_URE_30_40 = SUM / len(lambdas_percentages["URE_30_40"])
SUM = 0
for percantage in lambdas_percentages["URE_40_50"]:
	SUM += percantage
AVG_lambdas_URE_40_50 = SUM / len(lambdas_percentages["URE_40_50"])
SUM = 0
for percantage in lambdas_percentages["URE_50_60"]:
	SUM += percantage
AVG_lambdas_URE_50_60 = SUM / len(lambdas_percentages["URE_50_60"])
SUM = 0
for percantage in lambdas_percentages["URE_60_70"]:
	SUM += percantage
AVG_lambdas_URE_60_70 = SUM / len(lambdas_percentages["URE_60_70"])
SUM = 0
for percantage in lambdas_percentages["URE_70_80"]:
	SUM += percantage
AVG_lambdas_URE_70_80 = SUM / len(lambdas_percentages["URE_70_80"])
SUM = 0
for percantage in lambdas_percentages["URE_80_90"]:
	SUM += percantage
AVG_lambdas_URE_80_90 = SUM / len(lambdas_percentages["URE_80_90"])
SUM = 0
for percantage in lambdas_percentages["URE_90_100"]:
	SUM += percantage
AVG_lambdas_URE_90_100 = SUM / len(lambdas_percentages["URE_90_100"])


SUM = 0
for percantage in smartpointers_percentages["URE_0_10"]:
	SUM += percantage
AVG_smartpointers_URE_0_10 = SUM / len(smartpointers_percentages["URE_0_10"])
SUM = 0
for percantage in smartpointers_percentages["URE_10_20"]:
	SUM += percantage
AVG_smartpointers_URE_10_20 = SUM / len(smartpointers_percentages["URE_10_20"])
SUM = 0
for percantage in smartpointers_percentages["URE_20_30"]:
	SUM += percantage
AVG_smartpointers_URE_20_30 = SUM / len(smartpointers_percentages["URE_20_30"])
SUM = 0
for percantage in smartpointers_percentages["URE_30_40"]:
	SUM += percantage
AVG_smartpointers_URE_30_40 = SUM / len(smartpointers_percentages["URE_30_40"])
SUM = 0
for percantage in smartpointers_percentages["URE_40_50"]:
	SUM += percantage
AVG_smartpointers_URE_40_50 = SUM / len(smartpointers_percentages["URE_40_50"])
SUM = 0
for percantage in smartpointers_percentages["URE_50_60"]:
	SUM += percantage
AVG_smartpointers_URE_50_60 = SUM / len(smartpointers_percentages["URE_50_60"])
SUM = 0
for percantage in smartpointers_percentages["URE_60_70"]:
	SUM += percantage
AVG_smartpointers_URE_60_70 = SUM / len(smartpointers_percentages["URE_60_70"])
SUM = 0
for percantage in smartpointers_percentages["URE_70_80"]:
	SUM += percantage
AVG_smartpointers_URE_70_80 = SUM / len(smartpointers_percentages["URE_70_80"])
SUM = 0
for percantage in smartpointers_percentages["URE_80_90"]:
	SUM += percantage
AVG_smartpointers_URE_80_90 = SUM / len(smartpointers_percentages["URE_80_90"])
SUM = 0
for percantage in smartpointers_percentages["URE_90_100"]:
	SUM += percantage
AVG_smartpointers_URE_90_100 = SUM / len(smartpointers_percentages["URE_90_100"])

# --------------------------
SUM = 0
for percantage in lambdas_percentages["URE_0_20"]:
	SUM += percantage
AVG_lambdas_URE_0_20 = SUM / len(lambdas_percentages["URE_0_20"])
SUM = 0
for percantage in lambdas_percentages["URE_20_40"]:
	SUM += percantage
AVG_lambdas_URE_20_40 = SUM / len(lambdas_percentages["URE_20_40"])
SUM = 0
for percantage in lambdas_percentages["URE_40_60"]:
	SUM += percantage
AVG_lambdas_URE_40_60 = SUM / len(lambdas_percentages["URE_40_60"])
SUM = 0
for percantage in lambdas_percentages["URE_60_80"]:
	SUM += percantage
AVG_lambdas_URE_60_80 = SUM / len(lambdas_percentages["URE_60_80"])
SUM = 0
for percantage in lambdas_percentages["URE_80_100"]:
	SUM += percantage
AVG_lambdas_URE_80_100 = SUM / len(lambdas_percentages["URE_80_100"])

SUM = 0
for percantage in smartpointers_percentages["URE_0_20"]:
	SUM += percantage
AVG_smartpointers_URE_0_20 = SUM / len(smartpointers_percentages["URE_0_20"])
SUM = 0
for percantage in smartpointers_percentages["URE_20_40"]:
	SUM += percantage
AVG_smartpointers_URE_20_40 = SUM / len(smartpointers_percentages["URE_20_40"])
SUM = 0
for percantage in smartpointers_percentages["URE_40_60"]:
	SUM += percantage
AVG_smartpointers_URE_40_60 = SUM / len(smartpointers_percentages["URE_40_60"])
SUM = 0
for percantage in smartpointers_percentages["URE_60_80"]:
	SUM += percantage
AVG_smartpointers_URE_60_80 = SUM / len(smartpointers_percentages["URE_60_80"])
SUM = 0
for percantage in smartpointers_percentages["URE_80_100"]:
	SUM += percantage
AVG_smartpointers_URE_80_100 = SUM / len(smartpointers_percentages["URE_80_100"])


print("\n\nDiagram 3: Average distribution of lambda / smartpointer usage for all repos")
print("URE       Lambdas    Smart Pointers")
print(f"0.10      {(AVG_lambdas_URE_0_10 * 100):.2f}%           {(AVG_smartpointers_URE_0_10 * 100):.2f}%")
print(f"0.20      {(AVG_lambdas_URE_10_20 * 100):.2f}%           {(AVG_smartpointers_URE_10_20 * 100):.2f}%")
print(f"0.30      {(AVG_lambdas_URE_20_30 * 100):.2f}%           {(AVG_smartpointers_URE_20_30 * 100):.2f}%")
print(f"0.40      {(AVG_lambdas_URE_30_40 * 100):.2f}%           {(AVG_smartpointers_URE_30_40 * 100):.2f}%")
print(f"0.50      {(AVG_lambdas_URE_40_50 * 100):.2f}%           {(AVG_smartpointers_URE_40_50 * 100):.2f}%")
print(f"0.60      {(AVG_lambdas_URE_50_60 * 100):.2f}%           {(AVG_smartpointers_URE_50_60 * 100):.2f}%")
print(f"0.70      {(AVG_lambdas_URE_60_70 * 100):.2f}%           {(AVG_smartpointers_URE_60_70 * 100):.2f}%")
print(f"0.80      {(AVG_lambdas_URE_70_80 * 100):.2f}%           {(AVG_smartpointers_URE_70_80 * 100):.2f}%")
print(f"0.90      {(AVG_lambdas_URE_80_90 * 100):.2f}%           {(AVG_smartpointers_URE_80_90 * 100):.2f}%")
print(f"1.00     {(AVG_lambdas_URE_90_100 * 100):.2f}%          {(AVG_smartpointers_URE_90_100 * 100):.2f}%")
print("")
print(f"0.20      {(AVG_lambdas_URE_0_20 * 100):.2f}%           {(AVG_smartpointers_URE_0_20 * 100):.2f}%")
print(f"0.40      {(AVG_lambdas_URE_20_40 * 100):.2f}%           {(AVG_smartpointers_URE_20_40 * 100):.2f}%")
print(f"0.60      {(AVG_lambdas_URE_40_60 * 100):.2f}%           {(AVG_smartpointers_URE_40_60 * 100):.2f}%")
print(f"0.80      {(AVG_lambdas_URE_60_80 * 100):.2f}%           {(AVG_smartpointers_URE_60_80 * 100):.2f}%")
print(f"1.00     {(AVG_lambdas_URE_80_100 * 100):.2f}%          {(AVG_smartpointers_URE_80_100 * 100):.2f}%")







# ==================================================================================
# Diagram 4
# ==================================================================================
lambdas_percentages["URE_0_10"].sort()
lambdas_percentages["URE_10_20"].sort()
lambdas_percentages["URE_20_30"].sort()
lambdas_percentages["URE_30_40"].sort()
lambdas_percentages["URE_40_50"].sort()
lambdas_percentages["URE_50_60"].sort()
lambdas_percentages["URE_60_70"].sort()
lambdas_percentages["URE_70_80"].sort()
lambdas_percentages["URE_80_90"].sort()
lambdas_percentages["URE_90_100"].sort()
lambdas_percentages["URE_0_20"].sort()
lambdas_percentages["URE_20_40"].sort()
lambdas_percentages["URE_40_60"].sort()
lambdas_percentages["URE_60_80"].sort()
lambdas_percentages["URE_80_100"].sort()

smartpointers_percentages["URE_0_10"].sort()
smartpointers_percentages["URE_10_20"].sort()
smartpointers_percentages["URE_20_30"].sort()
smartpointers_percentages["URE_30_40"].sort()
smartpointers_percentages["URE_40_50"].sort()
smartpointers_percentages["URE_50_60"].sort()
smartpointers_percentages["URE_60_70"].sort()
smartpointers_percentages["URE_70_80"].sort()
smartpointers_percentages["URE_80_90"].sort()
smartpointers_percentages["URE_90_100"].sort()
smartpointers_percentages["URE_0_20"].sort()
smartpointers_percentages["URE_20_40"].sort()
smartpointers_percentages["URE_40_60"].sort()
smartpointers_percentages["URE_60_80"].sort()
smartpointers_percentages["URE_80_100"].sort()

MEAN_lambdas_URE_0_10 = lambdas_percentages["URE_0_10"][ int(len(lambdas_percentages["URE_0_10"])/2) ]
MEAN_lambdas_URE_10_20 = lambdas_percentages["URE_10_20"][ int(len(lambdas_percentages["URE_10_20"])/2) ]
MEAN_lambdas_URE_20_30 = lambdas_percentages["URE_20_30"][ int(len(lambdas_percentages["URE_20_30"])/2) ]
MEAN_lambdas_URE_30_40 = lambdas_percentages["URE_30_40"][ int(len(lambdas_percentages["URE_30_40"])/2) ]
MEAN_lambdas_URE_40_50 = lambdas_percentages["URE_40_50"][ int(len(lambdas_percentages["URE_40_50"])/2) ]
MEAN_lambdas_URE_50_60 = lambdas_percentages["URE_50_60"][ int(len(lambdas_percentages["URE_50_60"])/2) ]
MEAN_lambdas_URE_60_70 = lambdas_percentages["URE_60_70"][ int(len(lambdas_percentages["URE_60_70"])/2) ]
MEAN_lambdas_URE_70_80 = lambdas_percentages["URE_70_80"][ int(len(lambdas_percentages["URE_70_80"])/2) ]
MEAN_lambdas_URE_80_90 = lambdas_percentages["URE_80_90"][ int(len(lambdas_percentages["URE_80_90"])/2) ]
MEAN_lambdas_URE_90_100 = lambdas_percentages["URE_90_100"][ int(len(lambdas_percentages["URE_90_100"])/2) ]

MEAN_smartpointers_URE_0_10 = smartpointers_percentages["URE_0_10"][ int(len(smartpointers_percentages["URE_0_10"])/2) ]
MEAN_smartpointers_URE_10_20 = smartpointers_percentages["URE_10_20"][ int(len(smartpointers_percentages["URE_10_20"])/2) ]
MEAN_smartpointers_URE_20_30 = smartpointers_percentages["URE_20_30"][ int(len(smartpointers_percentages["URE_20_30"])/2) ]
MEAN_smartpointers_URE_30_40 = smartpointers_percentages["URE_30_40"][ int(len(smartpointers_percentages["URE_30_40"])/2) ]
MEAN_smartpointers_URE_40_50 = smartpointers_percentages["URE_40_50"][ int(len(smartpointers_percentages["URE_40_50"])/2) ]
MEAN_smartpointers_URE_50_60 = smartpointers_percentages["URE_50_60"][ int(len(smartpointers_percentages["URE_50_60"])/2) ]
MEAN_smartpointers_URE_60_70 = smartpointers_percentages["URE_60_70"][ int(len(smartpointers_percentages["URE_60_70"])/2) ]
MEAN_smartpointers_URE_70_80 = smartpointers_percentages["URE_70_80"][ int(len(smartpointers_percentages["URE_70_80"])/2) ]
MEAN_smartpointers_URE_80_90 = smartpointers_percentages["URE_80_90"][ int(len(smartpointers_percentages["URE_80_90"])/2) ]
MEAN_smartpointers_URE_90_100 = smartpointers_percentages["URE_90_100"][ int(len(smartpointers_percentages["URE_90_100"])/2) ]

# --------------------------------------------------------------
MEAN_lambdas_URE_0_20 = lambdas_percentages["URE_0_20"][ int(len(lambdas_percentages["URE_0_20"])/2) ]
MEAN_lambdas_URE_20_40 = lambdas_percentages["URE_20_40"][ int(len(lambdas_percentages["URE_20_40"])/2)]
MEAN_lambdas_URE_40_60 = lambdas_percentages["URE_40_60"][ int(len(lambdas_percentages["URE_40_60"])/2)]
MEAN_lambdas_URE_60_80 = lambdas_percentages["URE_60_80"][ int(len(lambdas_percentages["URE_60_80"])/2)]
MEAN_lambdas_URE_80_100 = lambdas_percentages["URE_80_100"][ int(len(lambdas_percentages["URE_80_100"])/2)]

MEAN_smartpointers_URE_0_20 = smartpointers_percentages["URE_0_20"][ int(len(smartpointers_percentages["URE_0_20"])/2) ]
MEAN_smartpointers_URE_20_40 = smartpointers_percentages["URE_20_40"][ int(len(smartpointers_percentages["URE_20_40"])/2)]
MEAN_smartpointers_URE_40_60 = smartpointers_percentages["URE_40_60"][ int(len(smartpointers_percentages["URE_40_60"])/2)]
MEAN_smartpointers_URE_60_80 = smartpointers_percentages["URE_60_80"][ int(len(smartpointers_percentages["URE_60_80"])/2)]
MEAN_smartpointers_URE_80_100 = smartpointers_percentages["URE_80_100"][ int(len(smartpointers_percentages["URE_80_100"])/2)]


print("\n\nDiagram 4: Mean distribution of lambda / smartpointer usage for all repos")
print("URE       Lambdas    Smart Pointers")
print(f"0.10      {(MEAN_lambdas_URE_0_10 * 100):.4f}%           {(MEAN_smartpointers_URE_0_10 * 100):.4f}%")
print(f"0.20      {(MEAN_lambdas_URE_10_20 * 100):.4f}%           {(MEAN_smartpointers_URE_10_20 * 100):.4f}%")
print(f"0.30      {(MEAN_lambdas_URE_20_30 * 100):.4f}%           {(MEAN_smartpointers_URE_20_30 * 100):.4f}%")
print(f"0.40      {(MEAN_lambdas_URE_30_40 * 100):.4f}%           {(MEAN_smartpointers_URE_30_40 * 100):.4f}%")
print(f"0.50      {(MEAN_lambdas_URE_40_50 * 100):.4f}%           {(MEAN_smartpointers_URE_40_50 * 100):.4f}%")
print(f"0.60      {(MEAN_lambdas_URE_50_60 * 100):.4f}%           {(MEAN_smartpointers_URE_50_60 * 100):.4f}%")
print(f"0.70      {(MEAN_lambdas_URE_60_70 * 100):.4f}%           {(MEAN_smartpointers_URE_60_70 * 100):.4f}%")
print(f"0.80      {(MEAN_lambdas_URE_70_80 * 100):.4f}%           {(MEAN_smartpointers_URE_70_80 * 100):.4f}%")
print(f"0.90      {(MEAN_lambdas_URE_80_90 * 100):.4f}%           {(MEAN_smartpointers_URE_80_90 * 100):.4f}%")
print(f"1.00      {(MEAN_lambdas_URE_90_100 * 100):.4f}%           {(MEAN_smartpointers_URE_90_100 * 100):.4f}%")
print("")
print(f"0.20      {(MEAN_lambdas_URE_0_20 * 100):.4f}%           {(MEAN_smartpointers_URE_0_20 * 100):.4f}%")
print(f"0.40      {(MEAN_lambdas_URE_20_40 * 100):.4f}%           {(MEAN_smartpointers_URE_20_40 * 100):.4f}%")
print(f"0.60      {(MEAN_lambdas_URE_40_60 * 100):.4f}%           {(MEAN_smartpointers_URE_40_60 * 100):.4f}%")
print(f"0.80      {(MEAN_lambdas_URE_60_80 * 100):.4f}%           {(MEAN_smartpointers_URE_60_80 * 100):.4f}%")
print(f"1.00      {(MEAN_lambdas_URE_80_100 * 100):.4f}%           {(MEAN_smartpointers_URE_80_100 * 100):.4f}%")


