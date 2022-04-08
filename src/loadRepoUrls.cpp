
#include "definitions.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

/* ------------------------------------------------------------------------------------------------
 * Returns a vector of all repository URL's that was placed inside the given file on success
 * Returns an empty vector on failure or in no repos was found
 * ------------------------------------------------------------------------------------------------ */
std::vector<std::string> loadRepoUrls()
{
	std::vector<std::string> allRepos;

	// Open the file
	std::ifstream fromFile(PLACE_REPOS_HERE);
	if (fromFile.fail()) {
	    std::cerr << "ERROR! The file: " << PLACE_REPOS_HERE << " doesn't exist" << std::endl;
	    return allRepos; 
	}

	// Read the file line by line
	std::string line;  
	while (std::getline(fromFile, line)) 
	{
	    // Skip lines that have been commented out or are empty
	    if ((!line.empty() && line[0] == '#') || line.empty()) {
	        continue;
	    }
	    allRepos.push_back(line);
	}

	return allRepos;
}