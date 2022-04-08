
#include "definitions.h"
#include <vector>
#include <algorithm>

/**
 * ------------------------------------------------------------------------------------------------
 * Calculates the MRE score and URE scores for each author that was passed as the parameter: all_authors
 * The vector is passed by reference and will be updated with the URE values, and the MRE value will be
 * set to the parameter MRE
 * 
 * Returns 0 on success and -1 on failure
 * ------------------------------------------------------------------------------------------------ 
 */
int calculateMREandURE(std::vector<AuthorData>& all_authors, int* MRE)
{
	// Remove all authors that has less than 2 commits in total
	all_authors.erase(std::remove_if(all_authors.begin(), all_authors.end(), [](const AuthorData& ad) {
		return (ad.commits <= 0 || ad.firstCommit <= 0 || ad.lastCommit <= 0);
	}), all_authors.end());

	if (all_authors.empty()) {
		return -1;
	}

	// Sort all authors by the time between their oldest and newest commits
	std::sort(all_authors.begin(), all_authors.end(), [](const AuthorData& ad1, const AuthorData& ad2) {
		return (ad1.lastCommit - ad1.firstCommit) < (ad2.lastCommit - ad2.firstCommit);
	});


	// Calculate the MRE value
	if (all_authors.size() % 2 == 0) 
	{
		// Even number of authors, calculate the average of the two authors in the middle
		int mean_index = (all_authors.size() / 2);
		if (mean_index < 0 || mean_index + 1 >= all_authors.size()) {
			return -1;
		}
		int MRE_1 = (all_authors[mean_index].lastCommit - all_authors[mean_index].firstCommit);
		int MRE_2 = (all_authors[mean_index + 1].lastCommit - all_authors[mean_index + 1].firstCommit);
		*MRE = (int)((MRE_1 + MRE_2) / 2);
	}
	else
	{
		// Odd number of authors, the mean is in the middle
		int mean_index = (all_authors.size() / 2);
		if (mean_index < 0 || mean_index >= all_authors.size()) {
			return -1;
		}
		*MRE = (all_authors[mean_index].lastCommit - all_authors[mean_index].firstCommit);
	}


	// Calculate the URE value for each author
	for (int i = 0; i < all_authors.size(); i++) {
		double percentile = ((i+1) / (double)all_authors.size()); 
		all_authors[i].URE = percentile;
	}

	return 0;
}