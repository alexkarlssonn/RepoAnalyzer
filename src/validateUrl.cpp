
#include "definitions.h"

#include <curl/curl.h>
#include <curl/easy.h>
#include <iostream>

static size_t writeFunction(void *buffer, size_t size, size_t nmemb, void *userp)
{
	return size * nmemb;
}

int validateUrl(const char *url)
{
	CURL* curl;
	CURLcode response;
	curl = curl_easy_init();
	long ct;
	if(curl) {
	    std::cout.setstate(std::ios::failbit);
	    curl_easy_setopt(curl, CURLOPT_URL, url);
	    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeFunction);
	    response = curl_easy_perform(curl);
	    if (CURLE_OK == response){
	        response = curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &ct);
	    }
	}
	curl_easy_cleanup(curl);
	std::cout.clear();
	return (ct != 200) ? 0 : 1;
}

