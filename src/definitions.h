
#pragma once

#include "libs/cJSON.h"
#include <vector>
#include <string>

#define PLACE_REPOS_HERE "PLACE_REPOS_HERE.txt"
#define CLONED_REPOS_DIR "./repos/"
#define OUTPUT_FILE "output.json"

struct AuthorData {
    char name[256];
    int firstCommit = 0;
    int lastCommit = 0;
    int commits = 0;
    int lambdas = 0;
    int smartPointers = 0;
    double URE = 0.0;
};


std::vector<std::string> loadRepoUrls();
std::string extractRepoName(const std::string& url);
int validateUrl(const char *url);
int cloneRepository(const std::string& repoPath, const std::string& repoUrl);
std::vector<AuthorData> extractAuthorData(const std::string& repoPath);
int calculateMREandURE(std::vector<AuthorData>& all_authors, int* MRE);
int countAdvancedCodeFeatures(const std::string& repoPath, std::vector<AuthorData>& all_authors);
cJSON* convertToJSON(const std::string& repoName, int MRE, const std::vector<AuthorData>& all_authors);
int saveToOutputFile(cJSON* repo_json, bool append_mode);



