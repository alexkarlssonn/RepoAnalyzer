
#include "definitions.h"
#include <git2.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cstring>
#include <unistd.h>
#include <sys/types.h>
#include <fstream>
#include <regex>
#include <algorithm>

#define DIFF_FILE "commit_diff.txt"

static int countLambdasAndSmartPointers(const std::string& file, int* lambda_counter, int* smartPointer_counter);
static std::vector<std::string> getValidFileExtensions();

/* 
 * ------------------------------------------------------------------------------------------------
 * This function will go through all commits for the given repository and count the total number of
 * lambdas and smart pointers for each contributor. The results will be saved in the parameter "all_authors"
 * 
 * Returns 0 success and -1 on failure
 * ------------------------------------------------------------------------------------------------ 
 */
int countAdvancedCodeFeatures(const std::string& repoPath, std::vector<AuthorData>& all_authors)
{
	// --------------------------------------------------------------------------------
	// Calculate the commits for the entire repo
	// --------------------------------------------------------------------------------
	int totalCommits = 0;
	for (int i = 0; i < all_authors.size(); i++) {
		totalCommits += all_authors[i].commits;
	}

	// --------------------------------------------------------------------------------
	// Create the DIFF_FILE that stores the output from the git diff command later
	// --------------------------------------------------------------------------------
	std::string rm_command = "rm -f ";
	rm_command += DIFF_FILE;
	std::string touch_command = "touch ";
	touch_command += DIFF_FILE;
	system(rm_command.c_str());
	system(touch_command.c_str());


	// --------------------------------------------------------------------------------
	// Open the given repository
	// --------------------------------------------------------------------------------
	std::string path = repoPath;
	path += "/.git";
	git_repository* repo = NULL;
	if (git_repository_open(&repo, path.c_str()) < 0) {
	    std::cerr << "Failed to open repository: " << path << std::endl;
	    system(rm_command.c_str());
	    return -1;
	}

	// Try both master and main when reading HEAD
	std::string path_master = path;
	path_master += "/refs/heads/master";
	std::string path_main = path;
	path_main += "/refs/heads/main";

	// Open the file for HEAD
	FILE* head_fileptr;
	if ((head_fileptr = fopen(path_master.c_str(), "r")) == NULL) {
	    if ((head_fileptr = fopen(path_main.c_str(), "r")) == NULL) {
	        std::cerr << "Failed to read HEAD. Error when opening file, tried both: " << path_master << ", and: " << path_main << std::endl;
	        git_repository_free(repo);
	        system(rm_command.c_str());
	        return -1;
	    }
	    path_master = path_main;
	}

	// Read the content of the file
	char head_rev[41];
	if (fread(head_rev, 40, 1, head_fileptr) != 1) {
	    std::cerr << "Failed to read HEAD. Error when reading from: " << path_master << std::endl;
	    fclose(head_fileptr);
	    git_repository_free(repo);
	    system(rm_command.c_str());
	    return -1;    
	}

	fclose(head_fileptr);



	// --------------------------------------------------------------------------------
	// Create a git_oid object
	// --------------------------------------------------------------------------------
	git_oid oid;
	if (git_oid_fromstr(&oid, head_rev) < 0) {
	    std::cerr << "Failed to create git object from the content that was read from HEAD" << std::endl;
	    git_repository_free(repo);
	    system(rm_command.c_str());
	    return -1;
	}

	// --------------------------------------------------------------------------------
	// Create a "walker" that will be used to go through all the commits
	// --------------------------------------------------------------------------------
	git_revwalk* walker = NULL;
	git_revwalk_new(&walker, repo);
	git_revwalk_sorting(walker, GIT_SORT_TOPOLOGICAL | GIT_SORT_TIME);
	git_revwalk_push(walker, &oid);

	// --------------------------------------------------------------------------------
	// Loop through all the commits in the current branch
	// --------------------------------------------------------------------------------
	fprintf(stdout, "Progress: ");
	fflush(stdout);
	int counter = 0;
	int segment = 2;
	git_commit* commit = NULL;
	while (git_revwalk_next(&oid, walker) != GIT_ITEROVER) 
	{
		// --------------------------------------------------------------------------
		// Print a progress bar
		// --------------------------------------------------------------------------
		counter++;
		int percentage = (int) 100 * (counter / (double)totalCommits);
		if (percentage >= segment) {
			fprintf(stdout, "#");
			fflush(stdout);
			segment += 2;
		}

		// --------------------------------------------------------------------------
	    // Lookup the next commit
	    // --------------------------------------------------------------------------
	    if (git_commit_lookup(&commit, repo, &oid) < 0) {
	        std::cerr << "\nFailed to lookup the next commit while checking repo: " << repoPath << std::endl;
	        if (commit) git_commit_free(commit);
	        git_revwalk_free(walker);
	        git_repository_free(repo);
	        system(rm_command.c_str());
	        return -1;
	    }

	    // Ignore the author if it's GitHub. This author is used to perform all the merged pull requests
	    const git_signature* commit_signature = git_commit_committer(commit);
	    if (strcmp(commit_signature->name, "GitHub") == 0) {
	    	git_commit_free(commit);
	        continue;
	    }
	    
	    // --------------------------------------------------------------------------
	    // Get the commit id and convert it to a hex string
	    // --------------------------------------------------------------------------
	    const git_oid* commit_id = git_commit_id(commit);
	    std::string commit_hash;
	    char hex_str[256];
	    int i;
	    for (i = 0; i < sizeof(commit_id->id); i++)
	        sprintf((hex_str + i*2), "%02x", commit_id->id[i]);
	    hex_str[i*2] = '\0';
	    commit_hash.append(hex_str);


	    // -----------------------------------------------------------------------------------------
	    // Generate a diff file containing the difference between the current- and previous commit
	    // -----------------------------------------------------------------------------------------
	    std::string cmd = "git --git-dir=";  // Shell command for calling git diff. The output is saved to the given DIFF_FILE
	    cmd = cmd + repoPath + "/.git diff " + commit_hash + "^! > " + DIFF_FILE;
	    
	    // Fork a child process
	    int pid = fork();
	    if (pid == -1) {
	        std::cerr << "\nERROR! Failed to fork a child process..." << std::endl;
	        git_commit_free(commit);
	        git_revwalk_free(walker);
	        git_repository_free(repo);
	        system(rm_command.c_str());
	        return -1;
	    }

	    // Execute the shell command and wait for the child process to finish
	    if (pid == 0) {
	        execl("/bin/sh", "sh", "-c", cmd.c_str(), 0);
	        return 0;
	    }
	    while (wait(NULL) > 0) ;

	    // -----------------------------------------------------------------------------------
	    // Count the advanced code features, and update the author data with the new values
	    // -----------------------------------------------------------------------------------
	    int lambda_counter = 0;
	    int smartPointer_counter = 0;
	    if (countLambdasAndSmartPointers(DIFF_FILE, &lambda_counter, &smartPointer_counter) == -1) {
	    	std::cerr << "\nFailed to count lambdas and smart pointers in repo: " << repoPath << ", in commit: " << commit_hash << std::endl;
	    	git_commit_free(commit);
	    	continue;
	    }

	    for (int i = 0; i < all_authors.size(); i++) {
	    	if (strcmp(all_authors[i].name, commit_signature->name) == 0) {
	    		all_authors[i].lambdas += lambda_counter;
	    		all_authors[i].smartPointers += smartPointer_counter;
	    		break;
	    	}
	    }

	    if (commit)
	    	git_commit_free(commit);
	} 

	fprintf(stdout, "\n");
	git_revwalk_free(walker);
	git_repository_free(repo);
	system(rm_command.c_str());

	return 0;	
}



/**
 * ------------------------------------------------------------------------------------------------
 * This function searches for, and counts lambdas and smart pointers for the given "git diff"-file
 * It only checks files that has a "valid" file extension, and also only counts lambdas/smart pointers that has been ADDED, according to the diff-file
 * 
 * Sets the parameters "lambda_counter" and "smartPointer_counter" to the results.
 *
 * Returns 0 on success, and -1 on failure
 * ------------------------------------------------------------------------------------------------ 
 */
static int countLambdasAndSmartPointers(const std::string& file, int* lambda_counter, int* smartPointer_counter)
{
	std::vector<std::string> validFileExtensions = getValidFileExtensions();
	std::regex lambda_regex(R"([\,\=\s\(\)]*[\,\=\s\t\(\)]+\[[a-zA-Z0-9\*\,_&\s=:<>]*\]\s*(\(|\{))", std::regex::optimize);
	std::regex smartptr_regex(R"(unique_ptr|auto_ptr|shared_ptr|weak_ptr)", std::regex::optimize);

	// Open the diff file
	std::ifstream fromFile(file);
	if (!fromFile.is_open()) {
		return -1;
	}

	// Read the diff file line by line
	std::string line;        
	bool isFileChunk = false;
	bool isInsideBlockComment = false;
	while (std::getline(fromFile, line))
	{
		// Check if the current line signals the start of a new file chunk. If so, then set the variable to false
		if (line.size() > 3) {
		    bool isAdd = (line[0] == '+' && line[1] == '+' && line[2] == '+');
		    bool isSub = (line[0] == '-' && line[1] == '-' && line[2] == '-');
		    if (isAdd || isSub) {
		        isFileChunk = false;
		        isInsideBlockComment = false;
		    }
		}
		
		// If we are inside a valid file chunk right now, then look for lines where code has been added, and search them for lambdas and smart pointers
		if (isFileChunk) 
		{
			if (line.size() > 2 && line[0] == '+') {
			    line.erase(0, 1);  // Remove the first '+' character
			    
			    // Remove all strings from the line
			    size_t stringPos = 0;
			    size_t endStringPos = 0;
			    if ((stringPos = line.find_first_of("\"")) != std::string::npos) {
			        if ((endStringPos = line.find_last_of("\"")) != std::string::npos) {
			            line.erase(stringPos + 1, endStringPos - stringPos - 1);
			        }
			    }
			    stringPos = 0;
			    
			    // If we are inside a block comment and '*/' is found, then we are now outside the block comment
			    if (isInsideBlockComment) { 
			        if (line.find("*/") == std::string::npos) { 
			            isInsideBlockComment = false;
			        }
			    }
			    // We are not inside a block comment right now
			    else
			    {
			        // Skip '/*' comments
			        if ((stringPos = line.find("/*")) != std::string::npos) 
			        {
			        	std::string substring = line.substr(0, stringPos);

			            // Check for lambda before the block comment    
			            if (std::regex_search(substring, lambda_regex)) {
			                *lambda_counter += 1;
			            }

			            // Check for smart pointer before the block comment 
			            if (std::regex_search(substring, smartptr_regex)) {
			            	*smartPointer_counter += 1;
			            }

			            // If '*/' is not found on this line, that means the following lines will be inside a block comment
			            if (line.find("*/") == std::string::npos) {
			                isInsideBlockComment = true;
			            }
			        }
			        
			        // Skip '//' comments
			        else if ((stringPos = line.find("//")) != std::string::npos) 
			        {
			        	std::string substring = line.substr(0, stringPos);

			            // Check for lambda before the line comment    
			            if (std::regex_search(substring, lambda_regex)) {
			                *lambda_counter += 1;
			            }

			            // Check for smart pointer before the line comment
			            if (std::regex_search(substring, smartptr_regex)) {
			            	*smartPointer_counter += 1;
			            }

			        }

			        // No code comment was found, just check the line for lambda and/or smart pointer
			        else {
			        	if (std::regex_search(line, lambda_regex)) {
			        	    *lambda_counter += 1;
			        	}
			        	else if (std::regex_search(line, smartptr_regex)) {
			        		*smartPointer_counter += 1;
			        	}
			        }
			    }
			}
		}

		// If we are not inside a valid file chunk right now, then check if the line signals that an addition to a valid file has occured
		if (!isFileChunk)
		{
		    if (line.size() > 3 && line[0] == '+' && line[1] == '+' && line[2] == '+') {
		        std::string file_extension = line.substr(line.find_last_of(".") + 1);
		        for (int i = 0; i < validFileExtensions.size(); i++) {
		            if (validFileExtensions[i] == file_extension) {
		                isFileChunk = true;
		                isInsideBlockComment = false;
		                break;
		            }    
		        }        
		    }
		}
	}

	// Close the file and return the data structure that contains the number of lambdas and smart pointers
	fromFile.close();
	
	return 0;
}




/**
 * ------------------------------------------------------------------------------------------------
 * Returns the valid file extensions to be used when searching for advanced code features
 * ------------------------------------------------------------------------------------------------ 
 */
static std::vector<std::string> getValidFileExtensions()
{
    std::vector<std::string> fe;
    fe.push_back("cpp");
    fe.push_back("cc");
    fe.push_back("c");
    fe.push_back("cxx");
    fe.push_back("c++");
    fe.push_back("h");
    fe.push_back("hpp");
    fe.push_back("hh");
    fe.push_back("hxx");
    fe.push_back("h++");

    return fe;
}








