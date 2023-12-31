import requests
#from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urlencode
import re
import json
import html
from bs4 import BeautifulSoup

def create_database():
    conn = sqlite3.connect('testReviews.db')
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS
            jobs
    """)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            company_reviews NUMERIC,
            job_title TEXT,
            job_description TEXT,
            job_salaryHigh NUMERIC,
            job_salaryLow NUMERIC,
            job_keywords TEXT,
            job_city TEXT,
            job_state TEXT,
            URL TEXT
        )
    ''')

    conn.commit()
    #conn.close()

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

    conn = sqlite3.connect('testReviews.db')
    cursor = conn.cursor()

    company_ids = {}
    current_company_id = 1

    while True:
        
        for offset in range(0, 1010, 10):
            indeed_jobs_url = get_indeed_search_url("aerospace", "United States", offset)
            response = requests.get(scrapeops_url(indeed_jobs_url))
            script_tag = re.search(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)

            if response.status_code == 200:
                
                if script_tag is not None:
                    json_blob = json.loads(script_tag.group(1))
        
                # Extract jobs data
                    jobs_list =json_blob['metaData']['mosaicProviderJobCardsModel']['results']      
                
                    for job in jobs_list:
                        if job.get('jobkey') is not None:
                            company_name = job.get('company')
                            company_reviews = job.get('companyRating')
                            job_title = job.get('displayTitle')
                            job_description = job.get('snippet') #after second u003E
                            #cut off at backwards slash
                            #take out initial string "snippet":"\u003Cul style=\"list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;\"\u003E \n \u003Cli
                            job_salary = job.get('estimatedSalary')
                            job_salaryHigh = 0
                            job_salaryLow = 0
                            job_keywords = job.get('jobCardReqContainer')
                            job_city = job.get('jobLocationCity')
                            job_state = job.get('jobLocationState')
                            URL = job.get('thirdPartyApplyUrl')
                            
                            if company_name not in company_ids:
                                company_ids[company_name] = current_company_id
                                

                            if company_reviews:
                              company_reviews = company_reviews           
                            else:
                                company_reviews = 9

                            if job_salary:
                                job_salaryHigh = job_salary['max']
                                job_salaryLow = job_salary['min']
                            else:
                                job_salary = "Salary not specified"

                            if job_description:
                                # Remove HTML tags
                                job_description = html.unescape(job_description)
                                job_description = re.sub(r'<[^>]*>', '', job_description)
                                
                            else:
                                job_description = "Description not specified"

                            if job_keywords:
                                job_keywords = job_keywords 
                            else:
                                job_keywords = "No keywords specified"

                            if job_city:
                                job_city = job_city
                            else:
                                job_city = "City not specified"

                            if job_state:
                                job_state = job_state
                            else:
                                job_state = "State not specified"
                         
                            if URL:
                                    company_page = requests.get(scrapeops_url(URL))
                                    if company_page.status_code == 200:
                                        soup = BeautifulSoup(company_page.content, 'html.parser')

                                        company_reviews_element = soup.find('span', class_='cmp-ReveiwsList')
                                        company_ratings_element = soup.find('span', class_='aggregateRating')

                                        if company_reviews_element:
                                            company_reviews = company_reviews_element.text.strip()
                                        else:
                                            company_reviews = "Reviews not available"

                                        if company_ratings_element:
                                            company_ratings = company_ratings_element.text.strip()
                                        else:
                                            company_ratings = "Ratings not available"
                        cursor.execute('''
                            INSERT INTO jobs (company_name, company_reviews, job_title, job_description, job_salaryHigh, job_salaryLow, job_keywords, job_city, job_state, URL)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (company_name, company_reviews, job_title, job_description, job_salaryHigh, job_salaryLow, job_keywords, job_city, job_state, URL))
                        
                        tags = 'placeholder'
                        Job.newJob(job_title,tags,current_company_id,job_city,job_state,job_salaryLow, job_salaryHigh, job_description)

                        conn.commit()
                        current_company_id += 1

                        ## If response contains less than 10 jobs then stop pagination
                        if len(jobs_list) < 10:
                            print('3')
                            break

                        

if __name__ == "__main__":
    create_database()
    scrape_indeed_aerospace_jobs()
    scrape_indeed_aerospace_jobs.conn.close()
