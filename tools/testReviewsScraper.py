import re
import json
import requests
import sqlite3
from urllib.parse import urlencode
from bs4 import BeautifulSoup

# Initialize a SQLite database connection
conn = sqlite3.connect('company_review_data.db')
cursor = conn.cursor()

# Create a table to store company review data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        company_id TEXT PRIMARY KEY,
        company_name TEXT,
        company_reviews TEXT,
        company_ratings TEXT,
        company_keywords TEXT
    )
''')

def save_company_to_database(company_id, company_name, company_reviews, company_ratings, company_keywords):
    cursor.execute('''
        INSERT INTO companies (company_id, company_name, company_reviews, company_ratings, company_keywords)
        VALUES (?, ?, ?, ?, ?)
    ''', (company_id, company_name, company_reviews, company_ratings, company_keywords))
    conn.commit()

def get_indeed_company_url(company_id):
    return f"https://www.indeed.com/cmp/{company_id}"

headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

company_id_list = []

# Company Search Parameters
company_name_list = ['example_company']
company_location_list = ['anywhere']

# Loop Through Indeed Pages Until No More Companies
for company_name in company_name_list:
    for company_location in company_location_list:
        try:
            indeed_company_url = get_indeed_company_url(company_name)

            # Send URL To ScrapeOps Instead of Indeed
            response = requests.get(
                url='https://proxy.scrapeops.io/v1/',
                params={
                    'api_key': '368ff5f6-f062-4cc3-b874-d08d6a7a1ff3',
                    'url': indeed_company_url,
                },
            )

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                company_id = re.search(r'/cmp/([^/]+)', indeed_company_url).group(1)
                company_name = soup.find('span', class_='cmp-HeadingSection-companyName').text.strip()
                company_reviews = soup.find('div', class_='cmp-AboutCompanyWidget-text').text.strip()
                company_ratings = soup.find('span', class_='cmp-HeaderCompanyReview-ratings').text.strip()
                company_keywords = soup.find('div', class_='cmp-KeywordList-keywordList').text.strip()

                # Insert company data into the database
                save_company_to_database(company_id, company_name, company_reviews, company_ratings, company_keywords)
                company_id_list.append(company_id)

        except Exception as e:
            print('Error', e)

print(company_id_list)

# Close the database connection
conn.close()
