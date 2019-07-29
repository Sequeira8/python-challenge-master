# Aptoide - Python Challenge

## Introduction

This project is based in the python-challenge-master - Aptoide.


# Objective

Develop an autocomplete API that helps users searching for apps by
their name.


# System Files

The system is composed of:
* An autocomplete file that stores all the apps names available and searches for sugestions to present to the user for a given input
* An API that receives a query from the user and returns the possible results for that query
* Templates rendered by the API
* Test files for system testing
* Docker files for the virtual machine environment


## Execution

Make sure to download the project into your computer.
The system only shows a maximum of 8 suggestions to the user, you can change this number on the autocomplete.py file line 72.


# Requirements

* Install "Docker Desktop"
* Install Python 3.7.4
* Install pip 19.2.1


# Test System with Docker-Compose

* Open python-challenge-master folder
* Right click on the folder and open git bash if you have it OR copy the path of the folder, open windows cmd and run " cd *path* "
* Run docker-compose up --build and wait until a message saying "Running on ..." appears in the terminal
* Open your browser and type: "localhost:8080"
* Test the app by inserting any names you want

Note: The names used are the ones in the "main/test_files/6500.csv" file


# Test System without Docker-Compose

* Open python-challenge-master/main folder
* Open git bash or cmd in the current path
* Run " python api.py *inputfile* " and switch *inputfile* with any csv file you would like. In case you don't type any inputfile the test_files/6500.csv its used by default. Wait until a message saying "Running on ..." appears in the terminal
* Open your browser and type: "localhost:8080"
* Test the app by inserting any names you want


# Run test.py files

* Open python-challenge-master/main folder
* Open git bash or cmd in the current path
* Run " python -m unittest discover tests
