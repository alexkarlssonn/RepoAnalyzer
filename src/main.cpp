
#include "definitions.h"
#include "libs/cJSON.h"
#include <git2.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

static void deleteLocalRepo(const std::string& repoPath);


/* 
 * ========================================================================================================================
 * MAIN 
 * This program will clone a number of given GitHub repositories and analyze them
 * The analyzed data will be written to an output file
 * ========================================================================================================================
 */
int main()
{
	// Initiate the libgit2 library
	if (git_libgit2_init() < 0) {
		std::cerr << "Failed to initialise libgit2" << std::endl;
	}

	// ---------------------------------------------------------------
	// Load all repository urls
	// ---------------------------------------------------------------
	std::vector<std::string> allRepos = loadRepoUrls();
	if (allRepos.empty()) {
	    std::cerr << "ERROR! Place the GitHub repositories you want to analyze in: " << PLACE_REPOS_HERE << std::endl;
	    std::cerr << "See the README file for more information on how to user the program" << std::endl;
	    return 1;
	}
	std::cout << "\nLoaded " << allRepos.size() << " repositories from: " << PLACE_REPOS_HERE << std::endl;


	// ---------------------------------------------------------------
	// Create the folder that will hold all the cloned repos
	// ---------------------------------------------------------------
	std::string rm_command = "rm -rf ";
	std::string mkdir_command = "mkdir ";
	rm_command += CLONED_REPOS_DIR;
	mkdir_command += CLONED_REPOS_DIR;
	system(rm_command.c_str());
	system(mkdir_command.c_str());

	// ---------------------------------------------------------------
	// Create/Reset the output file
	// ---------------------------------------------------------------
	std::fstream output_file;
	output_file.open(OUTPUT_FILE, std::ios::out | std::ios::trunc); // | std::ios_base::app);
	if (!output_file.is_open()) {
	    std::cerr << "ERROR! Failed to open: " << OUTPUT_FILE << std::endl;
	    system(rm_command.c_str());
	    return 1; 
	}
	output_file.close();



	// ---------------------------------------------------------------
	// Loop through and analyze all the given repositories
	// ---------------------------------------------------------------
	std::vector<std::string> failedRepos;
	for (int i = 0; i < allRepos.size(); i++)
	{
		// Extract the repository name from the url, and then create the "local path" that will store the cloned repository
		std::string repoName = extractRepoName(allRepos[i]);  
		std::string localRepoPath = CLONED_REPOS_DIR;
		localRepoPath += repoName;

		// ---------------------------------------------------------------
		// Clone the current repo
		// ---------------------------------------------------------------
		std::cout << "\nCloning repository (" << (i+1) << "/" << (allRepos.size()) << "): " << allRepos[i] << std::endl;
		if (!validateUrl(allRepos[i].c_str())) {
		    std::cerr << "ERROR! Invalid repository repo URL: " << allRepos[i] << std::endl;
		    failedRepos.push_back(repoName);
		    continue;
		}
		if (cloneRepository(localRepoPath, allRepos[i]) == -1) {
		    std::cerr << "ERROR! Failed to clone repo: " << allRepos[i] << std::endl;
		    failedRepos.push_back(repoName);
		    deleteLocalRepo(localRepoPath);
		    continue;
		}

		// ---------------------------------------------------------------
		// Extract the data for all authors in the repository
		// ---------------------------------------------------------------
		std::cout << "Gathering repository data..." << std::endl;
		std::vector<AuthorData> all_authors = extractAuthorData(localRepoPath);  
		if (all_authors.empty()) {
		    std::cerr << "ERROR! Failed to extract author data from repo: " << repoName << std::endl;
		    failedRepos.push_back(repoName);
		    deleteLocalRepo(localRepoPath);
		    continue;
		}

		// ---------------------------------------------------------------
		// Calculate MRE for the repo, and URE for all authors
		// ---------------------------------------------------------------
		int MRE = 0;
		if (calculateMREandURE(all_authors, &MRE) == -1) {
			std::cerr << "ERROR! Failed to calculate the MRE and URE values for the repo: " << repoName << std::endl;
			failedRepos.push_back(repoName);
			deleteLocalRepo(localRepoPath);
			continue;
		}

		// ---------------------------------------------------------------
		// Count the advanced code features for each author
		// ---------------------------------------------------------------
		std::cout << "Counting advanced code features..." << std::endl;
		if (countAdvancedCodeFeatures(localRepoPath, all_authors) == -1) {
			std::cerr << "ERROR! Failed to count the advanced code features in the repo: " << repoName << std::endl;
			failedRepos.push_back(repoName);
			deleteLocalRepo(localRepoPath);
			continue;
		}

		// ---------------------------------------------------------------------
		// Convert all results for the current repo into a cJSON object
		// ---------------------------------------------------------------------
		cJSON* repo_json = NULL;
		if ((repo_json = convertToJSON(repoName, MRE, all_authors)) == NULL) {
			std::cerr << "ERROR! Failed to create cJSON object with the analyzed results..." << std::endl;
			failedRepos.push_back(repoName);
			deleteLocalRepo(localRepoPath);
			continue;
		}

		// ---------------------------------------------------------------
		// Save results for the current repo to the output file
		// ---------------------------------------------------------------
		bool append_mode = (i > 0);  // Append results to the file it there is already results saved in it
		if (saveToOutputFile(repo_json, append_mode) == -1) {
			std::cerr << "ERROR! Failed to save the analyzed results to the output file..." << std::endl;
			failedRepos.push_back(repoName);
			deleteLocalRepo(localRepoPath);
			continue;
		}

		// ---------------------------------------------------------------
		// Delete the current repo
		// ---------------------------------------------------------------
		deleteLocalRepo(localRepoPath);
		std::cout << "SUCCESS! Analyzed repositories can be found in: " << OUTPUT_FILE << std::endl;
	}


	// ----------------------------------------------------------------------------------------------------------------
	// Print done text, and list all repositories that failed to be analyzed
	// ----------------------------------------------------------------------------------------------------------------
	std::cout << std::endl << "DONE! Finished going through all " << allRepos.size() << " repositories. See " << OUTPUT_FILE << " for the results" << std::endl;
	if (!failedRepos.empty()) {
	    std::cerr << "Failed to analyze " << failedRepos.size() << " repositories" << std::endl;
	    for (int i = 0; i < failedRepos.size(); i++) {
	        std::cerr << failedRepos[i] << std::endl;
	    }
	} 

	// Delete the folder containing all the cloned repos
	system(rm_command.c_str());
	return 0;
}




/** 
 * =========================================================================================================================
 *  Deletes the given repository
 * ========================================================================================================================= 
 */
static void deleteLocalRepo(const std::string& repoPath)
{
	std::string rm_repo_command = "rm -rf ";
	rm_repo_command += repoPath;
	system(rm_repo_command.c_str());
	return;
}










