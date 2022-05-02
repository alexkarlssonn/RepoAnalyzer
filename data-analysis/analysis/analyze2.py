import json
from statistics import median
from statistics import pstdev




allRepos = {}
with open("all_analyzed_repos.json", "r") as fromFile:
	allRepos = json.load(fromFile)
	print("\n" + str(len(allRepos['repos'])) + " repos was loaded from the file")

for repo in allRepos["repos"]:
	if repo["total_contributors"] < 10:
		allRepos["repos"].remove(repo)
print("\nOnly analyzing repos with atleast 10 contributors")

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

print("\nTotal repos:                    " + str(len(allRepos["repos"])))
print("Repos that used Lambdas:        " + str(len(usedLambda)))
print("Repos that used Smart Pointers: " + str(len(usedSmartPointer)))
print("Repos that used Both of them:   " + str(len(usedBoth)))






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

print("\nNumber of repos where atleast one lambda/smart pointer was used")
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










Lambda = {
	"total_1": [], "total_2": [], "total_3": [], "total_4": [], "total_5": [], "total_6": [], "total_7": [], "total_8": [], "total_9": [], "total_10": [],
	"dist_1": [], "dist_2": [], "dist_3": [], "dist_4": [], "dist_5": [], "dist_6": [], "dist_7": [], "dist_8": [], "dist_9": [], "dist_10": []
}
Smartpointer = {
	"total_1": [], "total_2": [], "total_3": [], "total_4": [], "total_5": [], "total_6": [], "total_7": [], "total_8": [], "total_9": [], "total_10": [],
	"dist_1": [], "dist_2": [], "dist_3": [], "dist_4": [], "dist_5": [], "dist_6": [], "dist_7": [], "dist_8": [], "dist_9": [], "dist_10": []
}

# Count the total number of lambdas and smart pointers used by each URE group
# Also count the distribution of lambdas and smart pointers between URE groups
for repo in allRepos["repos"]:
	lambdas = repo["total_lambdas"]
	smartpointers = repo["total_smartpointers"]
	for user in repo["contributors"]:

		if user["URE"] > 0.0 and user["URE"] <= 0.10:
			Lambda["total_1"].append(user["lambdas"])
			Smartpointer["total_1"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_1"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_1"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.10 and user["URE"] <= 0.20:
			Lambda["total_2"].append(user["lambdas"])
			Smartpointer["total_2"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_2"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_2"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.20 and user["URE"] <= 0.30:
			Lambda["total_3"].append(user["lambdas"])
			Smartpointer["total_3"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_3"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_3"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.30 and user["URE"] <= 0.40:
			Lambda["total_4"].append(user["lambdas"])
			Smartpointer["total_4"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_4"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_4"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.40 and user["URE"] <= 0.50:
			Lambda["total_5"].append(user["lambdas"])
			Smartpointer["total_5"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_5"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_5"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.50 and user["URE"] <= 0.60:
			Lambda["total_6"].append(user["lambdas"])
			Smartpointer["total_6"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_6"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_6"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.60 and user["URE"] <= 0.70:
			Lambda["total_7"].append(user["lambdas"])
			Smartpointer["total_7"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_7"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_7"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.70 and user["URE"] <= 0.80:
			Lambda["total_8"].append(user["lambdas"])
			Smartpointer["total_8"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_8"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_8"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.80 and user["URE"] <= 0.90:
			Lambda["total_9"].append(user["lambdas"])
			Smartpointer["total_9"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_9"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_9"].append(float(user["smartpointers"] / smartpointers))

		if user["URE"] > 0.90:
			Lambda["total_10"].append(user["lambdas"])
			Smartpointer["total_10"].append(user["smartpointers"])
			if user["lambdas"] > 0 and lambdas > 0:
				Lambda["dist_10"].append(float(user["lambdas"] / lambdas))
			if user["smartpointers"] > 0 and smartpointers > 0:
				Smartpointer["dist_10"].append(float(user["smartpointers"] / smartpointers))

print("\n+----------------------------------------------------------------------------------------------------------------------+")
print("| Total lambdas used                                                                                                   |")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")
print("|  URE  |   Total   |   Min   |    Max    |           Avg            |          Median          |          SD          |")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")
print("| 0.10  |       " + str(sum(Lambda["total_1"])) + " |       " + str(min(Lambda["total_1"])) + " |       " + str(max(Lambda["total_1"])) + " |       " + str( sum(Lambda["total_1"]) / len(Lambda["total_1"]) ) + " |                      " + str(float(median(Lambda["total_1"]))) + " |    " + str(pstdev(Lambda["total_1"])) + " |")
print("| 0.20  |       " + str(sum(Lambda["total_2"])) + " |       " + str(min(Lambda["total_2"])) + " |       " + str(max(Lambda["total_2"])) + " |       " + str( sum(Lambda["total_2"]) / len(Lambda["total_2"]) ) + " |                      " + str(float(median(Lambda["total_2"]))) + " |    " + str(pstdev(Lambda["total_2"])) + " |")
print("| 0.30  |      " + str(sum(Lambda["total_3"])) + " |       " + str(min(Lambda["total_3"])) + " |       " + str(max(Lambda["total_3"])) + " |       " + str( sum(Lambda["total_3"]) / len(Lambda["total_3"]) ) + " |                      " + str(float(median(Lambda["total_3"]))) + " |   " + str(pstdev(Lambda["total_3"])) + " |")
print("| 0.40  |      " + str(sum(Lambda["total_4"])) + " |       " + str(min(Lambda["total_4"])) + " |       " + str(max(Lambda["total_4"])) + " |        " + str( sum(Lambda["total_4"]) / len(Lambda["total_4"]) ) + " |                      " + str(float(median(Lambda["total_4"]))) + " |    " + str(pstdev(Lambda["total_4"])) + " |")
print("| 0.50  |      " + str(sum(Lambda["total_5"])) + " |       " + str(min(Lambda["total_5"])) + " |      " + str(max(Lambda["total_5"])) + " |       " + str( sum(Lambda["total_5"]) / len(Lambda["total_5"]) ) + " |                      " + str(float(median(Lambda["total_5"]))) + " |    " + str(pstdev(Lambda["total_5"])) + " |")
print("| 0.60  |      " + str(sum(Lambda["total_6"])) + " |       " + str(min(Lambda["total_6"])) + " |       " + str(max(Lambda["total_6"])) + " |       " + str( sum(Lambda["total_6"]) / len(Lambda["total_6"]) ) + " |                      " + str(float(median(Lambda["total_6"]))) + " |    " + str(pstdev(Lambda["total_6"])) + " |")
print("| 0.70  |      " + str(sum(Lambda["total_7"])) + " |       " + str(min(Lambda["total_7"])) + " |       " + str(max(Lambda["total_7"])) + " |        " + str( sum(Lambda["total_7"]) / len(Lambda["total_7"]) ) + " |                      " + str(float(median(Lambda["total_7"]))) + " |    " + str(pstdev(Lambda["total_7"])) + " |")
print("| 0.80  |     " + str(sum(Lambda["total_8"])) + " |       " + str(min(Lambda["total_8"])) + " |      " + str(max(Lambda["total_8"])) + " |       " + str( sum(Lambda["total_8"]) / len(Lambda["total_8"]) ) + " |                      " + str(float(median(Lambda["total_8"]))) + " |    " + str(pstdev(Lambda["total_8"])) + " |")
print("| 0.90  |     " + str(sum(Lambda["total_9"])) + " |       " + str(min(Lambda["total_9"])) + " |      " + str(max(Lambda["total_9"])) + " |       " + str( sum(Lambda["total_9"]) / len(Lambda["total_9"]) ) + " |                      " + str(float(median(Lambda["total_9"]))) + " |   " + str(pstdev(Lambda["total_9"])) + " |")
print("| 1.00  |    " + str(sum(Lambda["total_10"])) + " |       " + str(min(Lambda["total_10"])) + " |     " + str(max(Lambda["total_10"])) + " |       " + str( sum(Lambda["total_10"]) / len(Lambda["total_10"]) ) + " |                      " + str(float(median(Lambda["total_10"]))) + " |    " + str(pstdev(Lambda["total_10"])) + " |")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")
print("| Total smart pointers used                                                                                            |")
print("+----------------------------------------------------------------------------------------------------------------------+")
print("|  URE  |   Total   |   Min   |    Max    |           Avg            |          Median          |          SD          |")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")
print("| 0.10  |      " + str(sum(Smartpointer["total_1"])) + " |       " + str(min(Smartpointer["total_1"])) + " |       " + str(max(Smartpointer["total_1"])) + " |       " + str( sum(Smartpointer["total_1"]) / len(Smartpointer["total_1"]) ) + " |                      " + str(float(median(Smartpointer["total_1"]))) + " |   " + str(pstdev(Smartpointer["total_1"])) + " |")
print("| 0.20  |      " + str(sum(Smartpointer["total_2"])) + " |       " + str(min(Smartpointer["total_2"])) + " |      " + str(max(Smartpointer["total_2"])) + " |       " + str( sum(Smartpointer["total_2"]) / len(Smartpointer["total_2"]) ) + " |                      " + str(float(median(Smartpointer["total_2"]))) + " |    " + str(pstdev(Smartpointer["total_2"])) + " |")
print("| 0.30  |      " + str(sum(Smartpointer["total_3"])) + " |       " + str(min(Smartpointer["total_3"])) + " |      " + str(max(Smartpointer["total_3"])) + " |       " + str( sum(Smartpointer["total_3"]) / len(Smartpointer["total_3"]) ) + " |                      " + str(float(median(Smartpointer["total_3"]))) + " |     " + str(pstdev(Smartpointer["total_3"])) + " |")
print("| 0.40  |      " + str(sum(Smartpointer["total_4"])) + " |       " + str(min(Smartpointer["total_4"])) + " |      " + str(max(Smartpointer["total_4"])) + " |        " + str( sum(Smartpointer["total_4"]) / len(Smartpointer["total_4"]) ) + " |                      " + str(float(median(Smartpointer["total_4"]))) + " |     " + str(pstdev(Smartpointer["total_4"])) + " |")
print("| 0.50  |     " + str(sum(Smartpointer["total_5"])) + " |       " + str(min(Smartpointer["total_5"])) + " |      " + str(max(Smartpointer["total_5"])) + " |        " + str( sum(Smartpointer["total_5"]) / len(Smartpointer["total_5"]) ) + " |                      " + str(float(median(Smartpointer["total_5"]))) + " |    " + str(pstdev(Smartpointer["total_5"])) + " |")
print("| 0.60  |     " + str(sum(Smartpointer["total_6"])) + " |       " + str(min(Smartpointer["total_6"])) + " |      " + str(max(Smartpointer["total_6"])) + " |       " + str( sum(Smartpointer["total_6"]) / len(Smartpointer["total_6"]) ) + " |                      " + str(float(median(Smartpointer["total_6"]))) + " |   " + str(pstdev(Smartpointer["total_6"])) + " |")
print("| 0.70  |     " + str(sum(Smartpointer["total_7"])) + " |       " + str(min(Smartpointer["total_7"])) + " |      " + str(max(Smartpointer["total_7"])) + " |       " + str( sum(Smartpointer["total_7"]) / len(Smartpointer["total_7"]) ) + " |                      " + str(float(median(Smartpointer["total_7"]))) + " |   " + str(pstdev(Smartpointer["total_7"])) + " |")
print("| 0.80  |     " + str(sum(Smartpointer["total_8"])) + " |       " + str(min(Smartpointer["total_8"])) + " |      " + str(max(Smartpointer["total_8"])) + " |        " + str( sum(Smartpointer["total_8"]) / len(Smartpointer["total_8"]) ) + " |                      " + str(float(median(Smartpointer["total_8"]))) + " |    " + str(pstdev(Smartpointer["total_8"])) + " |")
print("| 0.90  |     " + str(sum(Smartpointer["total_9"])) + " |       " + str(min(Smartpointer["total_9"])) + " |     " + str(max(Smartpointer["total_9"])) + " |        " + str( sum(Smartpointer["total_9"]) / len(Smartpointer["total_9"]) ) + " |                      " + str(float(median(Smartpointer["total_9"]))) + " |    " + str(pstdev(Smartpointer["total_9"])) + " |")
print("| 1.00  |    " + str(sum(Smartpointer["total_10"])) + " |       " + str(min(Smartpointer["total_10"])) + " |     " + str(max(Smartpointer["total_10"])) + " |        " + str( sum(Smartpointer["total_10"]) / len(Smartpointer["total_10"]) ) + " |                      " + str(float(median(Smartpointer["total_10"]))) + " |   " + str(pstdev(Smartpointer["total_10"])) + " |")
print("+-------+-----------+---------+-----------+--------------------------+--------------------------+----------------------+")






print("\n+-------------------------------------------------------------------+")
print("| Distribution of lambdas between URE groups                        |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print("|  URE  |    Min    |    Max    |    Avg    |   Median  |     SD    |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print(f"| 0.10  |     {100*min(Lambda['dist_1']):.2f}% |    {100*max(Lambda['dist_1']):.2f}% |     {100*(sum(Lambda['dist_1'])/len(Lambda['dist_1'])):.2f}% |     {100*(float(median(Lambda['dist_1']))):.2f}% |     {100*pstdev(Lambda['dist_1']):.2f}% |")
print(f"| 0.20  |     {100*min(Lambda['dist_2']):.2f}% |   {100*max(Lambda['dist_2']):.2f}% |     {100*(sum(Lambda['dist_2'])/len(Lambda['dist_2'])):.2f}% |     {100*(float(median(Lambda['dist_2']))):.2f}% |    {100*pstdev(Lambda['dist_2']):.2f}% |")
print(f"| 0.30  |     {100*min(Lambda['dist_3']):.2f}% |    {100*max(Lambda['dist_3']):.2f}% |     {100*(sum(Lambda['dist_3'])/len(Lambda['dist_3'])):.2f}% |     {100*(float(median(Lambda['dist_3']))):.2f}% |     {100*pstdev(Lambda['dist_3']):.2f}% |")
print(f"| 0.40  |     {100*min(Lambda['dist_4']):.2f}% |    {100*max(Lambda['dist_4']):.2f}% |     {100*(sum(Lambda['dist_4'])/len(Lambda['dist_4'])):.2f}% |     {100*(float(median(Lambda['dist_4']))):.2f}% |     {100*pstdev(Lambda['dist_4']):.2f}% |")
print(f"| 0.50  |     {100*min(Lambda['dist_5']):.2f}% |   {100*max(Lambda['dist_5']):.2f}% |     {100*(sum(Lambda['dist_5'])/len(Lambda['dist_5'])):.2f}% |     {100*(float(median(Lambda['dist_5']))):.2f}% |    {100*pstdev(Lambda['dist_5']):.2f}% |")
print(f"| 0.60  |     {100*min(Lambda['dist_6']):.2f}% |   {100*max(Lambda['dist_6']):.2f}% |     {100*(sum(Lambda['dist_6'])/len(Lambda['dist_6'])):.2f}% |     {100*(float(median(Lambda['dist_6']))):.2f}% |    {100*pstdev(Lambda['dist_6']):.2f}% |")
print(f"| 0.70  |     {100*min(Lambda['dist_7']):.2f}% |    {100*max(Lambda['dist_7']):.2f}% |     {100*(sum(Lambda['dist_7'])/len(Lambda['dist_7'])):.2f}% |     {100*(float(median(Lambda['dist_7']))):.2f}% |     {100*pstdev(Lambda['dist_7']):.2f}% |")
print(f"| 0.80  |     {100*min(Lambda['dist_8']):.2f}% |   {100*max(Lambda['dist_8']):.2f}% |     {100*(sum(Lambda['dist_8'])/len(Lambda['dist_8'])):.2f}% |     {100*(float(median(Lambda['dist_8']))):.2f}% |    {100*pstdev(Lambda['dist_8']):.2f}% |")
print(f"| 0.90  |     {100*min(Lambda['dist_9']):.2f}% |   {100*max(Lambda['dist_9']):.2f}% |     {100*(sum(Lambda['dist_9'])/len(Lambda['dist_9'])):.2f}% |     {100*(float(median(Lambda['dist_9']))):.2f}% |    {100*pstdev(Lambda['dist_9']):.2f}% |")
print(f"| 1.00  |     {100*min(Lambda['dist_10']):.2f}% |   {100*max(Lambda['dist_10']):.2f}% |    {100*(sum(Lambda['dist_10'])/len(Lambda['dist_10'])):.2f}% |     {100*(float(median(Lambda['dist_10']))):.2f}% |    {100*pstdev(Lambda['dist_10']):.2f}% |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print("| Distribution of smart pointers between URE groups                 |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print("|  URE  |    Min    |    Max    |    Avg    |   Median  |     SD    |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")
print(f"| 0.10  |     {100*min(Smartpointer['dist_1']):.2f}% |   {100*max(Smartpointer['dist_1']):.2f}% |     {100*(sum(Smartpointer['dist_1'])/len(Smartpointer['dist_1'])):.2f}% |     {100*(float(median(Smartpointer['dist_1']))):.2f}% |    {100*pstdev(Smartpointer['dist_1']):.2f}% |")
print(f"| 0.20  |     {100*min(Smartpointer['dist_2']):.2f}% |    {100*max(Smartpointer['dist_2']):.2f}% |     {100*(sum(Smartpointer['dist_2'])/len(Smartpointer['dist_2'])):.2f}% |     {100*(float(median(Smartpointer['dist_2']))):.2f}% |    {100*pstdev(Smartpointer['dist_2']):.2f}% |")
print(f"| 0.30  |     {100*min(Smartpointer['dist_3']):.2f}% |   {100*max(Smartpointer['dist_3']):.2f}% |     {100*(sum(Smartpointer['dist_3'])/len(Smartpointer['dist_3'])):.2f}% |     {100*(float(median(Smartpointer['dist_3']))):.2f}% |    {100*pstdev(Smartpointer['dist_3']):.2f}% |")
print(f"| 0.40  |     {100*min(Smartpointer['dist_4']):.2f}% |    {100*max(Smartpointer['dist_4']):.2f}% |     {100*(sum(Smartpointer['dist_4'])/len(Smartpointer['dist_4'])):.2f}% |     {100*(float(median(Smartpointer['dist_4']))):.2f}% |     {100*pstdev(Smartpointer['dist_4']):.2f}% |")
print(f"| 0.50  |     {100*min(Smartpointer['dist_5']):.2f}% |    {100*max(Smartpointer['dist_5']):.2f}% |     {100*(sum(Smartpointer['dist_5'])/len(Smartpointer['dist_5'])):.2f}% |     {100*(float(median(Smartpointer['dist_5']))):.2f}% |     {100*pstdev(Smartpointer['dist_5']):.2f}% |")
print(f"| 0.60  |     {100*min(Smartpointer['dist_6']):.2f}% |   {100*max(Smartpointer['dist_6']):.2f}% |     {100*(sum(Smartpointer['dist_6'])/len(Smartpointer['dist_6'])):.2f}% |     {100*(float(median(Smartpointer['dist_6']))):.2f}% |    {100*pstdev(Smartpointer['dist_6']):.2f}% |")
print(f"| 0.70  |     {100*min(Smartpointer['dist_7']):.2f}% |   {100*max(Smartpointer['dist_7']):.2f}% |     {100*(sum(Smartpointer['dist_7'])/len(Smartpointer['dist_7'])):.2f}% |     {100*(float(median(Smartpointer['dist_7']))):.2f}% |    {100*pstdev(Smartpointer['dist_7']):.2f}% |")
print(f"| 0.80  |     {100*min(Smartpointer['dist_8']):.2f}% |    {100*max(Smartpointer['dist_8']):.2f}% |     {100*(sum(Smartpointer['dist_8'])/len(Smartpointer['dist_8'])):.2f}% |     {100*(float(median(Smartpointer['dist_8']))):.2f}% |    {100*pstdev(Smartpointer['dist_8']):.2f}% |")
print(f"| 0.90  |     {100*min(Smartpointer['dist_9']):.2f}% |   {100*max(Smartpointer['dist_9']):.2f}% |     {100*(sum(Smartpointer['dist_9'])/len(Smartpointer['dist_9'])):.2f}% |     {100*(float(median(Smartpointer['dist_9']))):.2f}% |    {100*pstdev(Smartpointer['dist_9']):.2f}% |")
print(f"| 1.00  |     {100*min(Smartpointer['dist_10']):.2f}% |   {100*max(Smartpointer['dist_10']):.2f}% |    {100*(sum(Smartpointer['dist_10'])/len(Smartpointer['dist_10'])):.2f}% |     {100*(float(median(Smartpointer['dist_10']))):.2f}% |    {100*pstdev(Smartpointer['dist_10']):.2f}% |")
print("+-------+-----------+-----------+-----------+-----------+-----------+")


















