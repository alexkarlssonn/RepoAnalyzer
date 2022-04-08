
#include "definitions.h"
#include "libs/cJSON.h"
#include <string>
#include <vector>
#include <iostream>


/**
 * ------------------------------------------------------------------------------------------------
 * Converts the results from the analyzed repository into a cJSON object.
 * The cJSON object that gets returned on success needs to be freed manually later
 * 
 * Returns NULL on failure, and an allocated cJSON object on success
 * ------------------------------------------------------------------------------------------------ 
 */
cJSON* convertToJSON(const std::string& repoName, int MRE, const std::vector<AuthorData>& all_authors)
{
	// Calculate the total lambdas, smart pointers and commits for all authors
	int totalCommits = 0;
	int totalLambas = 0;
	int totalSmartPointers = 0;
	for (int i = 0; i < all_authors.size(); i++) {
		totalCommits += all_authors[i].commits;
		totalLambas += all_authors[i].lambdas;
		totalSmartPointers += all_authors[i].smartPointers;
	}

	// --------------------------------------------------------------------------------
	// Create all cJSON objects to represent the repository
	// --------------------------------------------------------------------------------
	cJSON* parent = NULL;
	parent = cJSON_CreateObject();
	if (parent == NULL) {
		return NULL;
	}

	// Create all the fields
	cJSON* reponame_field = cJSON_CreateString(repoName.c_str());
	cJSON* MRE_field = cJSON_CreateNumber(MRE);
	cJSON* totalCommits_field = cJSON_CreateNumber(totalCommits);
	cJSON* totalLambdas_field = cJSON_CreateNumber(totalLambas);
	cJSON* totalSmartPointers_field = cJSON_CreateNumber(totalSmartPointers);
	cJSON* numberOfAuthors_field = cJSON_CreateNumber(all_authors.size());
	cJSON* array = cJSON_CreateArray();

	// Add all the fields to the parent
	cJSON_AddItemToObject(parent, "repository_name", reponame_field);
	cJSON_AddItemToObject(parent, "MRE", MRE_field);
	cJSON_AddItemToObject(parent, "total_commits", totalCommits_field);
	cJSON_AddItemToObject(parent, "total_lambdas", totalLambdas_field);
	cJSON_AddItemToObject(parent, "total_smartpointers", totalSmartPointers_field);
	cJSON_AddItemToObject(parent, "total_contributors", numberOfAuthors_field);
	cJSON_AddItemToObject(parent, "contributors", array);


	// --------------------------------------------------------------------------------
	// Add all contributors to the array as JSON objects
	// --------------------------------------------------------------------------------
	for (int i = 0; i < all_authors.size(); i++)
	{
		// Create a cJSON objects for the current contributor and add it to the array
		cJSON* currentContributor = NULL;
		currentContributor = cJSON_CreateObject();
		if (currentContributor == NULL) {
			std::cerr << "ERROR! Failed to convert " << all_authors[i].name << " to JSON format. Skipping this contributor..." << std::endl;
			continue;
		}
		cJSON_AddItemToArray(array, currentContributor);

		// Create all fields for the current contributor
		cJSON* username_field = cJSON_CreateString(all_authors[i].name);
		cJSON* devExperience_field = cJSON_CreateNumber(all_authors[i].lastCommit - all_authors[i].firstCommit);
		cJSON* URE_field = cJSON_CreateNumber(all_authors[i].URE);
		cJSON* commits_field = cJSON_CreateNumber(all_authors[i].commits);
		cJSON* lambdas_field = cJSON_CreateNumber(all_authors[i].lambdas);
		cJSON* smartPointers_field = cJSON_CreateNumber(all_authors[i].smartPointers);

		// Add all fields to the current contributor
		cJSON_AddItemToObject(currentContributor, "username", username_field);
		cJSON_AddItemToObject(currentContributor, "developer_experience", devExperience_field);
		cJSON_AddItemToObject(currentContributor, "URE", URE_field);
		cJSON_AddItemToObject(currentContributor, "commits", commits_field);
		cJSON_AddItemToObject(currentContributor, "lambdas", lambdas_field);
		cJSON_AddItemToObject(currentContributor, "smartpointers", smartPointers_field);
	}

	return parent;
}



