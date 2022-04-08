
#include "definitions.h"
#include "libs/cJSON.h"
#include <fstream>
#include <string>
#include <iostream>

/**
 * ------------------------------------------------------------------------------------------------
 * Saves the given cJSON object to the OUTPUT_FILE
 * Returns 0 on success and -1 on failure
 * ------------------------------------------------------------------------------------------------ 
 */
int saveToOutputFile(cJSON* repo_json, bool append_mode)
{
	if (repo_json == NULL) {
		return -1;
	}

	// Not being in append mode means that the output file will be reset, and the given respoitory will be written to it
	if (!append_mode)
	{
		cJSON* parent_json = cJSON_CreateObject();
		if (parent_json == NULL) {
			return -1;
		}
		cJSON* array = cJSON_CreateArray();
		if (array == NULL) {
			cJSON_Delete(parent_json);
			return -1;
		}

		cJSON_AddItemToObject(parent_json, "repos", array);
		cJSON_AddItemToArray(array, repo_json);

		// Convert the entire cJSON object to a string
		char* buffer = cJSON_Print(parent_json);
		cJSON_Delete(parent_json);
		if (buffer == 0) {
			return -1;
		}

		// Write the string to the output file
		std::fstream toFile;
		toFile.open(OUTPUT_FILE, std::ios::out | std::ios::trunc);
		if (!toFile.is_open()) {
		    std::cerr << "ERROR! Failed to open: " << OUTPUT_FILE << std::endl;
		    if (buffer != 0) 
		    	free(buffer);
		    return -1; 
		}
		toFile << buffer;
		toFile.close();

		if (buffer != 0)
			free(buffer);
	}

	// Append mode means that there is already repositories saved to the output file, so append repo_json to the file
	if (append_mode)
	{
		// Read the content of the output file
		std::ifstream fromFile;
		fromFile.open(OUTPUT_FILE);
		if (!fromFile.is_open()) {
		    std::cerr << "ERROR! Failed to open: " << OUTPUT_FILE << std::endl;
		    return -1; 
		}
		std::string file_data((std::istreambuf_iterator<char>(fromFile)), std::istreambuf_iterator<char>());
		fromFile.close();

		// Parse file data to cJSON
		cJSON* parent_json = NULL;
		parent_json = cJSON_Parse(file_data.c_str());
		if (parent_json == NULL) {
			std::cerr << "ERROR! Failed to parse " << OUTPUT_FILE << " to cJSON when trying to append new results to it" << std::endl;
			return -1;
		}

		// Append the current repository to the existing array of repos
		cJSON* repos = NULL;
		repos = cJSON_GetObjectItemCaseSensitive(parent_json, "repos");
		if (repos == NULL) {
			std::cerr << "ERROR! Failed to parse " << OUTPUT_FILE << " to cJSON when trying to append new results to it" << std::endl;
			cJSON_Delete(parent_json);
			return -1;
		}
		cJSON_AddItemToArray(repos, repo_json);

		// Convert the entire cJSON object to a string
		char* buffer = cJSON_Print(parent_json);
		cJSON_Delete(parent_json);
		if (buffer == 0) {
			return -1;
		}

		// Write the string to the output file
		std::fstream toFile;
		toFile.open(OUTPUT_FILE, std::ios::out | std::ios::trunc);
		if (!toFile.is_open()) {
		    std::cerr << "ERROR! Failed to open: " << OUTPUT_FILE << std::endl;
		    if (buffer != 0) 
		    	free(buffer);
		    return -1; 
		}
		toFile << buffer;
		toFile.close();

		if (buffer != 0)
			free(buffer);
	}

	return 0;
}



