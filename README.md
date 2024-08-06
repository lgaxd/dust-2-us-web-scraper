# Dust2.us Recent Results Scraper

## Overview
This Python script scrapes the recent match results from the Dust2.us website. The script fetches the latest matches, including the date, teams involved, and the final scores, and prints them out in a readable format.

## Requirements
Python 3.x
requests library
beautifulsoup4 library

## How It Works
Fetching the Webpage: The script sends a GET request to the Dust2.us results page to fetch the HTML content.

Parsing the HTML: The script uses BeautifulSoup to parse the HTML content and locate the section containing match results.

Extracting Match Data: The script iterates through each match entry, extracting the date, team names, and scores.

Formatting and Output: The script formats the extracted data and prints it in a readable format.

The script is designed to work with the current structure of the Dust2.us results page and may require updates if the webpage structure changes.
