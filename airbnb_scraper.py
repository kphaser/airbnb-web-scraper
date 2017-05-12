# Web crawler and scraper of Airbnb listings data
# based on location specification
###################################################
# PREDICT 452 Winter 2017 - Assignment 1
# Kevin Wong
###################################################

# prepare for Python version 3x features and functions
from __future__ import division, print_function

import scrapy
import os

# function for walking and printing directory structure
def list_all(current_directory):
    for root, dirs, files in os.walk(current_directory):
        level = root.replace(current_directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


# examine the directory structure
current_directory = os.getcwd()
list_all(current_directory)

# list the avaliable spiders, showing names to be used for crawling
os.system('scrapy list')

# text output that is easily readable in a plain text editor in either
# csv, json, or xml format
os.system('scrapy crawl airbnb -o listings_test.csv')
# os.system('scrapy crawl airbnb -o listings.json')
# os.system('scrapy crawl airbnb -o listings.xml')
