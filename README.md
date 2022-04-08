# README

## About
  
This program is used to analyze C++ GitHub repositories.  
The goal is to be able to find out if there is a correlation between developers with higher "experience", and a more frequent use of advanced code features.  
The advanced code features this program will look at are lambdas and smart pointers.  
  
The program takes a number of GitHub repositories as input, and places the analyzed results inside a JSON file.  
  
  

## How to use the program  

The program will take a number of GitHub repositories as input, and place the analyzed results inside a JSON file.  
Before starting the program, place all C++ repositories you want to be analyzed inside the file: PLACE_REPOS_HERE.txt  
Only include C++ repositories since all other repositories will be ignored.  
  
PLACE_REPOS_HERE.txt  
Place the full URL's of the repositories here. One repository per line  
If you want to include line commments, then use the '#' character.
```
https://github.com/randomusername/randomreponame
url2
url2
# This is a comment, this line will be skipped
...

```
  

## How to build on Linux  
  
The program requires the libgit2 library  

ALWAYS update the OS first!  
sudo apt update  
sudo apt full-upgrade -y  
install cmake (apt install cmake)  
install openssl (apt install libssl-dev)  
install git (apt install git)  
install g++ (apt install g++)  
install libgit2 (apt install libgit2-dev)  
install curl for openssl (apt install libcurl4-openssl-dev)  
Download Github User Repository Analyser (git clone https://github.com/marcusroos1904/github-user-repository-analyser.git)  
Once finished > cd to github user repository analyser root > 'make'  
Place the repos you want to analyze inside PLACE_REPOS_HERE.txt  
Run the program!  
  

## How to build on MacOS
  
To build the project, run make inside the directory  
  
In order for the project to build, you need to have libgit2 installed, and 2 other libraries.  
Here is a step by step guide that should work using Homebrew:  

brew install openssl  
brew install libssh2  
brew install libgit2 
  
Make sure libgit2 was installed inside: /usr/local/Cellar/libgit2/1.3.0  
If it was installed somwhere else, or if the version number is different, then you should change the directory paths inside the Makefile   

Once these libraries have been installed:  
Download Github User Repository Analyser (git clone https://github.com/marcusroos1904/github-user-repository-analyser.git)  
Once finished > cd to github user repository analyser root > 'make'  
Place the repos you want to analyze inside PLACE_REPOS_HERE.txt  
Run the program!  
  


  
