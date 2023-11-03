import requests
#from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urlencode
import re
import json

def create_database():
    conn = sqlite3.connect('indeed_aerospace_jobs.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            company_reviews TEXT,
            job_title TEXT,
            job_description TEXT,
            job_salary_range TEXT,
            job_keywords TEXT,
            job_location TEXT
        )
    ''')

    conn.commit()
    conn.close()

def get_indeed_search_url(keyword, location, offset=0):
    parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
    return "https://www.indeed.com/jobs?" + urlencode(parameters)

##bypass indeed blocking
def scrapeops_url(url):
    SCRAPEOPS_API_KEY = '1bcf4bb7-35b1-47e3-91b9-1053edd36bc7'
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

def scrape_indeed_aerospace_jobs():

    conn = sqlite3.connect('indeed_aerospace_jobs.db')
    cursor = conn.cursor()
    print(0.5)
    while True:
        print(0.75)
        indeed_jobs_url = get_indeed_search_url
        response = requests.get(scrapeops_url(indeed_jobs_url))
        #soup = BeautifulSoup(response.text, 'html.parser')
        #job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
        script_tag = re.search(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)
        
        
        print(response.status_code)
        if response.status_code == 200:
            print(0.8)

            if script_tag is not None:
                json_blob = json.loads(script_tag.group(1))
        
                # Extract jobs data
                jobs_list =json_blob['metaData']['mosaicProviderJobCardsModel']['results']      
                
                for job in jobs_list:
                    if job.get('jobkey') is not None:
                        company_name = job.find('span', class_='company').text.strip()
                        company_reviews = job.find('span', class_='ratingsContent')
                        job_title = job.find('a', class_='jobtitle').text.strip()
                        job_description = job.find('div', class_='summary').text.strip()
                        job_salary = job.find('span', class_='salaryText')
                        job_keywords = job.find('div', class_='jobCardReqContainer')
                        job_location = job.find('div', class_='location')

                        if company_reviews:
                            company_reviews = company_reviews.text.strip()
                            print(1)
                        else:
                            company_reviews = "No reviews"

                        if job_salary:
                            job_salary = job_salary.text.strip()
                        else:
                            job_salary = "Salary not specified"

                        if job_keywords:
                            job_keywords = job_keywords.text.strip()
                        else:
                            job_keywords = "No keywords specified"

                        if job_location:
                            job_location = job_location.text.strip()
                        else:
                            job_location = "Location not specified"

                       ## If response contains less than 10 jobs then stop pagination
                    if len(jobs_list) < 10:
                        print('3')
                        break  
                          

            cursor.execute('''
                INSERT INTO jobs (company_name, company_reviews, job_title, job_description, job_salary_range, job_keywords, job_location)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (company_name, company_reviews, job_title, job_description, job_salary, job_keywords, job_location))

            conn.commit()

        #next_page = soup.find('span', {'aria-label': 'Next'})

            if len(jobs_list) < 10:
                print('3')
                break

    conn.close()

if __name__ == "__main__":
    create_database()
    scrape_indeed_aerospace_jobs()
