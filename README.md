# data-pirates
Data Pirates challenge.

Scenario:
The Internet Movie Database (IMDb) is an online database of information about music, movies, TV shows and games and television games computer. [Wikipedia]. This challenge consist to collect information from this site and deliver it in other format.

Requirements:
- Get 500 titles from each genre
- Sorted by 'Rating'
- This app must run with only one command
- The output format is JSONL
- Write each genre in one output file

# How to run?

You need the libraries:
- Python 3
- urllib3 1.22
- BeautifulSoup 4.6.3
- jsonlines 1.2.0

You must execute:
- python main.py

The script will create a file for each genre in the root directory.
