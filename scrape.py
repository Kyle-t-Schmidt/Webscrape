# Title: Web Scrape
# Author: Kyle Schmidt
# Date: 12/22/19
# Description: This program is run from the command line and takes a 2 character country code and returns a list of the
# top beers (up to 100) from that country with the brewery name, beer name, beer type alcohol by volume (ABV), number of
# reviews and average review. The list is filtered by average review. If a blank '' is passed as the country code a list
# of the top 250 beers worldwide is returned. The information is scraped from https://www.beeradvocate.com/

# import packages
import sys
import requests
from bs4 import BeautifulSoup
import re
import csv

# base link wiht the top 250 beers
top_link = 'https://www.beeradvocate.com/beer/top-rated/'

# Using argv this creates the link to the web page to be scraped using the user given two character country code
beer_link = top_link + sys.argv[1] + '/'

# Get the raw html from the beer link
req = requests.get(beer_link)

# Make BeautifulSoup object from the raw html
beer_soup = BeautifulSoup(req.text, 'html.parser')

# The following extracts the necessary info from the beautifulsoup object.
# Create a beautifulsoup results object with the brewery names and beer types. these two pieces of information are of
#class muted and within a tags in the html.
brewery_btype = beer_soup.select('.muted > a')

# Extract the brewery names and beer types into a single list
lst_brewery_btype = []
for i in brewery_btype:
    lst_brewery_btype.append(i.getText())

# separate breweries and beer types into separate lists
breweries = lst_brewery_btype[::2]
beer_types = lst_brewery_btype[1::2]

# Get the beer names from the beautifulsoup object. Beer names are within the b tags, inside the a tags.
lst_beers = beer_soup.select('a > b')

# The first and last elements are not beers. Delete the non-beers
del lst_beers[len(lst_beers)-1]
del lst_beers[0]

# The tags are still in the results. Strip the tags from the beers
beers = []
for i in lst_beers:
    beers.append(i.getText())

# Get the ABV beautifulsoup object. The ABV is of class muted but don't have their own tag so I'll have to use regex to
# extract the data.
alc_content = beer_soup.select('.muted')

# First line is not a beer. Delete the non-beer.
del alc_content[0]

# Use regex to extract the ABV from each line
abv = []

for i in alc_content:
    abv.append(re.findall(r'\d+.\d\d', i.text))

# Convert each element in Abv from a list to a float. Insert NA if empty.
for i, j in enumerate(abv):
    if len(j) == 0:
        abv[i] = 'NA'
    else:
        abv[i] = float(j[0])

# Get the number of reviews and average review for each beer beautifulsoup object. They are within b tags and of class
# hr_bottom_light
reviews = beer_soup.select('.hr_bottom_light > b')

# Extract the number of reviews and average reviews for each beer.
num_avg_reviews = []
for i in reviews:
    num_avg_reviews.append(i.getText())

# Separate number of reviews and average reviews into separate lists
num_reviews = num_avg_reviews[::2]
avg_reviews = num_avg_reviews[1::2]

# Remove commas from num_reviews and change num_reviews to int data type
for i, j in enumerate(num_reviews):
    num_reviews[i] = int(j.replace(',', ''))

# Change avg_reviews to float data type
for i, j in enumerate(avg_reviews):
    avg_reviews[i] = float(j)

# Use extracted data to create csv. The user given country code is used for the file name
beer_file = open('Beer_' + sys.argv[1] + '.csv', 'w', newline='')
writer = csv.writer(beer_file)
writer.writerow(['BreweryName', 'BeerName', 'BeerType', 'ABV', 'NumReviews', 'AvgReview'])

for i in range(len(breweries)):
    row = [breweries[i], beers[i], beer_types[i], abv[i], num_reviews[i], avg_reviews[i]]
    writer.writerow(row)

beer_file.close()
