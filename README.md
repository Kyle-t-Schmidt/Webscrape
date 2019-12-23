# webscrape

## Introduction
https://www.beeradvocate.com/ descibes itself as the go-to resource for beer. Beer advocate has user fourms, ratings rankings and descriptions of thousands of beers. I wanted to build a tool that would allow me to easily and quickly extract information on the top rated beers.
In this project I demonstate:
* Extracting useful data from html
* Cleaning messy data and transforming it into a format usfull in data analysis
* The use of Python for data science
* Running a program from the command line

## Program Purpose
The program is meant to by run from the command line. The user passes a two letter country code as an argument and the program creates a csv file of the top beers (up to 100) from that country. the csv file contains the beer name, the brewery name, beer type, alcohol by volume (ABV), number of reviews and the average beer rating on a 1-5 scale for each beer. Passing an empty argument rather than a country code will return a csv with the top 250 rated beers in the world. Several example csvs are given in the repository.

## Using the program
1. Download the scrape.py file and save locally on your computer.
2. From your terminal or command line navigate to the folder where the program is stored.
3. Run the program in python 3 with the two letter country code in quotes (single or double quotes will both work). You may pass an empty argument to get the top 250 beers in the world.

examples of two letter country codes:

* 'us' = United States of America
* 'ca' = Canada
* 'jp' = Japan
* 'gb' = Great Britain
* 'it' = Italy


example of how to run the program:
The below is copied from my terminal. The first line navigates to the folder where I have the program stored. the next 4 lines runs the program and returns csv's with information on the top rated beers from the USA, Canada, Japan and the entire world.

**kyle:~$**  cd ~/PycharmProjects/web-scrape
**kyle:~/PycharmProjects/web-scrape$**  python3 scrape.py 'us'
**kyle:~/PycharmProjects/web-scrape$**  python3 scrape.py 'ca'
**kyle:~/PycharmProjects/web-scrape$**  python3 scrape.py 'jp'
**kyle:~/PycharmProjects/web-scrape$**  python3 scrape.py ''


